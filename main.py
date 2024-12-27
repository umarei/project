from flask import Flask, jsonify, render_template
from scripts.selenium_scraper import scrape_trending_topics
from database.mongo_utils import insert_data, query_records
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))


# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """
    Serve the HTML frontend.
    """
    return render_template('index.html')

@app.route('/scrape-trends', methods=['GET'])
def scrape_trends():
    """
    Trigger the Selenium scraper, store results in MongoDB,
    and return the scraped data as JSON.
    """
    try:
        # Call the scraping function
        trends, ip_address = scrape_trending_topics()

        # Prepare the data to be stored in MongoDB
        data = {
            "trends": trends,
            "ip_address": ip_address,
            "timestamp": time.time()
        }

        # Store data in MongoDB
        insert_data(data)

        # Return data as JSON
        return jsonify({
            "success": True,
            "trends": trends,
            "ip_address": ip_address
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/get-records', methods=['GET'])
def get_records():
    """
    Query the latest records from MongoDB and return them as JSON.
    """
    try:
        records = query_records(limit=5)
        return jsonify({"success": True, "records": records})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
