 # Image Scraper
#### About this project:
This is a project by me(Ravjot Sachdev). This is a simple python program that downloads images and gifs(based on file extension) from a website given by the user, and separates these images into distinct folders. PNGs, JPGs, and JPEGs are downloaded to an images folders, while MP4s are downlaoded to a gifs folder. To check out the source code, look at the image_scraper.py file. To run the executable file, download the executable (created using pyinstaller) from the dist folder.

#### Why this project:
This is just a project for me to get familiar with Python and various tools such as Beautiful Soup.

#### About the code:
The images are obtained using Beautiful Soup and selenium's web driver. The UI is created using TKinter to get user input.

#### ToDo List:
* Validate websites and notify user if the website is invalid
* Add an image(screenshot) to this README
* Improve UI? (With colors perhaps?)
* Expand files obtained (add DOCs, PDFs, WEBPs, etc)
* Allow users to choose what types of files are downloaded (Checkboxes to determine? ONLY do this after expanding files obtained)