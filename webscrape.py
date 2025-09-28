# Libraries
import requests
from pprint import pprint

# Initialization of website url and header
subreddit = 'malaysia'
url = f'https://www.reddit.com/r/{subreddit}.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Variables to track number of posts and pages collected and set number of pages to scrape
posts = 0
page = 0
num_of_pages = 10

# Iterate through pages of posts in the subreddit
while page < num_of_pages :
    
    # Make a request to the reddit page and collect the response
    response = requests.get(url, headers = headers)
    
    if response.ok: 
        data = response.json()['data']
        
        # Collect data to be able move to the next page of posts
        nextpage = data['after']
        
        # Iterate through each post data
        for post in data['children']:
            
            # Collect various data from each post
            pdata = post['data']
            title = pdata['title']
            thumbnail = pdata.get('thumbnail')
            ptype = pdata.get('post_hint')
        
            # Filter pages of type image and display data on them
            if ptype == 'image':
                print(f'title: {title}')
                print(f'picture: {thumbnail}')
                print(f'post type :{ptype}')
                print('--------------------------')
            
            posts =+1
        
        # Display number of posts scraped for test purposes
        print(f'total posts: {posts}')
    
    # Display error message to show faults
    else: 
        print(f'Error {response.status_code}')
    
    # Update url to enter the next page of posts
    url = f'https://www.reddit.com/r/{subreddit}.json?after={nextpage}'
    
    # Increment page number
    page +=1
