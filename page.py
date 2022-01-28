from tkinter import*
import json

def form():     
    form = Tk()
    form.title("Gestion Des Patients")
    form.resizable(False, False)
    form.geometry("1000x1000")
    heading = Label(form, text="Formulaire d'inscription ou mise à jour des patients", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 1, font="Roboto 16").pack(pady=30, ipadx=150, ipady=10)

    frame = Frame(form, highlightbackground= "black", highlightthickness=2)
    frame.pack(pady=50, ipadx=100, ipady=50)
    
    Nom = Label(frame, text=" Nom ",font="Roboto 15", justify="right").pack(pady=10)
    nom_entry = Entry(frame, textvariable=StringVar()).pack(pady=3)
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15").pack(pady=10)
    prenom_entry = Entry(frame, textvariable=StringVar()).pack(pady=3)
    
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
    age = Label(frame, text="Age",font="Roboto 15").pack(pady=10)
    age_drop = OptionMenu(frame , drop1 , *dif_age).pack(ipadx=25, pady=5)
    
    problème_médical = Label(frame, text="Problème Médical",font="Roboto 15").pack(pady=10)
    problème_médical_entry = Entry(frame, textvariable=StringVar()).pack(pady=5, ipadx=15)
   
    drop2 = StringVar(frame) 
    drop2.set("Déjà traité ")
    status= Label(frame, text="Statut du patient",font="Roboto 15", ).pack(pady=10)
    status_drop = OptionMenu(frame, drop2, *dif_wounds).pack(ipadx=50, pady=5)
    
    drop3 = StringVar(frame) 
    drop3.set("Médecin à voir")
    medecin = Label(frame, text="Les Différents Médecins",font="Roboto 15", ).pack(pady=10)
    medecin_drop = OptionMenu(frame, drop3, *dif_doctor,).pack(ipadx=50, pady=5)
    
    drop4 = StringVar(frame) 
    drop4.set("Chambre de patient")
    chambre = Label(frame, text="Salle De Repos",font="Roboto 15").pack(pady=10)
    chambre_drop = OptionMenu(frame, drop4, *dif_chambre,).pack(ipadx=50, pady=5)
    
    btn = Button(frame, text="Enregistrer Le Patient", font="Roboto 15",).pack(ipadx=25, pady=10, ipady=10)


    
    

    form.mainloop()
    
   
    
    
