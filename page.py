from re import I
from tkinter import*
from tkinter import ttk,messagebox
import tree
import json
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
from turtle import width

# Creating the formula of inscription and update 
def form():     
    form = Tk()
    form.title("Gestion Des Patients")
    heading = Label(form, text="Formulaire d'inscription ou mise à jour des patients", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 1, font="Roboto 16")
    heading.pack(pady=20, ipadx=150, ipady=10)

    #The Frame 
    frame = Frame(form, highlightbackground= "black", highlightthickness=2)
    frame.pack(pady=10, ipadx=100, ipady=50)
    
    #The Last name Label 
    Nom = Label(frame, text=" Nom ",font="Roboto 15", )
    Nom.pack(pady=10)
    nom_entry = Entry(frame)
    nom_entry.pack(pady=10)
    
    #The first Name Label
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.pack(pady=10)
    prenom_entry = Entry(frame)
    prenom_entry.pack(pady=10)
    
    # The Age Label and combobox 
    agelabel = Label(frame, text="Age",font="Roboto 15")
    agelabel.pack(pady=10)
    
    def age():     
       age_combo.get()
    
    age_combo = ttk.Combobox(frame, width = 20 , state='readonly' )
    age_combo ['values']= ("0","1","2","3",
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
        "59","60")
    
    age_combo.pack(pady=10)
    age_combo.set('')
    
    status= Label(frame, text="État du patient",font="Roboto 15")
    status.pack(pady=10)
    
    #The Status Label and combobox
    def statut():
        statut_combo.get()
        
    statut_combo = ttk.Combobox(frame, width = 20 , textvariable = statut, state='readonly')
    statut_combo ['values']= ("Déjà traité", "Toujours en traitement")
    statut_combo.pack(pady=10)
    statut_combo.set('')
    
    #The medical Problem Label and combobox
    problème_médical = Label(frame, text="Problème Médical",font="Roboto 15")
    problème_médical.pack(pady=10)
    problème_médical_entry = Entry(frame)
    problème_médical_entry.pack(pady=10)
    
    #The Doctor Label and the combobox
    medecin = Label(frame, text=" Les Différents Médecins ", font="Roboto 15")
    medecin.pack(pady=10)
    
    def medecin():
        medecin_combo.set('')
        medecin_combo.get()
        
    medecin_combo = ttk.Combobox(frame, width = 20 , state='readonly')
    medecin_combo ['values']= ("Médecins de famille",
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
    "Médecin Généraliste", 
    "pas de médecin à voir")
    
    medecin_combo.pack(pady=10)
    
    
    chambre = Label(frame, text="Salle De Repos",font="Roboto 15")
    chambre.pack(pady=10)
    
    #The Different Rooms and the room Label
    def chambre(): 
        chambre_combo.set('')        
        chambre_combo.get()
         
    chambre_combo = ttk.Combobox(frame, width = 20 ,  state='readonly')
    chambre_combo ['values']= ("Chambre 1","Chambre 2","Chambre 3","Chambre 4","Chambre 5","Chambre 6","Pas De chambre")
    chambre_combo.pack(pady=10)
    
    #Creating the Function which allows you to store in JSON File  
    def save(): 
        liste = [] 
        
        donnes = {
            "Nom ": nom_entry.get(),
            "Prenom": prenom_entry.get(),
            "Age": age_combo.get(),
            "Statut": statut_combo.get(),
            "Problème Médical": problème_médical_entry.get(),
            "Medecin": medecin_combo.get(),
            "Chambre": chambre_combo.get()
            }     
        
        liste.append(donnes)
        
        try:      
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "r", encoding='utf-8') as f:
                liste =json.load(f)
        
        except json.decoder.JSONDecodeError:           
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "w", encoding='utf-8') as f:
                json.dump(liste, f, ensure_ascii=False,indent=4)
                
            messagebox.showinfo(" Info "," Le patient a été enregistré " ) 
         
        else:
            
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "r",encoding='utf-8') as f:
                liste = json.load(f)
                      
            liste.append(donnes)
             
            
            with open("/Users/imac-13/gestion_des_patients-1/form.json", "w", encoding='utf-8') as f:
                json.dump(liste, f,ensure_ascii=False, indent=4)

            messagebox.showinfo(" Info "," Le patient a été enregistré " ) 
            
        nom_entry.delete(0,END)
        prenom_entry.delete(0,END)
        age_combo.set('') 
        statut_combo.set('')
        problème_médical_entry.delete(0,END)
        medecin_combo.set('')
        chambre_combo.set('')
        
    btn= Button(frame, text="Enregistrer Le Patient",command=save,  font="Roboto 15",relief=FLAT)
    btn.pack(ipadx=25, pady=10, ipady=10)

    btn2 = Button(form, text="Voir la liste des patients", command=tree.tree , font="Roboto 15",relief=FLAT) 
    btn2.pack(ipadx=25, pady=5, ipady=10)

    form.mainloop()
        
    
   
    
    
