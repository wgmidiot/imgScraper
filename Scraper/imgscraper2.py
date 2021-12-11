import requests
from bs4 import BeautifulSoup
from requests.models import MissingSchema
#import pip to install bs4. Requests comes with Python

page = requests.get('https://howrare.is/boryokudragonz/?&sort_by=rank')
souped = BeautifulSoup(page.content, 'html.parser')
imgs = souped.find_all('img')
print(imgs[3:-6])
#Prints from image #3 up until the 6th to last to avoid logos

for img in imgs:
    imgLink = img.attrs.get('src')
    try:
        image = requests.get(imgLink).content
        fileName = 'Images/' + imgLink[imgLink.rfind('/'):] + '.png'
        with open(fileName, 'wb') as file:
            file.write(image)
    except MissingSchema:
            print('error')


