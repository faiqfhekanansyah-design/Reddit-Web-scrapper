# Libraries
import requests
import json
import time

# Initialization of website url and header
subreddit = 'malaysia'
url = f'https://www.reddit.com/r/{subreddit}.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Other Variable Initialization
page = 0 
num_of_pages = 10
post_data= []

# Store information information on which subreddit is scraped and when
all_data ={
    "Subreddit" :subreddit,
    "url": f"https://www.reddit.com/r/{subreddit}",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}

# Iterate through pages of posts in the subreddit
while page < num_of_pages :
    response = requests.get(url, headers = headers)
    
    if response.ok: 
        data = response.json()['data']
        
        # Collect data to be able move to the next page of posts
        nextpage = data['after']
        
        # Iterate posts and collect post type 
        for post in data['children']:
            pdata = post['data']
            ptype = pdata.get('post_hint')
        
        # Filter pages of type image and store post title and image url in a variable
            if ptype == 'image':
                post_data.append({
                "post_title" : pdata['title'],
                "image_url": pdata.get('url_overridden_by_dest'),
                })

    # Display error message to show faults
    else: 
        print(f'Error: {response.status_code}')
    
    # Update url to enter the next page of posts
    url = f'https://www.reddit.com/r/{subreddit}.json?after={nextpage}'
    
    # Increment page number
    page +=1

# Store post data with the information of the subreddit
all_data["post_data"] = post_data

# Save data into a json file

try:
    # Attempt to open .json file and replace the data if access is allowed 
    with open("Reddit_post.json","w", encoding ="utf-8") as file:
        json.dump(all_data, file, indent=2, ensure_ascii=True)
        
    # Show users the process is completed
    print("Data saved as Json: Reddit_post.json ")
    
# Display error message to show faults with file storage
except Exception as e :
    print(f'Error: {e}')

# Keep window open until the user is ready done
input("Enter to Exit ")
