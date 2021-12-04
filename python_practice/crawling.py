from urllib.request import urlopen
from bs4 import BeautifulSoup
a=urlopen("https://music.bugs.co.kr/chart")
soup=BeautifulSoup(a.read(),"html.parser")
print(soup.title)

music=soup.find_all('p','title')

i=1
for a in music:
    print("%d위: %s"%(i,a.find('a').text))
    i=i+1

