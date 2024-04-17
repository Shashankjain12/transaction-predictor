#### Hosted github page at [Transaction Predictor Github Page](https://shashankjain12.github.io/transaction-predictor/)
# Transaction Predictor
This project is a Flask web application for deploying a machine learning model to predict Santander customer transactions.

## Overview
The web application allows users to upload a CSV file containing customer transaction data. The uploaded data is then preprocessed, fed into a pre-trained machine learning model, and predictions are made on whether a customer will make a transaction or not. The predictions are displayed to the user in a user-friendly format.


## Architecture Flow Diagram

### Prediction CI/CD Flow Diagram

![alt text](/images/prediction_model.png)

Currently implemented the flow using flask to host in model and then building a CI/CD Pipeline across it.

### Retraining flow Diagram
Pseudo code is there since model retraining required DWH Setup and the data which is being constantly generated.

![alt text](/images/retraining_model.png)


### Running WebAPP
![alt text](/images/running_webapp.png)

#### Predictions
![alt text](/images/predictions.png)


## Project Structure
The project directory structure is as follows:

```
project/
│
|── templates/
│   │   ├── home.html        # HTML template for the upload form
│   │   └── result.html      # HTML template for displaying predictions
├── models/
│   └── model.pkl            # Pre-trained machine learning model
│
├── Dockerfile               # Dockerfile for containerization
├── deployment.yaml          # Kubernetes YAML file for deployment
├── requirements.txt         # Python dependencies
├── README.md                # Project README file (you're reading it)
└── app.py                   # Python script to run the Flask application
```

#### Model Training Pipeline

During the model training phase of my project, I took several steps to train a machine learning model using the Santander Customer Transaction Prediction dataset. Here's a breakdown of what I did and the evaluation metrics I obtained:

1. Preprocessing: First, I preprocessed the data to ensure it was suitable for training. This involved handling missing values, removing outliers, and scaling or transforming features as needed.

2. Oversampling: To address class imbalance in the dataset, I employed oversampling. This technique involved increasing the number of instances in the minority class (e.g., customers who made a transaction) to balance the dataset.

3. Random Forest with 10 Estimators: For my model, I chose to use a Random Forest algorithm with 10 estimators. Random Forest is an ensemble learning method that combines multiple decision trees to make predictions. Each decision tree in the forest is trained on a subset of the data and makes predictions independently. By using 10 estimators, I created a Random Forest model consisting of 10 decision trees.

Evaluation Metrics:

1. Accuracy: My model achieved an accuracy score of 0.9063, indicating that it correctly classified about 90.63% of instances in the dataset.
2. Precision: The precision score was 0.9347, meaning that when my model predicted a positive class, it was correct approximately 93.47% of the time.
3. Recall: With a recall score of 0.8740, my model correctly identified approximately 87.40% of all actual positive instances in the dataset.
4. F1 Score: The F1 score, a balance between precision and recall, was 0.9033, indicating a good overall performance.
5. ROC AUC Score: The ROC AUC score of 0.9063 indicated that my model's ability to distinguish between positive and negative samples was relatively high.
Overall, these evaluation metrics suggest that my model is performing reasonably well in classifying customer transactions. However, I'll continue to explore ways to optimize and improve its performance further.


### Getting Started

### Prerequisites
Python 3.9

Docker (optional, for containerization)
Kubernetes (optional, for deployment)

Installation

Clone this repository to your local machine:

git clone https://github.com/shashankjain12/transaction-predictor.git

Navigate to the project directory:

Install Python dependencies:
`pip install -r requirements.txt`


### Running the Application

To run the Flask application locally, execute the following command:

`python app.py`

The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

### Deployment

You can deploy the Flask application using Docker and Kubernetes. 

Instructions for deployment can be found in the deployment.yaml file and Dockerfile.

`docker pull shashankjain/transaction-predictor-app:latest`

`docker run -p 5000:5000 shashankjain/transaction-predictor-app:latest`

## Usage

1. Access the web application in your browser.

2. Upload a CSV file containing customer transaction data.

3. Wait for the predictions to be displayed.

4. View the predictions on whether a customer will make a transaction or not.

## Tools and Frameworks used

Docker:

Reason: Docker was used for containerization to ensure that the Flask application runs consistently across different environments. By containerizing the application, it becomes portable and isolated, making it easier to deploy and manage.

Kubernetes:

Reason: Kubernetes was chosen for orchestrating and managing containerized applications in a production environment. It provides features like auto-scaling, load balancing, and rolling updates, which are essential for deploying and scaling the Flask application effectively.
Flask:

Reason: Flask was selected as the web framework for building the application that serves predictions generated by the machine learning model. Flask is lightweight, flexible, and easy to use, making it suitable for developing web applications with Python.

scikit-learn (sklearn):

Reason: scikit-learn is a popular machine learning library for Python, chosen for its comprehensive set of tools and algorithms for training and evaluating machine learning models. It provides easy-to-use interfaces and robust implementations of various algorithms, making it ideal for building the predictive model in this project.

SMOTE (Synthetic Minority Over-sampling Technique):

Reason: SMOTE was used to address class imbalance in the dataset by oversampling the minority class. Class imbalance can negatively impact the performance of machine learning models, and SMOTE helps mitigate this issue by generating synthetic samples to balance the class distribution.

Git Workflow:

Reason: A Git workflow, such as feature branching or GitFlow, was adopted for version control and collaboration purposes. It helps manage changes to the codebase, coordinate work among team members, and track the project's history effectively. Documenting the Git workflow in the README file provides clarity and guidance for team members on how to contribute to the project and follow best practices.