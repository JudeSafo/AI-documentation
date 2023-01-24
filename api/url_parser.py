import argparse
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

# Define the function to recursively search pages
def recursive_search(url, depth):
    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML of the website
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text from the website
    text = soup.get_text()

    # Print the text
    print(text)

    # Limit the recursion depth
    if depth > 2:
        return

    # Recursively search the website's pages
    for link in soup.find_all("a"):
        link_url = link.get("href")
        if link_url.startswith("http"):
            parsed_link = urlparse(link_url)
            parsed_original = urlparse(url)
            if parsed_link.netloc == parsed_original.netloc:
                recursive_search(link_url, depth + 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively search pages")
    parser.add_argument("url", help="The URL to start the search from")
    args = parser.parse_args()
    recursive_search(args.url, 0)

