from flaskApp import db
from datetime import datetime
class OdgovorModel(db.Model):
    __tablename__='odgovori'
    id=db.Column(db.Integer,primary_key=True)
    datum=db.Column(db.DateTime)
    email=db.Column(db.String)
    primalac=db.Column(db.String)
    naslov=db.Column(db.String)
    sadrzaj=db.Column(db.String)
    poruka=db.Column(db.Integer,db.ForeignKey('poruke.id'))
    
    def __init__(self,sadrzaj,primalac,naslov,poruka):
        self.datum=datetime.now()
        self.primalac=primalac
        self.naslov=naslov
        self.email='stefan.neskovic@elab.rs'
        self.sadrzaj=sadrzaj
        self.poruka=poruka
    
    def json(self):
        return {
            'id':self.id,
            'datum':self.datum,
            'email':self.email,
            'primalac':self.primalac,
            'naslov':self.naslov,
            'sadrzaj':self.sadrzaj,
            'poruka':self.poruka
        }
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_odgovorNaPoruku(cls,porukaID):
        return cls.query.filter_by(poruka=porukaID).first()

    def add(self):
        db.session.add(self)
        db.session.commit()
