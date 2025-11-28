from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from tabulate import tabulate

def scrape_olx_playwright():
    url = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

    with sync_playwright() as p:
      try:
        browser = p.firefox.launch(headless=True) 
        page = browser.new_page()

        print(f"Navigating to {url}...")
        page.goto(url, timeout=60000) # 60 second timeout

        print("Waiting for page to load and listings to appear...")
        page.wait_for_selector('[data-aut-id="itemBox3"]', timeout=30000)
        print("Listings found. Getting page content.")

        # Get the final HTML content after JavaScript has run
        html_content = page.content()
        browser.close()

      except Exception as e:
        print(f"\nAn error occurred with Playwright: {e}")
        print("This could be due to a network issue, a timeout, or the anti-scraping measures changing.")
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    print("Searching for listings with attribute data-aut-id='itemBox3'...")
    listings = soup.find_all(attrs={"data-aut-id": "itemBox3"})

    if not listings:
      print("\n No Listing found.")
      return

    results = []
    print(f"Found {len(listings)} listings. Extracting data...")
    for listing in listings:
      title_element = listing.find(attrs={"data-aut-id": "itemTitle"})
      price_element = listing.find(attrs={"data-aut-id": "itemPrice"})

      title = title_element.text.strip() if title_element else "N/A"
      price = price_element.text.strip() if price_element else "N/A"

      if title != "N/A" or price != "N/A":
        results.append([title, price])

    if results:
        print("\nSuccessfully extracted the following data:")
        headers = ["Title", "Price"]
        print(tabulate(results, headers=headers, tablefmt="grid"))
    else:
        print("\nFound listings, but could not extract title or price.")

if __name__ == "__main__":
    scrape_olx_playwright()
