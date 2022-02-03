from tkinter import*
from tkinter import messagebox
import json
from tkinter.ttk import Treeview

def form():     
    form = Tk()
    form.title("Gestion Des Patients")
    form.resizable(False, False)
    form.geometry("1000x1000")
    heading = Label(form, text="Formulaire d'inscription ou mise à jour des patients", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 1, font="Roboto 16").pack(pady=30, ipadx=150, ipady=10)

    frame = Frame(form, highlightbackground= "black", highlightthickness=2)
    frame.pack(pady=50, ipadx=100, ipady=50)
    
    Nom = Label(frame, text=" Nom ",font="Roboto 15", )
    Nom.pack(pady=10)
    nom_entry = Entry(frame).pack(pady=3)
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.pack(pady=10)
    prenom_entry = Entry(frame).pack(pady=3)
    
    dif_age = [
        "0","1","2","3",
        "4","5","6","7",
        "8","9","10","11",
        "12","13","14","15",
        "16","17","18","19",
        "20","21","22","23",
        "24","25","26","27",
        "28","29","30","31",
        "32","33","34","35",
        "36","37","38","39",
        "40","41","42","43",
        "44","45","46","47",
        "48","49","50","51",
        "52","53","54","55",
        "56","57","58",
        "59","60"
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
     "Podiatres", 
     "Médecin Généraliste"
    ]
    
    dif_wounds =[
        "Déjà traité",
        "Toujours en traitement"
    ]
    
    dif_chambre = [
        "Chambre 1",
        "Chambre 2",
        "Chambre 3",
        "Chambre 4",
        "Chambre 5",
        "Chambre 6",
        "Pas De chambre"
    ]
    
    drop1 = StringVar(frame) 
    drop1.set("Entrer l'âge du patient")
    age = Label(frame, text="Age",font="Roboto 15")
    age.pack(pady=10)
    age_drop = OptionMenu(frame , drop1 , *dif_age).pack(ipadx=25, pady=5)
    
    problème_médical = Label(frame, text="Problème Médical",font="Roboto 15")
    problème_médical.pack(pady=10)
    problème_médical_entry = Entry(frame,).pack(pady=5, ipadx=15)
   
    drop2 = StringVar(frame) 
    drop2.set("Déjà traité ")
    status= Label(frame, text="Statut du patient",font="Roboto 15",)
    status.pack(pady=10)
    status_drop = OptionMenu(frame, drop2, *dif_wounds).pack(ipadx=50, pady=5)
    
    drop3 = StringVar(frame) 
    drop3.set("Médecin à voir")
    medecin = Label(frame, text="Les Différents Médecins",font="Roboto 15", )
    medecin.pack(pady=10)
    medecin_drop = OptionMenu(frame, drop3, *dif_doctor,).pack(ipadx=50, pady=5)
    
    drop4 = StringVar(frame) 
    drop4.set("Chambre de patient")
    chambre = Label(frame, text="Salle De Repos",font="Roboto 15")
    chambre.pack(pady=10)
    chambre_drop = OptionMenu(frame, drop4, *dif_chambre,).pack(ipadx=50, pady=5)
    
    nom_entry = StringVar()
    prenom_entry = StringVar()
    age_drop = StringVar()
    problème_médical_entry = StringVar()
    status_drop = StringVar()
    medecin_drop = StringVar()
    chambre_drop = StringVar()
     
    nom1 = nom_entry.get()
    prenom1 = prenom_entry.get()
    age1 = age_drop.get()
    pro1 = problème_médical_entry.get()
    stat1 = status_drop.get()
    med1 = medecin_drop.get()
    room1 = chambre_drop.get()
    
    def save():       
          
        dict ={
            "Nom": nom1,
            "Prenom": prenom1,
            "Age": age1,
            "Probleme_medical": pro1,
            "Statuts": stat1,
            "Medecin": med1,
            "Chambre": room1
            }
        with open("form.json", "a") as f:   
            json.dump(dict,f ,indent=4)
        print(dict)
    btn= Button(frame, text="Enregistrer Le Patient", command=save, font="Roboto 15")
    btn.pack(ipadx=25, pady=10, ipady=10)
    
    btn2 = Button(form, text="Voir la liste des patients", command= tree , font="Roboto 15") 
    btn2.pack(ipadx=25, pady=10, ipady=10)
    
    form.mainloop()
    
def tree():
    window = Tk()
    window.title("Gestion des Stocke")
    
    tree = Treeview(window, columns=('#1','#2', '#3', '#4', '#5','#6', '#7'), height=50)
    tree.heading('#1', text="Nom")
    tree.heading('#2', text="Prenom")
    tree.heading('#3', text="Age")
    tree.heading('#4', text="Problème_médical" )
    tree.heading('#5', text="Statut" )
    tree.heading('#6', text="Medecin à voir" )
    tree.heading('#7', text="Salle De Repos" )

    tree.column('#0', stretch=NO, width=0)
    tree.grid()
    
    btn = Button(window, text="Voir la liste des patients" ,command= form, font="Roboto 15")
    btn.grid(ipadx=25, pady=10, ipady=10)
    window.mainloop()
   
   
   
        
    form.mainloop()
    
   
    
    
