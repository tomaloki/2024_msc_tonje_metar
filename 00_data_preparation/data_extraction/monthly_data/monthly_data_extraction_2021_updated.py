#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import pandas as pd
import numpy as np
import os
import time
import pyproj
import glob
import pickle


# In[2]:


airport_location = pd.read_csv('../../data/airport_positions_new.csv')


# In[4]:


parameters = ['air_temperature_0m', 'air_temperature_2m', 'air_temperature_pl', 
              'relative_humidity_2m', 'precipitation_amount_acc', 'x_wind_10m', 'y_wind_10m', 
             'x_wind_pl', 'y_wind_pl', 'fog_area_fraction', 'surface_air_pressure', 'air_pressure_at_sea_level']


# In[10]:


def transform_latitude_longitude_to_xy(latitude_values, longitude_values):
    # Create a pyproj CRS object
    proj4_str = '+proj=lcc +lat_0=63.3 +lon_0=15 +lat_1=63.3 +lat_2=63.3 +no_defs +R=6.371e+06'
    lcc_crs = pyproj.CRS.from_proj4(proj4_str)

    # Create a transformer for converting between lat/lon and x/y
    transformer = pyproj.Transformer.from_crs(pyproj.CRS("EPSG:4326"), lcc_crs, always_xy=True)

    # Transform lat/lon to x/y
    x_values, y_values = transformer.transform(longitude_values, latitude_values)

    return x_values, y_values


# In[13]:


# Define folder with paths and prefix for files to read
folder_path = '/lustre/storeB/immutable/archive/projects/metproduction/meps/2021/'
file_prefix = 'meps_lagged_6_h_subset_2_5km_*.nc'
# file_pattern = os.path.join(folder_path, file_prefix)
#file_list = glob.glob(file_pattern)
output_folder = '/lustre/storeB/users/tonjek/msc/2024_msc_tonje_metar/00_data_preparation/data_extraction/2021/'


# In[14]:


airport_identifier = airport_location['airport_identifier'].unique()
for month_folder in os.listdir(folder_path):
    month_path = os.path.join(folder_path, month_folder)
    all_timesteps_data = []
    for day_folder in os.listdir(month_path):
        day_path = os.path.join(month_path, day_folder)

        file_pattern = os.path.join(day_path, file_prefix)
        file_list = glob.glob(file_pattern)

        print(f"Processing day: Month: {month_folder}, Day: {day_folder}")

        for file_path in file_list:
            data = xr.open_mfdataset(file_path, chunks={'time':1})
            start_time = time.time()
            print(file_path)

            latitude_values = airport_location.latitude.values
            longitude_values = airport_location.longitude.values

            x_values, y_values = transform_latitude_longitude_to_xy(latitude_values, longitude_values)

            airport_six_timesteps = []

            for airport_idx in range(len(latitude_values)):
                nearest_x = x_values[airport_idx]
                nearest_y = y_values[airport_idx]

                #print(f"AIRPORT {airport_idx + 1} COORDINATES:")
                #print(f"  Latitude: {latitude_values[airport_idx]}")
                #print(f"  Longitude: {longitude_values[airport_idx]}")
                #print(f"  Nearest x: {nearest_x}")
                #print(f"  Nearest y: {nearest_y}")

                # Extract latitude and longitude values from the data variable
                lat_from_data = data.latitude.sel(x=nearest_x, y=nearest_y, method='nearest').values.item()
                lon_from_data = data.longitude.sel(x=nearest_x, y=nearest_y, method='nearest').values.item()

                #print(f"  Latitude (Data): {lat_from_data}")
                #print(f"  Longitude (Data): {lon_from_data}")


                interpolated_data = data[parameters].interp(x=nearest_x, y=nearest_y)

                start_datetime = pd.to_datetime(data.time.values[0])  # Convert to pandas datetime
                end_datetime = start_datetime + pd.DateOffset(hours=5)  # Assuming each time step is 1 hour

                extracted_data = interpolated_data.sel(
                    ensemble_member=0,
                    time=slice(start_datetime, end_datetime)
                )
                
                # Calculate precipitation amount

                precipitation_acc = data['precipitation_amount_acc']

                # Calculate precipitation for timestamp
                precipitation = precipitation_acc.diff(dim='time', label='lower')

                # Replace NaN in the first time step with the original value
                precipitation = precipitation.fillna(precipitation_acc.isel(time=0))
                precipitation.attrs = precipitation_acc.attrs
                extracted_data['precipitation_amount'] = precipitation
                # Add airport as a dimension with the corresponding index in airport_identifier
                extracted_data = extracted_data.expand_dims({'airport': [airport_identifier[airport_idx]]})
                airport_six_timesteps.append(extracted_data)
            combined_data = xr.concat(airport_six_timesteps, dim='airport')
            all_timesteps_data.append(combined_data)
            end_time = time.time()
            print(f'Time taken to extract info from {file_path}: {end_time - start_time}')
            #print(f'Dimensions after concatenation for day {day_folder}: {combined_data.dims}')
    final_combined_data = xr.concat(all_timesteps_data, dim='time')
    final_combined_data = final_combined_data.drop_vars('ensemble_member')
    
    # Save pickle
    pickle_filename = f'2021_{month_folder}_UPDATED.pkl'
    pickle_filepath = os.path.join(output_folder, pickle_filename)

    with open(pickle_filepath, 'wb') as pickle_file:
        pickle.dump(final_combined_data, pickle_file)

    print(f"Saved pickle file for file {file_path}: {pickle_filepath}")

