from flaskApp.models.Odgovor import OdgovorModel
from flaskApp.models.Poruka import PorukaModel
from email.message import EmailMessage
import ssl,smtplib

class Odgovor():
    @classmethod
    def dodajOdgovor(cls,data):
        try:
            odgovor=OdgovorModel(data['sadrzaj'],data['za'],data['naslov'],data['poruka'])
            Odgovor.posaljiMail(data)
            odgovor.add()
            return 'Uspesno unosenje odgovora u bazu'
        except:
            return 'Neuspesno unosenje odgovora u bazu'

    @classmethod
    def posaljiMail(cls,data):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "steficefi97@gmail.com"
        password = "Ljubovija2018"
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            msg = EmailMessage()
            msg.set_content(data['sadrzaj'])
            msg['subject'] = data['naslov']
            msg['From'] = sender_email
            msg['To'] = data['za']
            server.send_message(msg)
        except Exception as e:
            raise Exception('Nije moguce poslati poruku')
        finally:
            server.quit()
    
    @classmethod
    def vratiPoslate(cls):
        try:
            lista=OdgovorModel.find_all()
            result=[]
            for i in lista:
                poslata=i.json()
                porukaID=poslata['poruka']
                if porukaID!=None:
                    poruka=PorukaModel.find_for_id(porukaID)
                    poslata['poruka']=poruka.json()
                result.append(poslata)
            result.sort(key = lambda c: c['datum'],reverse=True)
            return result
        except:
            return 'Problem prilikom citanja podataka iz baze!'
            