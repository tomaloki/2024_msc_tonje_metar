# Master's Thesis 2024  30 ECTS
Faculty of Science and Technology

## Investigating the Viability of Mchine Learning for the Prediction of Icing Occurrences at Airports
Tonje Martine Lorgen Kirkholt



This repository contain the necessary code to get an overview of the work and processes explained and presented in the thesis. 
Files with code for extraction of data can not be run, as it is used internally at MET.
Due to the final size of the dataset, it was not possible to upload the file to GIT. The data can be handed over by request.

An overview of the files and the different models, which can be located in **03_final_ml_training_test**:

### Persistence
- *persistence_model*: Majority class downsampled by 1%, dataset D1
- *persistence_model_2*: Majority class downsampled by 3.3%, dataset D2
- *perstistence_model_without_AUTO*: All instances of metartype AUTO are removed, dataset D3


### Instantaneous
- *instantaneous_1*: Majority class downsampled by 1%, dataset D1
- *instantaneous_3_3*: Majority class downsampled by 3.3%, dataset D2
- *instantaneous_without_AUTO*: All instances of metartype AUTO are removed, dataset D3


### Temporal
- *lead_1_prediction*: 1 timestep prediction = 1H ahead, dataset D1
- *lead_1_prediction_2*: 1 timestep prediction = 1H ahead, dataset D2
- *lead_2_prediction*: 2 timesteps prediction = 2H ahead, dataset D1
- *lead_2_prediction_2*: 2 timesteps prediction = 2H ahead, dataset D2
- *lead_3_prediction*: 2 timesteps prediction = 2H ahead, dataset D1
- *lead_3_prediction_2*: 3 timesteps prediction = 3H ahead, dataset D2
- *lead_4_prediction*: 3 timesteps prediction = 3H ahead, dataset D1
- *lead_4_prediction_2*: 4 timesteps prediction = 4H ahead, dataset D2
- *lead_5_prediction*: 3 timesteps prediction = 5H ahead, dataset D1
- *lead_5_prediction_2*: 5 timesteps prediction = 5H ahead, dataset D2

Files inside **00_data_preparation** have been used for data extraction. 
Files inside **01_data_analyzation** and **02_machine_learning** show examples of data analyzation and preprocessing.
Files inside **data** contains dataset containing only METAR information used early in the process. 
