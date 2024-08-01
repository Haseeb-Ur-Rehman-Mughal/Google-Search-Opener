import pandas as pd
import webbrowser
import time

# Function to construct and open Google search URL
def open_google_search(query, site):
    search_url = f"https://www.google.com/search?q={site}+{query}"
    print(f"Opening URL: {search_url}")
    webbrowser.open_new_tab(search_url)

# Read the queries and websites from the CSV file
df = pd.read_csv('queries_websites.csv')

# Loop through each query and site, and open the search URL in a new tab
for index, row in df.iterrows():
    query = row['query']
    site = row['website']
    print(f"Searching for '{query}' on {site}")
    open_google_search(query, site)
    # Add a small delay to ensure browser handles new tab openings smoothly
    time.sleep(2)