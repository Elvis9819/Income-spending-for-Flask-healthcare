import csv
from pymongo import MongoClient

class User:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client.survey_data
        self.collection = self.db.responses

    def export_to_csv(self, file_path):
        data = self.collection.find()
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Age", "Gender", "Total Income", "Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"])
            for row in data:
                writer.writerow([
                    row["age"],
                    row["gender"],
                    row["total_income"],
                    row["expenses"]["utilities"],
                    row["expenses"]["entertainment"],
                    row["expenses"]["school_fees"],
                    row["expenses"]["shopping"],
                    row["expenses"]["healthcare"]
                ])