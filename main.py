# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:37:14 2020

@author: luhoe
"""
import os

from downloader import downloader_main


video_url = 'https://www.youtube.com/watch?v=nXWzbsnb638'
output_folder = "C:\\Users\\luhoe\\Documents\\Git_Projects\\Github\\youtube-comment-downloader\\Data"


argv = {}
argv['youtubeid'] = video_url.split('=')[-1]
argv['output'] = output_folder
argv['limit'] = 100


# Create if directory does not exist
if not os.path.exists(argv['output']):
    os.makedirs(argv['output'])

downloader_main(argv)