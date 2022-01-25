from multiprocessing.dummy import connection
from textwrap import fill
from tkinter import*
from modules import page
import json

def inscription(): 
    inscription = Tk()
    inscription.title("Gestion Des Patients")
    inscription.resizable(False, False)
    inscription.geometry("500x500")
    heading = Label(inscription, text="Page D'Inscription", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 16").pack(pady=30, ipadx=150, ipady=10)
    
    frame = Frame(inscription, highlightbackground="black", highlightthickness=2)
    frame.pack(padx=70, pady=(50), anchor='w')

    Nom = Label(frame, text=" Nom ",font="Roboto 15").grid(row=0, column=0, sticky=E )
    nom_entry = Entry(frame).grid(row=0, column=1, ipadx=25, ipady=5, sticky= E)
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15").grid(row=1, column=0, sticky=E)
    prenom_entry = Entry(frame).grid(row=1, column=1 ,ipadx=25, ipady=5, sticky= E) 
    Email = Label(frame, text=" Email ",font="Roboto 15").grid(row=2, column=0, sticky= E)
    email_entry = Entry(frame).grid(row=2, column=1, ipadx=25, ipady=5, sticky=E )
    
        
    btn = Button(frame, text="S'Inscrire", width=10, height=2, font="Roboto 15").grid(row=3, columnspan=2, sticky="N")
    
    inscription.mainloop()

def connexion():      
    connexion = Tk()
    connexion.title("Gestion Des Patients")
    connexion.resizable(False, False)
    connexion.geometry("500x500")
    heading1 = Label(connexion, text="Page de Connexion", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 15").pack(pady=30, ipadx=150, ipady=10)
    
    frame = Frame(connexion, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)

    username = Label(frame, text=" Username ",font="Roboto 15").grid(row=0, column=0, sticky=E )
    username_entry = Entry(frame).grid(row=0, column=1, ipadx=25, ipady=5, sticky= E)
    Email = Label(frame, text=" Email ",font="Roboto 15").grid(row=1, column=0, sticky=E)
    Email_entry = Entry(frame).grid(row=1, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    btn = Button(frame, text ="Se Connecter", font= "Roboto 15" ,command= page.rooms, width=10, height=2).grid(row=3, columnspan=2, sticky="N")
     
    connexion.mainloop()
