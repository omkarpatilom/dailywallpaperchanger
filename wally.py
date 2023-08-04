import os
import requests
from bs4 import BeautifulSoup

url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

response = requests.get(url)
data = response.json()

wallpaper = data["images"][0]
file_name = wallpaper["copyright"].replace("/", "-") + ".jpg"

if file_name == "wally.py":
    print("Skipping deletion of wally.py.")
elif os.path.exists(file_name):
    print(f"{file_name} already exists, no need to download.")
else:
    url = "https://www.bing.com" + wallpaper["url"]
    response = requests.get(url)
    open(file_name, "wb").write(response.content)
    print(f"{file_name} downloaded!")
    # delete oldest wallpaper, except for wally.py
    list_of_files = os.listdir()
    list_of_files.sort(key=lambda x: os.path.getmtime(x))
    oldest_file = list_of_files[0]
    if oldest_file == "wally.py":
        next_oldest_file = list_of_files[1]
        os.remove(next_oldest_file)
        print(f"{next_oldest_file} is removed!")
    else:
        os.remove(oldest_file)
        print(f"{oldest_file} is removed!")
