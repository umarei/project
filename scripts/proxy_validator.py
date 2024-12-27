import requests

def validate_proxy(proxy_url):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
        if response.status_code == 200:
            return response.json()["origin"]
        else:
            raise Exception("Proxy validation failed")
    except Exception as e:
        print(f"Proxy validation error: {e}")
        return None
