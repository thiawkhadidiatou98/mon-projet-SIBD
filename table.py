# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 14:45:43 2021

@author: USER
"""

import mysql.connector # cette ligne permet d'importer le module
matable = mysql.connector.connect( # cette variable utilise le module 
#pour se connecter à la base
host="localhost",
user="root",
password="user123",
database="tkinterdb"
)
mycursor = matable.cursor()
mycursor.execute("CREATE TABLE etudiant (id INT AUTO_INCREMENT PRIMARY KEY, nom varchar(30), prenom varchar(30), matricule varchar(12), matiere varchar(50), note varchar(10))") #cette ligne permet de créer la table avec ses champs
