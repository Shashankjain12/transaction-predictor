from flask import render_template

class AppHandler:
    def __init__(self, model_handler):
        self.model_handler = model_handler

    def handle_post_request(self, request):
        if "file" not in request.files:
            return self.render_home_page_with_message("No file uploaded")

        file = request.files["file"]

        if file.filename == "":
            return self.render_home_page_with_message("No file selected")

        try:
            df = self.model_handler.load_file(file)
            id_codes = df["ID_code"].tolist()
            df = self.model_handler.preprocess(df)
            predictions = self.model_handler.predict(df)
            predictions = predictions.tolist()
            return render_template("result.html", predictions=predictions, codes=id_codes)
        except ValueError as e:
            return self.render_home_page_with_message(str(e))

    def render_home_page_with_message(self, message):
        return render_template("home.html", message=message)
