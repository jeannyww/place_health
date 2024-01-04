import requests
import os
from selenium import webdriver
from bs4 import BeautifulSoup

# Getting the html of the page 
browser=webdriver.Firefox()
url = "https://empowerprogram.hhs.gov/about-empowermap.html"
browser.get(url)
sitehtml=browser.page_source
browser.quit()
soup=BeautifulSoup(sitehtml, features="html.parser")
soup.title.text

# Pulling site htmls 
start_of_url="https://empowerprogram.hhs.gov"
end_of_url=".xlsx"
allurls=soup.find_all("a") 
mydownloadlinks=[link["href"] for link in allurls if link["href"].endswith(end_of_url)]
len(mydownloadlinks)
print(mydownloadlinks)


# Loop through the site htmls and save the files into a folder ("out")
if not os.path.exists("out"):
    os.mkdir("out")

for link in mydownloadlinks: 
    print(link)
    full_link = start_of_url + link
    filename = full_link.split("/")[-1]
    response = requests.get(full_link)
    print(response)
    with open(os.path.join("out", filename), "wb") as f:
        f.write(response.content)
    print(filename)