### test_proxy_validator.py
import unittest
from scripts.proxy_validator import validate_proxy
from unittest.mock import patch

class TestProxyValidator(unittest.TestCase):
    def test_validate_proxy_success(self):
        proxy_url = "http://mocked.proxy:8080"

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"origin": "123.123.123.123"}

            ip = validate_proxy(proxy_url)
            self.assertEqual(ip, "123.123.123.123")

    def test_validate_proxy_failure(self):
        proxy_url = "http://mocked.proxy:8080"

        with patch('requests.get') as mock_get:
            mock_get.side_effect = Exception("Proxy validation error")
            ip = validate_proxy(proxy_url)
            self.assertIsNone(ip)

if __name__ == '__main__':
    unittest.main()
