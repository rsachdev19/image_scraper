import re
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from tkinter import *
from tkinter import filedialog

#Some sites to test
#site = 'http://heroimages.com/portfolio'
#site = 'https://imgur.com/'
#site = 'https://doogeveneers.com/browse-veneers'
#site = 'https://giphy.com/'

directory = os.getcwd() + "\\" #Set default directory to directory of script
site = "https://google.com" #Set default website

def getfile():
    global directory
    global directoryLabel
    direct = filedialog.askdirectory(initialdir=os.getcwd(), title="Select folder",) 
    directory = direct + "/"
    directoryLabel.config(text=("..." + directory[-20:])) #Shorten file path displayed
    print("Downloading to " + directory[-20:])
    
def quit():
    global site
    global root
    site = textBox.get("1.0", "end-1c")
    #@TODO: Validate site. If valid, root.destroy. Else, notify user.
    #print(site)
    root.destroy()
    
root = Tk()
root.title("Rav's Web Scrapper")
root.geometry("400x200")

frame = Frame(root)
frame.pack()
directoryFrame = Frame(root)
directoryFrame.pack()
submitframe = Frame(root)
submitframe.pack()

siteLabel = Label(frame, text="Enter Website")
siteLabel.pack(side=LEFT)

textBox=Text(frame, height = 1, width = 35)
textBox.pack(side=LEFT)

directoryLabel = Label(directoryFrame, text=("..." + directory[-20:]))
directoryLabel.pack(side=LEFT)
choose_button = Button(directoryFrame, text="Choose Folder", fg="black", command=getfile)
choose_button.pack(side=LEFT)

submit_button = Button(submitframe, text="Submit", fg="black", command=quit)
submit_button.pack(fill=X)

root.mainloop()

#sys.exit()

jpg = ".jpg"
jpeg = ".jpeg"
png = ".png"
gif = ".gif"
mp4 = ".mp4"
count = 0

def check_directory(checkDir):
    if not os.path.exists(checkDir):
        os.makedirs(checkDir)

check_directory(directory)
driver = webdriver.Chrome('C:/Python35/chromedriver')
driver.get(site)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_tags = soup.find_all('img')
video_tags = soup.find_all('video')
urls = [img['src'] for img in img_tags]
videos = [video['src'] for video in video_tags]

def clean_url(url):
    if jpg in url:
        index = url.find(jpg)
        url = url[:index+len(jpg)]
    if jpeg in url:
        index = url.find(jpeg)
        url = url[:index+len(jpeg)]
    if gif in url:
        index = url.find(png)
        url = url[:index+len(png)]
    if gif in url:
        index = url.find(gif)
        url = url[:index+len(gif)]
    return url

def download_video(url):
    subdirectory = directory + "gifs/"
    check_directory(subdirectory)
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(os.path.join(subdirectory,local_filename), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename

if len(urls) > 0:
    print("Starting download process...")
else:
    print("No files to download")
    
for url in urls:
    if jpg in url or jpeg in url or png in url or gif in url:
        url = clean_url(url)
        filename = re.search(r'/([\w_-]+[.](jpg|jpeg|png|gif))$', url)
        if jpg in url or jpeg in url or png in url:
            subdirectory = directory + "imgs/"
            check_directory(subdirectory)
        if gif in url:
            subdirectory = directory + "gifs/"
            check_directory(subdirectory)
        with open(os.path.join(subdirectory,filename.group(1)), 'wb') as f:
            if 'http' not in url:
                # sometimes an image source can be relative 
                # if it is provide the base url which also happens 
                # to be the site variable atm. 
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
            count+=1

for video in videos:
    if mp4 in video:
        count+=1
        download_video(video)

#@TODO: Option to download certain type of files only
print("Downloading completed")
print("Number of files downloaded = {}".format(count))
driver.quit() #Close the window
