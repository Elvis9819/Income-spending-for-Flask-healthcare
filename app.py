from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.survey_data
collection = db.responses

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "age": request.form.get("age"),
            "gender": request.form.get("gender"),
            "total_income": request.form.get("total_income"),
            "expenses": {
                "utilities": request.form.get("utilities"),
                "entertainment": request.form.get("entertainment"),
                "school_fees": request.form.get("school_fees"),
                "shopping": request.form.get("shopping"),
                "healthcare": request.form.get("healthcare"),
            }
        }
        collection.insert_one(data)
        return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)