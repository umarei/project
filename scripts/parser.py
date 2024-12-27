### parser.py
from bs4 import BeautifulSoup

def parse_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    trends = []
    for trend in soup.select("div[aria-label='Timeline: Trending now'] span"):
        trends.append(trend.get_text())
    return trends
