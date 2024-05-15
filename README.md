# Master's Thesis 2024  30 ECTS
Faculty of Science and Technology

## Investigating the Viability of Mchine Learning for the Prediction of Icing Occurrences at Airports
Tonje Martine Lorgen Kirkholt



This repository contain the necessary code to get an overview of the work and processes explained and presented in the thesis. 
Files with code for extraction of data can not be run, as it is used internally at MET.
Due to the final size of the dataset, it was not possible to upload the file to GIT. The dataset can be accessed and
downloaded via this link:
https://teams.microsoft.com/l/message/19:9315df58-d9f9-4ca7-9be0-a0fb83407ae2_f6e70d41-f13c-4964-a71d-7b5681dae066@unq.gbl.spaces/1715782203185?context=%7B%22contextType%22%3A%22chat%22%7D](https://zenodo.org/records/11198572?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjZhNDNmYThkLTNlYjEtNDI2MC1iYzZiLTEyNWNiMDM3MTgzZiIsImRhdGEiOnt9LCJyYW5kb20iOiI5MTQ1ODBiYmYwZjMyZDE0OWJkZWJjZTEwZDAwMDNlNCJ9.NAtiK_yL3r3Vklb0_gtAkIrxy6kT7Lz0jMggah8KvGiYaTK1FFj8pY4cb14feFN_0oNpF0_4-ARZ0PSxBWHzKg)](https://zenodo.org/records/11198572?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjZhNDNmYThkLTNlYjEtNDI2MC1iYzZiLTEyNWNiMDM3MTgzZiIsImRhdGEiOnt9LCJyYW5kb20iOiI5MTQ1ODBiYmYwZjMyZDE0OWJkZWJjZTEwZDAwMDNlNCJ9.NAtiK_yL3r3Vklb0_gtAkIrxy6kT7Lz0jMggah8KvGiYaTK1FFj8pY4cb14feFN_0oNpF0_4-ARZ0PSxBWHzKg

The results in the thesis can be reproduced with this dataset and the models, remember to change the filepaths for 
importing the data in the notebook you want to run. Most of these notebooks are saved with a previous
run, so results, statistics, and figures can be viewed as they are now. 

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
