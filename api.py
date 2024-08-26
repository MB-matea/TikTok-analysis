import requests
import json
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
from helpers import process_results

# TikTok API authentication URLs and client credentials
TOKEN_URL = 'https://open.tiktokapis.com/v2/oauth/token/'
API_URL = 'https://open.tiktokapis.com/v2/research/video/query/'
CLIENT_KEY = '' # Your TikTok client key
CLIENT_SECRET = ''  # Your TikTok client secret

## Prepare the request headers for authentication
headers = {'content-type': 'application/x-www-form-urlencoded'}
data = {
        'client_key': CLIENT_KEY,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

# Send a POST request to the TOKEN_URL to retrieve an access token
response = requests.post(TOKEN_URL, data=data, headers=headers)
token = response.json()['access_token'] # Extract the access token from the response

def get_date_strings():
    # Get today's date
    end_date = datetime.now()
    # Get the date 30 days ago
    start_date = end_date - timedelta(days=30)
    # Format dates as 'YYYYMMDD'
    return start_date.strftime('%Y%m%d'), end_date.strftime('%Y%m%d')


######### HASHTAG SEARCH QUERY #######
def get_data(hashtag):
    # Define the URL for querying video data on TikTok
    url = 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names,voice_to_text,favorites_count'
    # Prepare the request headers with the authorization token
    headers = {'authorization': 'bearer ' + token, 'content-type': 'application/json;charset=UTF-8'}
    
    # Get the start and end date strings for the query
    start_date_str, end_date_str = get_date_strings()

    # Define the data for the POST request, including the search query, date range, and result count
    data = {
        "query": {
            "and": [
                {
                    "operation": "EQ",
                    "field_name": "hashtag_name",
                    "field_values": [hashtag]
                }
            ],
        },
        "max_count": 100,   # Maximum number of results to return
        "start_date": start_date_str,   # Start date for the data query
        "end_date": end_date_str    # End date for the data query
    }

    # Send the POST request to the TikTok API
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Raise an error if the request failed

    # Process the response data using the helper function
    flattened_data = process_results(response.json())

    # Convert the processed data into a Pandas DataFrame
    df = pd.DataFrame.from_dict(flattened_data, orient = 'index')
    # Save the DataFrame to a CSV file
    df.to_csv('tiktokdata.csv', index = False)
