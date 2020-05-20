# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:20:34 2020

@author: luhoe
"""
import json
import os
from tqdm import tqdm

# folder containing the downloaded .json files
data_folder = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data\\Galileo"


#prepare data for word2vec

min_len = 10
max_len = 300

with open(data_folder + '_summary.txt', 'a') as file:
    for filename in tqdm(os.listdir(data_folder)):
        if filename.endswith(".json"): 
            
            f = open(data_folder + '\\' + filename)
            data = json.load(f)
            comments = data['comments']

            #seperating initiial comments and answers and write comments to summary file
            for comment in comments:
                if '.' not in (comments[comment]['cid']): 
                    try:
                        if (len(comments[comment]['text']) >  min_len) and (len(comments[comment]['text']) <  max_len):
                            file.write(comments[comment]['text'] + '\n')
                    except:
                        file.write(comments[comment]['text'].encode('ascii', 'ignore').decode('ascii'))
                else:
                    isAnswer = True

            continue
        else:
            continue


