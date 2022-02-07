from pydoc import text
from tkinter import*
import json
from tkinter.ttk import Treeview
import page

#The Next page which shows the results of the formula  
 
def tree():
    window = Tk()
    window.title("La Liste Des Patients")
    tree = Treeview(window, height=30) 
    tree['columns']=("Nom", "Prenom", "Age","Statut", "Problème Medical", "Medecin", "Chambre")
    
    tree.heading("Nom", text="Nom", )
    tree.heading("Prenom", text="Prenom", )
    tree.heading("Age", text="Age", )
    tree.heading("Statut", text="Statut", )
    tree.heading("Problème Medical", text="Problème Medical", )
    tree.heading("Medecin", text="Medecin", )
    tree.heading("Chambre", text="Chambre", )
    
    tree.column("Nom",  )
    tree.column("Prenom", )
    tree.column("Age",  )
    tree.column("Statut", )
    tree.column("Problème Medical",  )
    tree.column("Medecin",  )
    tree.column("Chambre",  )
    
    
    with open("/Users/imac-13/gestion_des_patients-1/form.json", "r", encoding='utf-8') as f:
        liste = json.load(f)
        for i in liste: 
            for elt in i.values():
                tree.insert( parent='',index='end', values=(elt))
                
    
    tree.pack(pady=20, ipady=100)
    
    btn = Button(window, text="Retour" ,command= page.form , font="Roboto 15")
    btn.pack(ipadx=25, pady=10, ipady=10)
 
    window.mainloop()
    