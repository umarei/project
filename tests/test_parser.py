### test_parser.py
import unittest
from scripts.parser import parse_html

class TestParser(unittest.TestCase):
    def test_parse_html(self):
        html_content = """
        <div aria-label='Timeline: Trending now'>
            <span>Trend 1</span>
            <span>Trend 2</span>
            <span>Trend 3</span>
            <span>Trend 4</span>
            <span>Trend 5</span>
        </div>
        """
        trends = parse_html(html_content)
        self.assertEqual(trends, ["Trend 1", "Trend 2", "Trend 3", "Trend 4", "Trend 5"])

if __name__ == '__main__':
    unittest.main()
