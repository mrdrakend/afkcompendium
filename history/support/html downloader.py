#CREATE A SCRIPT TO DOWNLOAD HTML FROM A WEBSITE AND SAVE IT TO A TXT FILE

import requests
import os

# Set the script directory as the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# list the files in the current working directory without the extension
files = [os.path.splitext(f)[0] for f in os.listdir('.') if os.path.isfile(f)]
print(files)

domain = 'https://afk-arena.fandom.com/wiki/'

# Create urls parsing the domain and the files list
urls = [domain + f for f in files]
print(urls)

# Download the html from the urls and save it to a txt file inside folder text. cREATE THE FOLDER IF IT DOES NOT EXIST. USE UTF-8 ENCODING
for url in urls:
    r = requests.get(url)
    if not os.path.exists('text'):
        os.makedirs('text')
    with open('text/' + os.path.splitext(os.path.basename(url))[0] + '.txt', 'w', encoding='utf-8') as f:
        f.write(r.text)        






