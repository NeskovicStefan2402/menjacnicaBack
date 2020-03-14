from flask import Flask,jsonify,request
from flaskApp import app,db
from flaskApp.resources.valuta import Valuta
from flaskApp.resources.Poruka import Poruka
from flaskApp.resources.Odgovor import Odgovor
from flaskApp.others.vesti import Vesti

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/getKurs')
def getKurs():
    return jsonify({'Kurs':Valuta.vratiDnevniKurs()})

@app.route('/postKurs',methods=['POST'])
def postKurs():
    data=request.get_json()
    return jsonify({'Poruka':Valuta.dodajDnevniKurs(data)})

@app.route('/addValuta',methods=['POST'])
def addValuta():
    data=request.get_json()
    return jsonify({'Poruka':Valuta.dodajValutu(data)})

@app.route('/postMessage',methods=['POST'])
def postMessage():
    message=request.get_json()
    return jsonify({'Poruka':Poruka.primiPoruku(message)})

@app.route('/deleteValuta',methods=['DELETE'])
def deleteValuta():
    data=request.get_json()
    return jsonify({'Poruka':Valuta.obrisiValutu(data)})

@app.route('/getAllKurs')
def getAllKurs():
    return jsonify({'Istorija':Valuta.getAllKurs()})

@app.route('/getUniqueKurs')
def getUniqueKurs():
    return jsonify({'Kurs':Valuta.getUniqueKurs()})

@app.route('/getPoruke')
def getPoruke():
    return jsonify({'Poruke':Poruka.getPoruke()})

@app.route('/postOdgovor',methods=['POST'])
def postOdgovor():
    data=request.get_json()
    return jsonify({'Poruka':Odgovor.dodajOdgovor(data)})

@app.route('/getPoslate')
def getPoslate():
    return jsonify({'Poslate':Odgovor.vratiPoslate()})

@app.route('/getLast10days')
def last30():
    return jsonify({'Istorija':Valuta.getLast10Days()})

@app.route('/getNews')
def vratiVesti():
    return jsonify({'Vesti':Vesti.vratiSveNaslove()})