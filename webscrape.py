# Libraries
import requests
from pprint import pprint

# Initialization of website url and header
subreddit = 'malaysia'
url = f'https://www.reddit.com/r/{subreddit}.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Make a request to the reddit page and collect the response
response = requests.get(url, headers = headers)

# Check response received from the web page
if response.ok: 
    
    # Collect response and display the website data
    data = response.json()
    pprint(data)
    
# Display error message to show faults
else: 
    print(f'Error {response.status_code}')