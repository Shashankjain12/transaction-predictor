from flask import Flask, render_template, request
from handlers.app_handler import AppHandler
from handlers.model_handler import ModelHandler
import joblib
import os

model_path = "./models/randomforest_model.pkl"
# model_path = "/mnt/models/random_forest_model.pkl"
# Initialize Flask application
app = Flask(__name__)

# Load pre-trained Random Forest model
model_handler = None

# Render home page with upload form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #  Building Global model handler for caching model
        global model_handler
        if not model_handler:
            model_handler = ModelHandler(model_path=model_path)
        app_handler = AppHandler(model_handler)
        return app_handler.handle_post_request(request)
    else:
        return render_template("home.html", message="Upload a CSV file")


if __name__ == "__main__":
    app.run(debug=True)
