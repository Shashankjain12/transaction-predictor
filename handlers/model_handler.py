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

    def predict(self, df):
        predictions = self.model.predict(df)
        return predictions