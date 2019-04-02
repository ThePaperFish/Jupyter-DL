import requests
from bs4 import BeautifulSoup4

def web(page,WebUrl):
    if(page>0):
	
        url = WebUrl
        code = requests.get(url)
        plain = code.text

        print(plain)
        
        s = BeautifulSoup(plain, "html.parser")

        index = 0


web(1,'https://www.google.com/search?q=ball&tbm=isch')
