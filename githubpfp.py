import requests
import urllib.request
from bs4 import BeautifulSoup as bs 
from pathlib import Path


github = input("Github Username: ")
url = "https://github.com/" +github
r = requests.get(url)
soup = bs(r.content, 'html.parser')
pfp = soup.find("img", {"alt" : "Avatar"})["src"]
save_name = "githubpfp.png"
urllib.request.urlretrieve(pfp, save_name)

path_to_file = 'githubpfp.png'
path = Path(path_to_file)

if path.is_file():
    print(f'profile picture "{path_to_file}" downloaded')
else:
    print(f'profile picture "{path_to_file}" not downloaded')

