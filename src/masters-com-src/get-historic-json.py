import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():

    YEAR = 2023

    url = f"https://www.masters.com/en_US/scores/feeds/{YEAR}/scores.json"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    # Configure session with specific settings
    session = requests.Session()
    session.verify = True
    adapter = requests.adapters.HTTPAdapter(
        max_retries=3,
        pool_connections=100,
        pool_maxsize=100
    )
    session.mount('https://', adapter)

    try:
        response = session.get(
            url,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return

    data = response.json()
    with open(f"extract-{YEAR}.json", "w") as outfile:
        json.dump(data, outfile, indent=2)
    print(f"Data saved to extract-{YEAR}.json")


if __name__ == "__main__":
    main()
