# Capstone_Project_Azure_ML

This capstone project is the culmination of the Azure ML Engineer path. The primary objective is to develop and deploy a predictive model for stroke occurrence based on various diseases and habits recorded in the dataset. The project is structured into three main tasks:

- Train a Model with AutoML: Utilize Azure AutoML to automate the process of model selection and hyperparameter tuning.
- Train a Model with HyperDrive: Implement HyperDrive to perform hyperparameter optimization manually, ensuring a thorough search for the best model configuration.
- Deploy the Best Model: Compare the models generated from AutoML and HyperDrive, and deploy the superior model. In our case we found that Hyperdrive gave the better model 0.95 Accuracy as compared to that obtained from AutoML i.e. 0.85 AUC. 

Below are the mentioned steps in which this project was performed. 

### Overview of Dataset

The dataset utilized for this project is the Heart Failure Clinical Dataset. It contains clinical features such as age, sex, smoking, and medical history, which are potential predictors of stroke occurrence.

#### Method Used to Get Data into Azure ML Studio Workspace

To import the dataset into Azure ML Studio workspace:
The dataset was sourced from below Kaggle link and downloaded as a CSV file.
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/7414f3c6-ff3c-421f-8b81-e4fb9291d2c1)

Azure ML Studio was used to create a Dataset in the worskpace by uploading it from local files. 

## AutoML

### AutoML Run details
AutoML Run details which details all the trials performed by AutoML and their corresponding results.
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/d01fab6b-6493-42af-8904-748ed5d1ae54)


### AutoML Job completed
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/388df000-d65a-491b-9891-c6035a38eb84)


### AutoML Best model
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/4b5a2530-144e-475f-8c4d-c2ebec9bce1c)

![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/9d85a9cf-df2c-4db5-bb96-54636532dad9)

![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/125b7c36-b4c0-4d8c-a2d4-a515ef35f06d)

### AutoML model registered
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/6fd17d22-4b83-4bce-8fb0-c1b290e5ceb4)

## HyperDrive

### Notebook and used files for HyperDrive
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/509a2a54-5b9e-4b41-9782-7ac2f5c1c918)

### HyperDrive Search details 
For the HyperDrive experiment, a RandomParameterSampling was employed with the following parameters:
C: "Inverse of regularization strength. Smaller values cause stronger regularization" with Uniform distribution between 0.1 and 1.0.
max_iter: "Maximum number of iterations to converge" with Choice between 50, 100, 150, 200, and 250.

### HyperDrive Run details
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/32be52f3-a791-4940-bfb4-65248d5a63a2)

### HyperDrive Trials
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/57a97013-18eb-461c-9228-4f68d7775fe3)

### Overview of the Best Model
THe Best model obtained from AutoML was compared with the best model obtained from HyperDrive. Below are the details.

AutoML Best Model: VotingEnsemble with an AUC_weighted of 0.85.
HyperDrive Best Model: LogisticRegression with a regularization strength of 0.997 and max iterations of 50, achieving an accuracy of 0.95.

### HyperDrive Best Model
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/ca6a7a43-7d84-493a-baf3-abf498e407bc)

### Overview of Deployed Model
The HyperDrive best model, a LogisticRegression classifier, was deployed as an endpoint. To query the endpoint for predictions, use the sample input in 'data' and below Python code snippet.
You may need to copy the the Rest url from the Deployed model endpoint
'
data = {"data": [[0, 0, 0, 0, 0, False, 0, 0, 0, 0, 0]]}
body = str.encode(json.dumps(data))

url = 'Rest url of the endpoint'
headers = {'Content-Type':'application/json'}

req = urllib.request.Request(url, body, headers)
response = urllib.request.urlopen(req)
result = response.read()
print(result)'

### HyperDrive Model Deployed as endpoint
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/4c4a38f8-a480-49c9-8e99-f6631ab012f3)

### HyperDrive Predictions
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/d073f92e-036c-42cf-8d46-3ae4cfae01d9)


### Screencast
https://www.youtube.com/watch?v=Fjs2wnb_BH4

### Service deletion
![image](https://github.com/saxenam06/Capstone_Project_Azure_ML/assets/83720464/0fc0c292-d191-4a2e-8e09-fbd7b3112cc1)


### Future work
In future iterations, the project could be enhanced by:
- Exploring advanced ensemble techniques for better model performance.
- Implementing model monitoring and retraining strategies to ensure continous imporovement in the prediction accuracy with continous change in data.
