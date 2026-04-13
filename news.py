import subprocess
import sys

# Auto-install packages if missing
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import requests
except ImportError:
    install("requests")
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    install("beautifulsoup4")
    from bs4 import BeautifulSoup

# News website URL
URL = "https://news.ycombinator.com/"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("span", class_="titleline")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, start=1):
            file.write(f"{i}. {headline.get_text(strip=True)}\n")

    print("Headlines saved to headlines.txt")

else:
    print("Failed to fetch website")
