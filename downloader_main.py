# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:37:14 2020

@author: luhoe
"""
import os
import json
import time

from comments_downloader import downloader_main
from description_downloader import scrape_video_data
from datetime import datetime
from tqdm import tqdm

urlList = 'C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\download_urls\\video_ids_galileo_3950.txt'
output_folder = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data\\Galileo"

with open(urlList) as f:
    content = f.readlines()
content = [x.strip() for x in content]
print('start')

retry = True
retrys = 0
for video_url in tqdm(content): 
    retry = True
    retrys = 0
    while retry == True:
        try:
            argv = {}
            if video_url.split('//')[0] == 'http:'or video_url.split('//')[0] == 'https:':
                argv['youtubeid'] = video_url.split('=')[-1]
            else:
                argv['youtubeid'] = video_url
                video_url = 'https://www.youtube.com/watch?v=' + video_url
                
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
            retry = False
            
        except:
            if retrys <= 5:
                print('error in scraping ' + video_url + ' sleeping 20s and trying again')
                retry = True
                retrys = retrys +1
                time.sleep(20)
            else:
                retry = False
                print('error couldnt scrape ' + video_url)

print('everything  finished!')