# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:20:34 2020

@author: luhoe
"""
import json
from collections import Counter
import pandas as pd

video_url = 'https://www.youtube.com/watch?v=IvGBZaprpWE'
data_folder = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data"

ID =  video_url.split('=')[-1]

f = open(data_folder + '\\' + ID + '.json')
data = json.load(f)
comments = data['comments']


#creating Dataframe
init_comments_df = pd.DataFrame(columns=['cid', 'author', 'text', 'time', 'votes'])
init_comments_df = pd.DataFrame(comments).T
init_comments_df = init_comments_df.reset_index(drop=True)
convert_dict = {'votes': int} 
init_comments_df = init_comments_df.astype(convert_dict) 



#seperating initiial comments and answers



# for comment in comments:
#     if '.' not in (comments[comment]['cid']): 
#         Authors.append(comments[comment]['author'])
#     else:
#         isAnswer = True



def getAuthors(comments):
    Authors = []
    for comment in comments:
        Authors.append(comments[comment]['author'])    
    return Authors
    
Authors = getAuthors(comments)
c = Counter(Authors)
most_common_Authors =  c.most_common(50)