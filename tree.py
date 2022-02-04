from tkinter import*
import json
from tkinter.ttk import Treeview
import page

#The Next page which shows the results of the formula   
def tree():
    window = Tk()
    window.title("Gestion des Stocke")
    tree = Treeview(window) 
    tree['columns']=("Nom", "Prenom", "Age","Statut", "Problème Medical", "Medecin", "Chambre")
    
    tree.column("Nom", anchor=W, )
    tree.column("Prenom", anchor=W, )
    tree.column("Age", anchor=W, )
    tree.column("Statut", anchor=W, )
    tree.column("Problème Medical", anchor=W, )
    tree.column("Medecin", anchor=W, )
    tree.column("Chambre", anchor=W, )
    

    tree.heading("Nom", text="Nom", anchor=W)
    tree.heading("Prenom", text="Prenom", anchor=W)
    tree.heading("Age", text="Age", anchor=CENTER)
    tree.heading("Statut", text="Statut", anchor=W)
    tree.heading("Problème Medical", text="Problème Medical", anchor=W)
    tree.heading("Medecin", text="Medecin", anchor=W)
    tree.heading("Chambre", text="Chambre", anchor=W)
    
    with open("/Users/imac-13/gestion_des_patients-1/form.json", "r", encoding='utf-8') as f:
        liste = json.load(f)
        for i in liste: 
            for elt in i.values():
                tree.insert(parent='',index='end', values=(elt))
                
    tree.pack(pady=20, ipady=100)
    
    btn = Button(window, text="Retour" ,command= page.form , font="Roboto 15")
    btn.pack(ipadx=25, pady=10, ipady=10)
    window.mainloop()
    