from bs4 import BeautifulSoup
import urllib.request
class Vesti():
    @classmethod
    def vratiSveNaslove(cls):
        URL='https://naslovi.net/search.php?q=valuta'
        soup = BeautifulSoup(urllib.request.urlopen(URL))
        vesti=[]
        sviOdeljci=soup.find_all('div',{'class':'article'})
        for i in sviOdeljci:
            dir={}
            dir['naslov']=i.h2.text
            dir['ruta']=i.h2.a['href']
            dir['objavio']=i.find('div',{'class':'a-info'}).find('span',{'class':'a-source'}).text
            dir['vreme']=i.find('div',{'class':'a-info'}).find('span',{'class':'a-time'}).text
            vesti.append(dir)
        return vesti
