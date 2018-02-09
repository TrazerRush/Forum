#!/usr/bin/env python
# -*- coding: utf-8 -

from flask import Flask
from flask import render_template, request, redirect, url_for
from datetime import datetime

# Importe la base de données et les fonctions
from utils import *


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

### Forum 

@app.route('/add', methods=['GET'])
def faire_addition():
    return "%s" % addition(1, 2)

@app.route('/forum', methods=['GET'])
def forum():
  sujets = select_database()
  
  nombre_sujet = count_database() # ???
  
  dernier_sujet_date = dernier_sujet_database()
  
  auteur_actif = auteur_actif_database()

  return render_template('forum.html', sujets=sujets, nombre_sujet=nombre_sujet, dernier_sujet_date=dernier_sujet_date, auteur_actif=auteur_actif)

@app.route('/formulaire', methods=['GET'])
def formulaire():
  return render_template('formulaire.html')

@app.route('/traitement', methods=['POST'])
def traitement():
    auteur = request.form['auteur']
    sujet = request.form['sujet']
    date_sujet = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formulaire_auteur_database(
        sujet=sujet, 
        auteur=auteur, 
        date_sujet=date_sujet)

    return  redirect(url_for('forum'))

@app.route('/suppression', methods=['POST'])
def suppression():
    id_suppression = request.form['id']
    suppression_database(id_suppression)

    return redirect(url_for('forum'))

if __name__ == "__main__":
    app.run()
