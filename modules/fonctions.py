from email import message
from tkinter import*
from tkinter import messagebox
import page
import json

def inscription(): 
    inscription = Tk()
    inscription.title("Gestion Des Patients")
    inscription.resizable(False, False)
    inscription.geometry("700x700")
    heading = Label(inscription, text="Page D'Inscription", bg="#144087", fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 16").pack(pady=50, ipadx=150, ipady=10)
    
    frame = Frame(inscription, highlightbackground="black", highlightthickness=2)
    frame.pack(padx=70, pady=(50),)

    Nom = Label(frame, text=" Nom ",font="Roboto 15")
    Nom.grid(row=0, column=0, sticky=E )
    nom_entry = Entry(frame)
    nom_entry.grid(row=0, column=1, ipadx=25, ipady=5, sticky= E)
    
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.grid(row=1, column=0, sticky=E)
    prenom_entry = Entry(frame)
    prenom_entry.grid(row=1, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    Email = Label(frame, text=" Email ",font="Roboto 15")
    Email.grid(row=2, column=0, sticky= E)
    email_entry = Entry(frame)
    email_entry.grid(row=2, column=1, ipadx=25, ipady=5, sticky=E)
    
    def save1():       
        dict ={
            "Nom": nom_entry.get(),   
            "Prenom":prenom_entry.get(),   
            "Email": email_entry.get()   
        }
        
        with open("data.json", "a") as f:   
            json.dump(dict,f ,indent=4)
            
            
        if nom_entry.get()=="" or prenom_entry.get()=="" or email_entry.get() =="":       
            messagebox.showerror("Error", " Veuillez saisir vos informations. ")
            
        else:     
            messagebox.showinfo("Info","Vous êtes inscrit" )  
            
        nom_entry.delete(0,END)
        prenom_entry.delete(0,END)
        email_entry.delete(0,END)
           
    btn = Button(frame, text="S'Inscrire",command=save1 , width=10, height=2, font="Roboto 15").grid(row=3, columnspan=2, sticky="N")
    
    inscription.mainloop()

def connexion(): 
    connexion = Tk()
    connexion.title("Gestion Des Patients")
    connexion.resizable(False, False)
    connexion.geometry("700x700")
    heading1 = Label(connexion, text="Page de Connexion", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 15").pack(pady=50, ipadx=150, ipady=10)
    
    frame = Frame(connexion, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)

    nom = Label(frame, text=" Nom ",font="Roboto 15").grid(row=0, column=0, sticky=E)
    nom_entry = Entry(frame).grid(row=0, column=1, ipadx=25, ipady=5, sticky= E)
    
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15").grid(row=1, column=0, sticky=E)
    prenom_entry = Entry(frame).grid(row=1, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    Email = Label(frame, text=" Email ",font="Roboto 15").grid(row=2, column=0, sticky=E)
    Email_entry = Entry(frame).grid(row=2, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    def data():       
        try:   
            global dict 
            with open("data.json", "r") as f:
                file = json.load(f)
                
        except json.JSONDecodeError:    
            if nom_entry and prenom_entry and Email_entry not in file:      
                messagebox.showerror("Error", "Vous n'êtes pas inscrit.")
        
        else:           
            messagebox.showinfo("ShowInfo", "Bienvenue") 
        
    btn = Button(frame, text ="Se Connecter", font= "Roboto 15" ,command=data, width=10, height=2).grid(row=3, columnspan=2, sticky="N")
     
    connexion.mainloop()
