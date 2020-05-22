# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:04:06 2020

@author: luhoe
"""

import io
import os
import sys
import time
import re
import urllib
import json
from tqdm import tqdm

from bs4 import BeautifulSoup

with open('Youtube_API_KEY.txt', 'r') as f:
    x = f.readlines()
    API_KEY = x[0]
    
channel_ID = 'UC1XrG1M_hw8103zO2x-oivg'
output_path = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data\\Galileo"
request_url = 'https://www.googleapis.com/youtube/v3/channels?id='+ channel_ID +'&key=' + API_KEY + '&part=contentDetails'

urls = []


response = urllib.request.urlopen(request_url)
data = json.load(response)   
uploads_ID = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

request_url2 = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+ uploads_ID +'&key=' + API_KEY + '&part=snippet&maxResults=50'
response2 = urllib.request.urlopen(request_url2)
data2 = json.load(response2)   
nextPageToken =data2['nextPageToken']
for item in data2['items']:
    urls.append(item['snippet']['resourceId']['videoId'])

for i in tqdm(range(3)):
    try:
        request_url_next = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+ uploads_ID +'&key=' + API_KEY + '&part=snippet&pageToken=' + nextPageToken + '&maxResults=50'
        response_next = urllib.request.urlopen(request_url_next)
        data_next = json.load(response_next)   
        nextPageToken = data_next['nextPageToken']
        for item in data_next['items']:
            urls.append(item['snippet']['resourceId']['videoId'])
    except:
        break
print('Finished')

#save to file 
with open(output_path + '\\' + 'video_ids.txt', 'w') as f:
    for item in urls:
        f.write("%s\n" % item)