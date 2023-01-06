import requests
import os
import data
from data import heroes_dict
import urllib.request
import urllib.parse
import urllib.error
import re

# Open 'text' folder
os.chdir('text')

# Loop through all the files in the folder an extract text from line 26 of each file using utf-8 encoding
#    for file in os.listdir():
#        with open(file, 'r', encoding='utf-8') as f:
#            lines = f.readlines()
#            text = lines[25]
#            # From text, extract content between 'content="' mark and the '.png' string
#            png = re.findall('content="(.+?)/rev', text)
#            # Loop through the list of pngs and download them to PNG folder
#            for i in png:
#               # Create 'PNG' folder if it doesn't exist
#                if not os.path.exists('PNG'):
#                    os.makedirs('PNG')
#                # Open 'PNG' folder
#                os.chdir('PNG')
#               # Download pngs to 'PNG' folder
#                urllib.request.urlretrieve(i, os.path.basename(i))
#                # Open 'text' folder
#                os.chdir('..')

# Loop through all the files in the folder and find the div class="floatleft" using utf-8 encoding
for file in os.listdir():
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # From text, extract content between 'content="' mark and the '.png' string
        wepons = re.findall('<p><a href="(.+?)/revision', str(lines))
        # Loop through the list of pngs and download them to PNG folder
        for i in wepons:
            # Create 'PNG' folder if it doesn't exist
            if not os.path.exists('PNG'):
                os.makedirs('PNG')
            # Open 'PNG' folder
            os.chdir('PNG')
            # Download pngs to 'PNG' folder
            urllib.request.urlretrieve(i, os.path.basename(i))
           # Save pngs to 'PNG' folder with the name of the file they were extracted from (excluding .html) followed by ' sigitem'
            os.rename(os.path.basename(i), file[:-9] + ' sigitem.png')
            # Open 'text' folder
            os.chdir('..')

