from tkinter import*
from tkinter import messagebox
import json
import page
from subprocess import call 

#Creation of the Sign-up page and it's different functions including the JSON File.
def inscription(): 
    
    #Creating The frame and the header     
    inscription = Tk()
    inscription.title("Gestion Des Patients")
    
    #The frame  
    frame = Frame(inscription, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=200, ipady=20, ipadx=25)
    
    #The header
    heading = Label(frame, text="Page D'Inscription", bg="#144087", fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 16")
    heading.pack(pady=20, ipadx=150, ipady=10)
    
    #The (Last Name) Label and entry part 
    Nom = Label(frame, text=" Nom ",font="Roboto 15")
    Nom.pack(pady=10)
    nom_entry = Entry(frame)
    nom_entry.pack(pady=10)
    
    #The (First Name) Label and entry part 
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.pack(pady=10)
    prenom_entry = Entry(frame)
    prenom_entry.pack(pady=10) 
    
    #The (Email) Label and entry part 
    Email = Label(frame, text=" Email ",font="Roboto 15")
    Email.pack(pady=10)
    email_entry = Entry(frame)
    email_entry.pack(pady=10)
    
    password = Label(frame, text=" Password ",font="Roboto 15")
    password.pack(pady=10)
    password_entry = Entry(frame)
    password_entry.pack(pady=10)
    
    confirm_password = Label(frame, text=" Confirm Password ",font="Roboto 15")
    confirm_password.pack(pady=10)
    confirm_password_entry = Entry(frame)
    confirm_password_entry.pack(pady=10)
    
    
    #This is the function which allows me to create a JSON file and store all the different (nurse) user in the file
    
    """In order for This function to work, 
    Firstly, we must create an empty list and dictionary which contains a list of my different entry.
    Secondly, we must use the function try and execpt to verify the error which occurs when the JSON file is empty, (json.decoder.JSONDecodeError)
    Finally, we must add the conditions needed the user doesn't fill the form."""
    
    def recoding():
        liste = []
        
        donnees = {
            "nom": nom_entry.get(),
            "prenom": prenom_entry.get(),
            "email": email_entry.get(),
            "password" : password_entry.get(),
            "confirm password": confirm_password_entry.get()
        }
            
        liste.append(donnees)
       
        #Reading of the function
        try:
            with open("/Users/imac-13/gestion_des_patients-1/data.json", "r") as f:
                liste = json.load(f)
        
        #Fixing the error and the writing mode        
        except json.decoder.JSONDecodeError:           
            
            with open("/Users/imac-13/gestion_des_patients-1/data.json", "w") as f:
                json.dump(liste, f, indent=4)
            
               
            #The Condition
            if confirm_password_entry.get() != password_entry.get():
                    messagebox.showerror("Error", "Vos mots de passe ne correspondent pas")
            
            elif nom_entry.get() == "" or prenom_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "" or confirm_password_entry.get() == "":       
                messagebox.showerror("Error", "Veuillez saisir vos informations.")
                
            else:     
                messagebox.showinfo(" Info "," Vous êtes inscrit " )  
                inscription.destroy()
        
        #Adding the Items to the JSON File 
        else:
        
            with open("/Users/imac-13/gestion_des_patients-1/data.json", "r") as f:
                liste = json.load(f)
                      
            liste.append(donnees)
            if confirm_password_entry.get() != password_entry.get():
                messagebox.showerror("Error", "Vos mots de passe ne correspondent pas")
            
            elif nom_entry.get() == "" or prenom_entry.get() == "" or email_entry.get() == "" :       
                messagebox.showerror(" Error ", " Veuillez saisir vos informations. ")
        
            else:     
                messagebox.showinfo(" Info "," Vous êtes inscrit " )
                inscription.destroy()
                
            
            with open("/Users/imac-13/gestion_des_patients-1/data.json", "w") as f:
                json.dump(liste, f, indent=4)
                
        
        nom_entry.delete(0,END)    
        prenom_entry.delete(0,END)    
        email_entry.delete(0,END)    
        password_entry.delete(0,END)    
        confirm_password_entry.delete(0,END)    
        
        
        
    btn = Button(frame, text="S'Inscrire", command=recoding, width=10, height=2, font="Roboto 15")
    btn.pack(pady=30)
    
    inscription.mainloop()

def connexion():
    
    #Creation of the Login page and it's verification.
    connexion = Tk()
    connexion.title("Gestion Des Patients")
    
    #The Frame 
    frame = Frame(connexion, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=200, ipady=20, ipadx=25)
   
    #The Header
    heading1 = Label(frame, text="Page de Connexion", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 15")
    heading1.pack(pady=50, ipadx=150, ipady=10)
    
    #The (Last Name) Label and entry part 
    nom = Label(frame, text=" Nom ",font="Roboto 15")
    nom.pack(pady=10)
    nom_entry = Entry(frame)
    nom_entry.pack(pady=10)
    
    #The (First Name) Label and entry part 
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.pack(pady=10)
    prenom_entry = Entry(frame)
    prenom_entry.pack(pady=10) 
    
    #The (Email) Label and entry part 
    Email = Label(frame, text=" Email ",font="Roboto 15")
    Email.pack(pady=10)
    Email_entry = Entry(frame)
    Email_entry.pack(pady=10) 
    
    password = Label(frame, text=" Password ",font="Roboto 15")
    password.pack(pady=10)
    password_entry = Entry(frame)
    password_entry.pack(pady=10)
    
    def data():
        with open("/Users/imac-13/gestion_des_patients-1/data.json", "r") as f:
            liste = json.load(f) 
        for i in liste: 
                for elt in i.values():
                    
                    if nom_entry.get() == "" or prenom_entry.get() == "" or Email_entry.get() == "" or password_entry.get() == "":       
                        messagebox.showerror("Error", "Veuillez saisir vos informations.")
                    
                    elif password_entry.get() != elt :        
                        messagebox.showerror("Error", "Vos mots de passe ne correspondent pas")
                        
                    else:
                        messagebox.showinfo("info", "Vous êtes connecté ")
                    
                        # connexion.destroy()
                    break   
                    # elif nom_entry.get() == "" or prenom_entry.get() == "" or Email_entry.get() == "" or password_entry.get() == "" or confirm_password_entry.get() == "":       
                    #     messagebox.showerror("Error", "Veuillez saisir vos informations.")
                    #     connexion.destroy()
                        
                    # messagebox.showerror("Error", "Vous n'êtes pas inscrit à ce service.")  
                   
                     
                    
    btn = Button(frame, text ="Se Connecter", font= "Roboto 15", command=page.form, width=10, height=2,relief=FLAT)
    btn.pack( pady=10, ipady=10)
    
    connexion.mainloop()
