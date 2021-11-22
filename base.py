# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 14:37:39 2021

@author: USER
"""

#création d'une base de donnée avec python, mais avant d'importer le 
#module, installer le module mysql.connector avec la commande "###apt-get 
#install mysql.connector###"


import mysql.connector # l'importation du module
mydb = mysql.connector.connect( #cette variable permet d'appliquer lemodule
host="localhost", # l'adresse de la machine de base de donnée
user="root", # le nom l'utilisateur de la base de donnée 
password="user123" # le mot de passe de l'utilisateur de la base de donnée
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE tkinterdb") # cette fonction exécute 
#permet de créer la base sur le serveur
