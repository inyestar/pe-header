import requests
from bs4 import BeautifulSoup

res = requests.get(url='https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html')
soup = BeautifulSoup(res.text, "lxml")
alist = soup.find_all('a')
downloadlink = None
for a in alist:
    if a['href'].endswith('exe'):
        downloadlink = a['href']
        break

