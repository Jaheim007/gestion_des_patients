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
    Nom.grid(row=0, column=0)
    nom_entry = Entry(frame)
    nom_entry.grid(row=0, column=1)
    last = nom_entry.get()
     
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.grid(row=1, column=0)
    prenom_entry = Entry(frame)
    prenom_entry.grid()
    first = prenom_entry.get()
    
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
    agelabel= Label(frame, text="Age",font="Roboto 15")
    agelabel.grid(row=3, column=0)
    
    drop1 = StringVar(frame) 
    drop1.set("Entrer l'âge du patient")
    age_drop = OptionMenu(frame , drop1 , *dif_age)
    age_drop.grid()
    age = age_drop.get()
    
    
    problème_médical = Label(frame, text="Problème Médical",font="Roboto 15")
    problème_médical.grid(row=4, column=0)
    problème_médical_entry = Entry(frame)
    problème_médical_entry.grid()
    problem = problème_médical_entry.get()
    
    status= Label(frame, text="Statut du patient",font="Roboto 15")
    status.grid(row=5, column=0)
    
    drop2 = StringVar(frame) 
    drop2.set(" Déjà traité ")
    status_drop = OptionMenu(frame, drop2, *dif_wounds)
    status_drop.grid()
    statut = drop2.get()
    
    medecin = Label(frame, text="Les Différents Médecins",font="Roboto 15")
    medecin.grid(row=6, column=0)
    
    drop3 = StringVar(frame) 
    drop3.set("Médecin à voir")
    medecin_drop = OptionMenu(frame, drop3, *dif_doctor,)
    medecin_drop.grid(row=0, column=0)
    med = drop3.get()
    
    chambre = Label(frame, text="Salle De Repos",font="Roboto 15")
    chambre.grid(row=7, column=0)
    
    drop4 = StringVar(frame) 
    drop4.set("Chambre de patient")
    chambre_drop = OptionMenu(frame, drop4, *dif_chambre,)
    chambre_drop.grid(row=0, column=0)
    selection = drop4.get()
  
    def save(): 
        liste = [] 
        
        donnes = {
            "Nom ": last,
            "Prenom": first,
            "Age": age,
            "Problème Médical": problem,
            "Statut": statut,
            "Medecin": med,
            "Chambre": selection
            }     
        
        liste.append(donnes)
        try:      
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "r") as f:
                liste =json.load(f)
        
        except json.decoder.JSONDecodeError:           
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "w") as f:
                json.dump(liste, f, indent=4)
        
            if last == "" or first == "" or problem == "" :       
                messagebox.showerror("Error", "Veuillez saisir vos informations.")
            
            else:     
                messagebox.showinfo(" Info "," Le patient a été enregistré " )  
                
        else:
            
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "r") as f:
                liste = json.load(f)
                      
            liste.append(donnes)
            
            if last == "" or first == "" or problem == "" :       
                messagebox.showerror("Error", "Veuillez saisir vos informations.")
            
            else:     
                messagebox.showinfo(" Info "," Le patient a été enregistré " )  
            
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "w") as f:
                json.dump(liste, f, indent=4)

        nom_entry.delete(0,END)
        prenom_entry.delete(0,END)
        problème_médical_entry.delete(0,END)
        
       
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
    
   
    
    
