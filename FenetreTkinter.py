# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 14:49:02 2021

@author: USER
"""

from tkinter import * #depuis le module tkinter importer toutes les fonctions  

import mysql.connector
# importer le module de connexion à la base de donnée mysql

fenetre = Tk() # Création de la fenêtre 
fenetre.title("La Premiere page de python tkinter+mysql") # 
#le nom de la fenetre
fenetre.geometry("840x800") #la taille(longueur et largeur) de la fenêtre
#Toutes les insctructions doivent d'etre ecrit ici



# Déclaration de mes labels et entrées
def afficher():
    global entreePrenom
    global entreeNom
    global entreeMatricule
    global entreeMatiere
    global entreeNote
    labelUn = Label (fenetre, text="votre prénom :")
    labelUn.grid (row = 1,column = 1, sticky = "E", padx = 10)
    entreePrenom = Entry (fenetre)
    entreePrenom.grid (row = 1, column = 2)
    labelDeux = Label (fenetre, text="votre nom :")
    labelDeux.grid (row = 2, column = 1, sticky = "E", padx = 10)
    entreeNom = Entry (fenetre)
    entreeNom.grid (row = 2, column = 2)
    labelTrois = Label (fenetre, text="votre matricule:")
    labelTrois.grid (row = 3,column = 1, sticky = "E", padx = 10) 
    entreeMatricule = Entry (fenetre)
    entreeMatricule.grid (row = 3, column = 2)
    
    labelQuatre = Label (fenetre, text="Donnez une matiere:")
    labelQuatre.grid (row = 4,column = 1, sticky = "E", padx = 10)
    entreeMatiere = Entry (fenetre)
    entreeMatiere.grid (row = 4, column = 2)
    labelCinq = Label (fenetre, text="Donnez une note SVP:")
    labelCinq.grid (row = 5,column = 1, sticky = "E", padx = 10)
    entreeNote = Entry (fenetre)
    entreeNote.grid (row = 5, column = 2)

def ajouter () :
    #essayer de e connecter à la base de donnée 
    conn=mysql.connector.connect(host="localhost", user="root", password="user123", database="tkinterdb")
    # On verifie si la connexion s'est etablie
    if conn.is_connected() :
        print("Connexion établie avec succes !")
    # Creation d'un objet curseur afin de pouvoir envoyer des 
    #requetes et transactions
    entreePrenom.get()
    entreeNom.get()
    entreeMatricule.get()
    entreeMatiere.get()
    entreeNote.get()
    req = "INSERT INTO etudiant (nom, prenom, matricule, matiere, note) VALUES (%s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    
    cursor.execute(req, (entreePrenom.get(), entreeNom.get(), entreeMatricule.get(), entreeMatiere.get(), entreeNote.get()) )
    conn.commit() 
    # fermeture connexion
    conn.close()


def selectionner():
    #entrer trois c'est le matricule de l'etudiant
    if(entreeMatricule.get() == ""):
        MessageBox.showinfo("afficher les champs")
    else: 
        conn = mysql.connector.connect(host="localhost", user="root", 
        password="user123", database = "tkinterdb") 
        cursor = conn.cursor()
        cursor.execute("select *from etudiant where matricule = '"+ 
        entreeMatricule.get() +"'")
        rows = cursor.fetchall()
    for row in rows: 
        entreePrenom.insert(0, row[1])
        entreeNom.insert(0, row[2])
        entreeMatricule.insert(0, row[3])
        entreeMatiere.insert(0, row[4])
        entreeNote.insert(0, row[5])
    conn.close()


def Mettre_à_Jour():
    nom = entreePrenom.get()
    prenom = entreeNom.get()
    matricule = entreeMatricule.get()
    matiere = entreeMatiere.get()
    note = entreeNote.get()
    if(nom=="" or prenom=="" or matricule=="" or matiere=="" or 
    note==""):
        MessageBox.showinfo("tous les champs sont obligatoires")
    else: 
        conn= mysql.connector.connect(host="localhost", user="root", 
        password="user123", database = "tkinterdb") 
        cursor = conn.cursor()
        cursor.execute("update etudiant set nom='"+ nom +"',prenom='"+
        prenom +"', matiere='"+ matiere +"',note='"+ note +"' where matricule ='"+ 
        matricule +"'")
        cursor.execute("commit")
        #c'est-à-dire après avoir que l'étudiant remplit les champs et valider, ils seront automatiques vider les champs.
        entreePrenom.delete(0, 'end')
        entreeNom.delete(0, 'end')
        entreeMatricule.delete(0, 'end')
        entreeMatiere.delete(0, 'end')
        entreeNote.delete(0, 'end')
    conn.close()


def Supprimer():
    entreeMatricule.get() == ""
    conn = mysql.connector.connect(host="localhost", user="root", 
    password="user123", database = "tkinterdb") 
    cursor = conn.cursor()
    cursor.execute("delete from etudiant where matricule = '"+ 
    entreeMatricule.get() +"'")
    cursor.execute("commit")
    conn.close()

def Montrer():
    conn= mysql.connector.connect(host="localhost", user="root", 
    password="user123", database = "tkinterdb") 
    cursor = conn.cursor()
    cursor.execute("select *from etudiant")
    rows = cursor.fetchall()
    for row in rows: 
        insererdonnee = str(row[0])+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]+' '+row[5]
        liste.insert(liste.size()+1, insererdonnee)
    conn.close()




boutonAjouter = Button (fenetre, text='Ajouter', bg="dark green", 
command=ajouter)
boutonAjouter.place(x=30, y=200)
boutonSelectionner = Button (fenetre, text=' Selectionner ', bg="blue", 
command=selectionner)
boutonSelectionner.place(x=100, y=200)
boutonmisajour = Button (fenetre, text=' Mettre_à_Jour', bg="yellow", 
command=Mettre_à_Jour)
boutonmisajour.place(x=200, y=200)
boutonsupprimer = Button (fenetre, text='Supprimer', bg="red", 
command=Supprimer)
boutonsupprimer.place(x=300, y=200)
boutonReinitialiser = Button (fenetre, text=' Reinitialiser ', bg="dark green", 
command=ajouter)
boutonReinitialiser.place(x=390, y=200)


menubar = Menu(fenetre)


menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="ajouter un etudiant", command=afficher)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)


menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="lister un etudiant", command=afficher)
menu2.add_separator()
menu2.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Selectionner", menu=menu2)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="modifer les entrées d'un etudiant", command=afficher)
menu3.add_separator()
menu3.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Mettre_à_Jour", menu=menu3)


menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="supprimer un etudiant", command=afficher)
menu4.add_separator()
menu4.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Supprimer", menu=menu4)

menu5 = Menu(menubar, tearoff=0)
menu5.add_command(label="Afficher les etudiants", command=Montrer)
menu5.add_separator()
menu5.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Afficher", menu=menu5)


liste = Listbox(fenetre)
liste.place(x=640, y=132)
#le cannevas  (160x170)
cannevasImg = Canvas (fenetre, width =160, height = 170)

fenetre.config(menu=menubar) # la fin de fenetre
fenetre.mainloop()