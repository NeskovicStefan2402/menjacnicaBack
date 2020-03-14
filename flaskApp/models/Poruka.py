from flaskApp import db
from datetime import datetime
class PorukaModel(db.Model):
    __tablename__='poruke'
    id=db.Column(db.Integer,primary_key=True)
    datum=db.Column(db.DateTime)
    email=db.Column(db.String)
    sadrzaj=db.Column(db.String)
    
    def __init__(self,email,sadrzaj):
        self.datum=datetime.now()
        self.email=email
        self.sadrzaj=sadrzaj
    
    def json(self):
        return {
            'id':self.id,
            'datum':self.datum,
            'email':self.email,
            'sadrzaj':self.sadrzaj
        }
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_for_id(cls,porukaID):
        return cls.query.filter_by(id=porukaID).first()

    def add(self):
        db.session.add(self)
        db.session.commit()
