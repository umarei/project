### mongo_utils.py
from pymongo import MongoClient
import time

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "twitter_trends"
COLLECTION_NAME = "trends"

def connect_to_mongo():
    """
    Establishes a connection to the MongoDB server.
    Returns the collection object.
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        print("Connected to MongoDB successfully.")
        return collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def insert_data(data):
    """
    Inserts a document into the MongoDB collection.
    Args:
        data (dict): The data to be inserted.
    """
    collection = connect_to_mongo()
    if collection:
        try:
            collection.insert_one(data)
            print("Data inserted successfully into MongoDB.")
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")


def query_records(limit=5):
    """
    Fetches the latest records from the MongoDB collection.
    Args:
        limit (int): Number of records to fetch.
    Returns:
        list: A list of queried documents.
    """
    collection = connect_to_mongo()
    if collection:
        try:
            records = collection.find().sort("timestamp", -1).limit(limit)
            return list(records)
        except Exception as e:
            print(f"Error querying records from MongoDB: {e}")
            return []

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "trends": ["Trend1", "Trend2", "Trend3", "Trend4", "Trend5"],
        "ip_address": "192.168.1.1",
        "timestamp": time.time()
    }

    insert_data(sample_data)
    records = query_records()
    print("Queried Records:", records)