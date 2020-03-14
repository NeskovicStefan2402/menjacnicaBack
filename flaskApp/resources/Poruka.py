from flaskApp.models.Poruka import PorukaModel
from flaskApp.models.Odgovor import OdgovorModel

class Poruka():

    @classmethod
    def primiPoruku(cls,data):
        try:
            poruka=PorukaModel(data['email'],data['sadrzaj'])
            poruka.add()
            return 'Uspesno sacuvana poruka u bazi.'
        except:
            return 'Greska prilikom cuvanja poruke u bazu.'
        
    @classmethod
    def getPoruke(cls):
        lista=PorukaModel.find_all()
        result=[]
        for i in lista:
            if OdgovorModel.find_odgovorNaPoruku(i.json()['id'])==None:
                result.append(i.json())
        result.sort(key = lambda c: c['datum'],reverse=True)
        return result