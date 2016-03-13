import requests
from bs4 import BeautifulSoup
import random
#from urllib import request
import time

rname = raw_input("Input Name:- \n")
pages = int(raw_input("Input Max Pages:- \n"))
xname=rname.replace(" ","-")
name = xname.lower()


def di(url):
        n=random.randrange(1,500)
        fullname= name + str(n) + ".jpg"
        f = open(fullname, 'wb')
        f.write(request.urlopen(url).read())
        f.close()
try:
    def crawler(max):
        i=1;
        while i<= max:
            url = "http://www.santabanta.com/wallpapers/"+ name + "/?page=" + str(i)
            source_code = requests.get(url)
            text_code = source_code.text
            soup = BeautifulSoup(text_code,"html.parser")
            for link in soup.find_all('div','wallpapers-box-300x180-2-img'):
                x = "http://www.santabanta.com/"+ link.find('a').get('href')
                time.sleep(2)
                next_page(x)
            i=i+1
        
    def next_page(url):
        source_code = requests.get(url)
        text_code = source_code.text
        soup = BeautifulSoup(text_code,"html.parser")
        for link in soup.find_all('div','wallpaper-big-1-img width-video-new-2 lazy'):
            x = link.find('a').contents[0].get('src')
            di(x) 

except:
    print("Error")

if __name__ = '__main__':
	print("Please Wait... Downloading")
    	crawler(pages)
    	print ("Downloaded!")

    
