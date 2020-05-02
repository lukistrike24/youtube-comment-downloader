# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:20:34 2020

@author: luhoe
"""
import json
from collections import Counter

video_url = 'https://www.youtube.com/watch?v=IvGBZaprpWE'
data_folder = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data"

ID =  video_url.split('=')[-1]

f = open(data_folder + '\\' + ID + '.json')
data = json.load(f)

comments = data['comments']

def getAuthors(comments):
    Authors = []
    for comment in comments:
        Authors.append(comments[comment]['author'])    
    return Authors
    
Authors = getAuthors(comments)
c = Counter(Authors)
most_common_Authors =  c.most_common(50)