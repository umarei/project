# Twitter Trends Scraper

This project is a web application that scrapes trending topics from Twitter, stores them in a MongoDB database, and visualizes the data on a simple frontend using Flask and Chart.js.

---




## Features

- **Web Scraping**: Uses Selenium to log in to Twitter and scrape the top 5 trending topics.
- **Proxy Handling**: Integrates ProxyMesh to rotate IP addresses for each scraping request.
- **Data Parsing**: Leverages Beautiful Soup for cleaner trend extraction.
- **Data Storage**: Stores scraped data in a MongoDB database with fields like trends, IP address, and timestamp.
- **Frontend Display**: Displays trending topics and their associated details in a user-friendly interface.
- **Data Visualization**: Visualizes the trends using Chart.js.

---

## Project Structure

```plaintext
project/
├── config/                # Configuration files (e.g., settings.py)
├── database/              # MongoDB utilities
│   └── mongo_utils.py     # MongoDB connection, insertion, and querying
├── logs/                  # Logs for errors
│   └── error.log          # Error tracking logs
├── scripts/               # Core functionalities
│   ├── selenium_scraper.py  # Selenium-based scraping logic
│   ├── proxy_validator.py   # Proxy validation logic
│   ├── parser.py            # HTML parsing logic using Beautiful Soup
│   ├── data_exporter.py     # Logic to export data to CSV using Pandas
│   └── error_handling.py    # Common error-handling utilities
├── static/                # Static files for the frontend
│   ├── app.js              # JavaScript for frontend interactivity
│   ├── style.css           # Styling for the frontend
│   └── chart.js            # Chart visualization logic
├── templates/             # HTML templates
│   └── index.html          # Main frontend page
├── tests/                 # Test cases for the project
├── main.py                # Main application entry point
└── requirements.txt       # List of Python dependencies
```

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- MongoDB installed and running
- Google Chrome browser installed
- ChromeDriver matching your Chrome version

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/twitter-trends-scraper.git
   cd twitter-trends-scraper
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure MongoDB:
   - Ensure MongoDB is running locally or provide a connection URI in `config/settings.py`.

5. Update Twitter login credentials:
   - Open `scripts/selenium_scraper.py` and update:

     ```python
     username.send_keys("your_twitter_username")
     password.send_keys("your_twitter_password")
     ```

6. Verify ChromeDriver installation:
   - Ensure `chromedriver` is installed and matches your Chrome version.

---

## Running the Application

1. Start the Flask server:

   ```bash
   python main.py
   ```

2. Open the application in a browser:

   ```
   http://127.0.0.1:5000/
   ```

3. Click **"Fetch Trends"** to scrape data, store it in MongoDB, and view the results.

---

## Testing

Run the test cases in the `tests/` directory:

```bash
python -m unittest discover -s tests
```

---

## Features Breakdown

1. **Selenium Scraper**:
   - Logs in to Twitter to scrape the top 5 trending topics.
   - Handles dynamic content loading with explicit waits.

2. **Proxy Validator**:
   - Automates IP rotation using ProxyMesh.
   - Ensures the proxy is functional before sending requests.

3. **Data Handling**:
   - Stores scraped data in MongoDB with fields:
     - `trends`: List of trending topics.
     - `ip_address`: IP used for the request.
     - `timestamp`: Time of scraping.
   - Allows exporting data to CSV using Pandas.

4. **Frontend**:
   - Displays scraped trends and details.
   - Includes data visualization using Chart.js.

---

## Troubleshooting

1. **Error: No module named `pip`**
   - Install `pip`:

     ```bash
     python get-pip.py
     ```

2. **Error: `TemplateNotFound: index.html`**
   - Ensure `index.html` is in the `templates/` folder.

3. **Error: `chromedriver` not found**
   - Download ChromeDriver from [ChromeDriver site](https://chromedriver.chromium.org/) and ensure it matches your Chrome version.
   - Add ChromeDriver to your PATH.

4. **MongoDB connection issues**:
   - Verify MongoDB is running:

     ```bash
     mongod
     ```

   - Check connection URI in `config/settings.py`.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing

Feel free to submit issues and pull requests for improvements. Contributions are always welcome!
