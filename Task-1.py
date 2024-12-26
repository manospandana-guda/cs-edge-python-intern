import requests
from bs4 import BeautifulSoup
import json

# Function to scrape data from the specified URL
def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the desired data
        data = {}

        # Get book title
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else None
        data['title'] = title

        # Get book price
        price = soup.find('p', class_='price_color').get_text(strip=True) if soup.find('p', class_='price_color') else None
        data['price'] = price

        # Get product description
        description = soup.find('meta', {'name': 'description'})['content'].strip() if soup.find('meta', {'name': 'description'}) else None
        data['description'] = description

        # Return the extracted data as JSON
        return json.dumps(data, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error while making HTTP request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
def main():
    # The URL of the website to scrape
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    print("Scraping data from website...")
    scraped_data = scrape_website(url)

    if scraped_data:
        print("Scraping completed. Here's the extracted data:")
        print(scraped_data)

        # Optional: Save the JSON data to a file
        with open('scraped_data.json', 'w') as file:
            file.write(scraped_data)
            print("Data saved to 'scraped_data.json'.")

if __name__ == "__main__":
    main()
