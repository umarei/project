### test_frontend.py
import unittest
from main import app
from main import app
from unittest.mock import patch
class TestFrontend(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Twitter Trending Topics', response.data)

    def test_scrape_trends_endpoint(self):
        with patch('scripts.selenium_scraper.scrape_trending_topics') as mock_scrape:
            mock_scrape.return_value = (["Trend 1", "Trend 2"], "123.123.123.123")

            response = self.app.get('/scrape-trends')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Trend 1', response.data)
            self.assertIn(b'123.123.123.123', response.data)

if __name__ == '__main__':
    unittest.main()
