# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:37:14 2020

@author: luhoe
"""
import os
import json

from comments_downloader import downloader_main
from description_downloader import scrape_video_data
from datetime import datetime
from tqdm import tqdm

urlList = 'C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\download_urls\\galileo_urls2.txt'
output_folder = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data\\Galileo"

with open(urlList) as f:
    content = f.readlines()
content = [x.strip() for x in content]

for video_url in tqdm(content):
    
    #video_url = 'https://www.youtube.com/watch?v=nXWzbsnb638'
    
    
    
    argv = {}
    argv['youtubeid'] = video_url.split('=')[-1]
    argv['output'] = output_folder
    argv['limit'] = 100000000
    
    
    # Create if directory does not exist
    if not os.path.exists(argv['output']):
        os.makedirs(argv['output'])
    
    description_dict = scrape_video_data(video_url)
    
    comments_dict = downloader_main(argv)
    
    VideoData = {}
    VideoData['description'] = description_dict
    VideoData['comments'] = comments_dict
    VideoData['size'] = len(comments_dict)
    VideoData['download_date'] = datetime.today().strftime('%Y-%m-%d')
    
    
    
    
    #save to json text file
    print('saving collected data to json file')
    with open(os.path.join(argv['output'],argv['youtubeid'] + '.json'), 'w') as fw:
    	fw.write(json.dumps(VideoData))

print('everything  finished!')