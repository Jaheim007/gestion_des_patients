from curses import window
from tkinter import*
import json
from tkinter.ttk import Treeview
from turtle import left, width

def form():     
    form = Tk()
    form.title("Gestion Des Patients")
    form.resizable(False, False)
    form.geometry("1000x1000")
    heading = Label(form, text="Formulaire D'inscription Des Patients", bg="skyblue", highlightbackground="black", highlightthickness= 1, font="Roboto 20").pack(pady=30, ipadx=150, ipady=10)

    frame = Frame(form, highlightbackground= "black", highlightthickness=2)
    frame.pack(pady=50, ipadx=100, ipady=50)
    
    Nom = Label(frame, text=" Nom ",font="Roboto 15", justify="right").pack(pady=10)
    nom_entry = Entry(frame).pack(pady=3)
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15").pack(pady=10)
    prenom_entry = Entry(frame).pack(pady=3)
    
    dif_age = [
        "0","1","2","3",
        "4","5","6","7",
        "8","9","10","11",
        "12","13","14","15",
        "16","17","18","19",
        "20","21","22","23",
        "24","25","26","27",
        "28","29","30"
    ]
    
    dif_doctor = [
     "Médecins de famille",
     "Internistes",
     "Médecins d'urgence", 
     "Psychiatres", 
     "Gynécologues", 
     "Neurologues",
     "Radiologues",  
     "Pédiatres", 
     "Dentiste", 
     "Dermatologue",
     "Podiatres"
    ]
    
    dif_chambre = [
        "Chambre 1",
        "Chambre 2",
        "Chambre 3",
        "Chambre 4",
        "Chambre 5",
        "Chambre 6",
    ]
    
    drop1 = StringVar(frame) 
    drop1.set("0")
    age = Label(frame, text="Age",font="Roboto 15").pack(pady=10)
    age_drop = OptionMenu(frame, drop1, *dif_age,).pack(ipadx=75, pady=5)
    
    problème_médical = Label(frame, text="Problème Médical",font="Roboto 15").pack(pady=10)
    problème_médical_entry = Entry(frame).pack(pady=5, ipadx=15)
    
    drop2 = StringVar(frame) 
    drop2.set("Les différents médecins")
    medecin = Label(frame, text="Médecin à voir",font="Roboto 15").pack(pady=10)
    medecin_drop = OptionMenu(frame, drop2, *dif_doctor,).pack(ipadx=50, pady=5)
    
    drop3 = StringVar(frame) 
    drop3.set("Chambre")
    chambre = Label(frame, text="Salle De Repos",font="Roboto 15").pack(pady=10)
    chambre_drop = OptionMenu(frame, drop3, *dif_chambre,).pack(ipadx=50, pady=5)
    
    btn = Button(frame, text="Enregistrer Le Patient", font="Roboto 15", command= treeview).pack(ipadx=25, pady=5, ipady=10)

    form.mainloop()
    
def treeview():    
    window= Tk()
    window.title("Liste des patients")
    # frame = Frame(tree, highlightbackground="black", highlightthickness=2)
    # frame.pack(padx=200)
    tree = Treeview(window, columns=('#1','#2','#3','#4','#5','#6'), height=100)
    tree.heading('#1', text="Nom")
    tree.heading('#2', text="Prenom")
    tree.heading('#3', text="Age")
    tree.heading('#4', text="Problème Médical")
    tree.heading('#5', text="Médecin à voir")
    tree.heading('#6', text="Salle De Repos")
    
    tree.column('#0', stretch=NO, width=0)
    tree.grid()
    treeview = tree
    
    window.mainloop()
    
    
