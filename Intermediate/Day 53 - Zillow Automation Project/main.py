import scraper
import gform

try:
    def get_data():
        data = scraper.get_listings()
        print("\nListings scraped, populating sheet now...\n")
        return data
except:
    print("\nError building dictionary!\n")
try:
    data = get_data()
    if data:
        gform.populate_sheet(data)
        print("\nSheets updated!\n")
    else:
        print("\nNo data found to populate sheet..\n")
except:
    print("\nError populating sheet!\n")