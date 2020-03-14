from flaskApp import db
import numpy as np
from datetime import date,timedelta

class ValutaModel(db.Model):
    __tablename__='kurs'
    id=db.Column(db.Integer,primary_key=True)
    datum=db.Column(db.Date)
    naziv=db.Column(db.String)
    skracenica=db.Column(db.String)
    kupovni=db.Column(db.Float)
    srednji=db.Column(db.Float)
    prodajni=db.Column(db.Float)
    

    def __init__(self,naziv,skracenica,kupovni,srednji,prodajni,datum):
        self.datum=datum
        self.naziv=naziv
        self.skracenica=skracenica
        self.kupovni=kupovni
        self.srednji=srednji
        self.prodajni=prodajni
    
    def json(self):
        return {
            'id':self.id,
            'naziv':self.naziv,
            'datum':self.datum,
            'skracenica':self.skracenica,
            'kupovni':self.kupovni,
            'srednji':self.srednji,
            'prodajni':self.prodajni
        }
    
    @classmethod
    def find_all_for_Date(cls,datum):
        return cls.query.filter_by(datum=datum)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_last_30days(cls):
        return cls.query.filter(datum<=date.today()-timedelta(days=30))

    @classmethod
    def find_for_skracenica(cls,skracenica):
        return cls.query.filter_by(skracenica=skracenica)

    @classmethod
    def find_for_date(cls,datum,skracenica):
        return cls.query.filter_by(datum=datum, skracenica=skracenica).first()
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self,skracenica,datum):
        value=ValutaModel.find_for_date(datum,skracenica)
        value.kupovni=self.kupovni
        value.srednji=self.srednji
        value.prodajni=self.prodajni
        db.session.commit()
    
    
        
