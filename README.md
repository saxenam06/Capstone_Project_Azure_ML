# Capstone_Project_Azure_ML

This capstone project is the culmination of the Azure ML Engineer path. The primary objective is to develop and deploy a predictive model for stroke occurrence based on various diseases and habits recorded in the dataset. The project is structured into three main tasks:

- Train a Model with AutoML: Utilize Azure AutoML to automate the process of model selection and hyperparameter tuning.
- Train a Model with HyperDrive: Implement HyperDrive to perform hyperparameter optimization manually, ensuring a thorough search for the best model configuration.
- Deploy the Best Model: Compare the models generated from AutoML and HyperDrive, and deploy the superior model. In our case we found that Hyperdrive gave the better model 0.95 Accuracy as compared to that obtained from AutoML i.e. 0.85 AUC. 

Below are the mentioned steps in which this project was performed. 

### Dataset
https://www.kaggle.com/andrewmvd/heart-failure-clinical-data
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/7414f3c6-ff3c-421f-8b81-e4fb9291d2c1)

## AutoML

### AutoML Run details
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/d01fab6b-6493-42af-8904-748ed5d1ae54)


### AutoML Job completed
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/388df000-d65a-491b-9891-c6035a38eb84)


### AutoML Best model
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/4b5a2530-144e-475f-8c4d-c2ebec9bce1c)

![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/9d85a9cf-df2c-4db5-bb96-54636532dad9)

![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/125b7c36-b4c0-4d8c-a2d4-a515ef35f06d)

## HyperDrive

### Notebook and used files for HyperDrive
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/509a2a54-5b9e-4b41-9782-7ac2f5c1c918)

### HyperDrive Run details
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/32be52f3-a791-4940-bfb4-65248d5a63a2)

### HyperDrive Best Model
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/ca6a7a43-7d84-493a-baf3-abf498e407bc)

### HyperDrive Model Deployed as endpoint
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/4c4a38f8-a480-49c9-8e99-f6631ab012f3)

### HyperDrive Predictions
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/d073f92e-036c-42cf-8d46-3ae4cfae01d9)


### Screencast
https://www.youtube.com/watch?v=Fjs2wnb_BH4

### Service deletion
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/0fc0c292-d191-4a2e-8e09-fbd7b3112cc1)
