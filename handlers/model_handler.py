import pandas as pd
import joblib

class ModelHandler:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
    
    def load_file(self, file):
        if not file.filename.endswith(".csv"):
            raise ValueError("File must be in CSV format")
        df = pd.read_csv(file)
        return df

    def preprocess(self, df):
        # Perform preprocessing steps if needed
        df.drop(columns=["ID_code"], inplace=True, errors='ignore')
        return df

    def fetch_data(self):
        """
        Fetching the data from the warehouse
        """
        pass

    def preprocess_training_data(self, new_data):
        """
        Steps include
        1. Imputing
        2. Oversampling
        3. Removing the outliers
        """
        pass
    
    def train_model(self, preprocessed_data):
        """
        Steps include:
        1. Adding Randomforest as been currently used
        2. Fitting the model
        """
        pass

    def evaluate_model(self, trained_model, preprocessed_data):
        """
        This involves identifying the metrics to evaluate the model
        Then comparing our current model with retrained model
        """
        pass

    def save_model(self, trained_model):
        """
        If retrained model is better compared to older model then keep it
        else discard the model
        """
        pass

    # Define a function to trigger continuous training
    def continuous_training(self):
        # Fetch new data
        new_data = self.fetch_data()

        # Preprocess the new data
        preprocessed_data = self.preprocess_training_data(new_data)

        # Train the model using the updated dataset
        trained_model = self.train_model(preprocessed_data)

        # Evaluate the model performance
        evaluation_metrics = self.evaluate_model(trained_model, preprocessed_data)

        # Save the trained model to disk
        self.save_model(trained_model)

        return evaluation_metrics

    # Periodically trigger continuous training
    def predict(self, df):
        predictions = self.model.predict(df)
        return predictions