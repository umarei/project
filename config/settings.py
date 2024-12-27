### settings.py

# Selenium Configuration
SELENIUM_DRIVER_PATH = "chromedriver"  # Path to your ChromeDriver executable
SELENIUM_WAIT_TIME = 10  # Default wait time for Selenium actions (in seconds)

# ProxyMesh Configuration
PROXYMESH_URL = "http://your-proxymesh-url:port"  # Replace with your ProxyMesh URL

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"  # Local MongoDB connection string
DB_NAME = "twitter_trends"  # Database name
COLLECTION_NAME = "trends"  # Collection name for storing trends

# Logging Configuration
LOG_FILE_PATH = "logs/error.log"  # Path to the log file for error tracking

# Flask Configuration
FLASK_DEBUG = True  # Set to False in production
