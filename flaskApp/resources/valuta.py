from flaskApp.models.valuta import ValutaModel
import sys
from datetime import date, timedelta
class Valuta():

    @classmethod
    def vratiDnevniKurs(cls):
        lista=Valuta.getValute()
        result=[]
        for i in lista:
            result.append(Valuta.vratiPoslednjuIzmenu(i))
        return result
    
    @classmethod
    def dodajDnevniKurs(cls,data):
        try:    
            for i in data['Kurs']:
                valuta=ValutaModel(i['naziv'],i['skracenica'],i['kupovni'],i['srednji'],i['prodajni'],date.today())
                value=ValutaModel.find_for_date(date.today(),i['skracenica'])
                if value:
                    valuta.update(i['skracenica'],date.today())
                else:    
                    valuta.add()
            return 'Uspesno je izvrsen unos'    
        except Exception:
            return'Greska prilikom unosa podataka u bazu!'
    
    @classmethod
    def dodajValutu(cls,i):
        valuta=ValutaModel(i['naziv'],i['skracenica'],i['kupovni'],i['srednji'],i['prodajni'],date.today())
        try:
            if ValutaModel.find_for_skracenica(i['skracenica']).first():
                return 'Nije moguce uneti vec postojecu vaalutu!'
            valuta.add()
            return 'Uspesno unet podataka u bazu!'
        except:
            return 'Neuspesno unosenje podatka u bazu!'
        
    @classmethod
    def obrisiValutu(cls,data):
        try:
            valute=ValutaModel.find_for_skracenica(data['skracenica'])
            for i in valute:
                i.delete()
            return 'Uspesno brisanje valute!'    
        except:
            return 'Neuspesno brisanje valute!'
        
    @classmethod
    def vratiPoslednjuIzmenu(cls,skracenica):
        lista=ValutaModel.find_for_skracenica(skracenica)
        result=[]
        for i in lista:
            result.append(i.json())
        result.sort(key = lambda c: c['datum'])
        return result[-1]
    
    @classmethod
    def getAllKurs(cls):
        lista=ValutaModel.find_all()
        result=[]
        for i in lista:
            result.append(i.json())
        return result

    @classmethod
    def getValute(cls):
        lista=ValutaModel.find_all()
        uniqueLista=[]
        for i in lista:
            if i.json()['skracenica'] not in uniqueLista:
                uniqueLista.append(i.json()['skracenica'])
        return uniqueLista
    
    @classmethod
    def vrati10zaSkracenicu(cls,skracenica):
        lista=ValutaModel.find_for_skracenica(skracenica)
        result=[]
        for i in lista:
            if(i.json()['datum']>=date.today()-timedelta(days=10)):
                result.append(i.json())
        return result

    @classmethod
    def getLast10Days(cls):
        lista=Valuta.getValute()
        result=[]
        for i in lista:
            dir={}
            dir['skracenica']=i
            dir['istorija']=Valuta.vrati10zaSkracenicu(i)
            result.append(dir)
        return result