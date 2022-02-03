from tkinter import*
from tkinter import messagebox
import json


#Creation of the Sign-up page and it's different functions including the JSON File.
def inscription(): 

    #Creating The frame and the header     
    inscription = Tk()
    inscription.title("Gestion Des Patients")
    inscription.resizable(False, False)
    inscription.geometry("700x700")
   
    #The header
    heading = Label(inscription, text="Page D'Inscription", bg="#144087", fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 16").pack(pady=50, ipadx=150, ipady=10)
    
    #The frame  
    frame = Frame(inscription, highlightbackground="black", highlightthickness=2)
    frame.pack(padx=70, pady=(50),)

    #The (Last Name) Label and entry part 
    Nom = Label(frame, text=" Nom ",font="Roboto 15")
    Nom.grid(row=0, column=0, sticky=E )
    nom_entry = Entry(frame)
    nom_entry.grid(row=0, column=1, ipadx=25, ipady=5, sticky= E)
    
    #The (First Name) Label and entry part 
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.grid(row=1, column=0, sticky=E)
    prenom_entry = Entry(frame)
    prenom_entry.grid(row=1, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    #The (Email) Label and entry part 
    Email = Label(frame, text=" Email ",font="Roboto 15")
    Email.grid(row=2, column=0, sticky= E)
    email_entry = Entry(frame)
    email_entry.grid(row=2, column=1, ipadx=25, ipady=5, sticky=E)
    
    
    
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
            "email": email_entry.get()
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
            if nom_entry.get() == "" or prenom_entry.get() == "" or email_entry.get() == "" :       
                messagebox.showerror("Error", "Veuillez saisir vos informations.")
            
            else:     
                messagebox.showinfo(" Info "," Vous êtes inscrit " )  
        
        #Adding the Items to the JSON File 
        else:
        
            with open("/Users/imac-13/gestion_des_patients-1/data.json", "r") as f:
                liste = json.load(f)
                      
            liste.append(donnees)
            
            if nom_entry.get() == "" or prenom_entry.get() == "" or email_entry.get() == "" :       
                messagebox.showerror("Error", "Veuillez saisir vos informations.")
            
            else:     
                messagebox.showinfo(" Info "," Vous êtes inscrit " )
                inscription.destroy()
            
            with open("/Users/imac-13/gestion_des_patients-1/data.json", "w") as f:
                json.dump(liste, f, indent=4)

       
        
           
    btn = Button(frame, text="S'Inscrire", command=recoding, width=10, height=2, font="Roboto 15")
    btn.grid(row=3, columnspan=2, sticky="N")
    
    
    inscription.mainloop()

def connexion(): 
    
    #Creation of the Login page and it's verification.
    connexion = Tk()
    connexion.title("Gestion Des Patients")
    connexion.resizable(False, False)
    connexion.geometry("700x700")
    
    #The Header
    heading1 = Label(connexion, text="Page de Connexion", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 15").pack(pady=50, ipadx=150, ipady=10)
    
    #The Frame 
    frame = Frame(connexion, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)

    #The (Last Name) Label and entry part 
    nom = Label(frame, text=" Nom ",font="Roboto 15")
    nom.grid(row=0, column=0, sticky=E)
    nom_entry = Entry(frame)
    nom_entry.grid(row=0, column=1, ipadx=25, ipady=5, sticky= E)
    
    #The (First Name) Label and entry part 
    Prenom = Label(frame, text=" Prenom ",font="Roboto 15")
    Prenom.grid(row=1, column=0, sticky=E)
    prenom_entry = Entry(frame)
    prenom_entry.grid(row=1, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    #The (Email) Label and entry part 
    Email = Label(frame, text=" Email ",font="Roboto 15")
    Email.grid(row=2, column=0, sticky=E)
    Email_entry = Entry(frame)
    Email_entry.grid(row=2, column=1 ,ipadx=25, ipady=5, sticky= E) 
    
    def data():
        with open("/Users/imac-13/gestion_des_patients-1/data.json", "r") as f:
            liste = json.load(f) 
        
        if nom_entry.get() == "" or prenom_entry.get() == "" or Email_entry.get() == "" :       
            messagebox.showerror("Error", "Veuillez saisir vos informations.")
        else: 
            pass      
        
        for i in liste: 
            for elt in i.values():
                if nom_entry.get() in elt and prenom_entry.get() in elt and Email_entry.get() in elt:
                    messagebox.showinfo("info", "Vous êtes connecté ")
                
                break
            else:
                    messagebox.showerror("Error", "Vous n'êtes pas inscrit à ce service.")  
                    connexion.destroy()  
                    
            # connexion.destroy()
            # import page
            # print(i.values(), '\n')
            # if nom_entry.get() in i.values() and prenom_entry.get() in i.values() and Email_entry.get() in i.values():
            #     print("ok")
            #     print(i.values(), '\n')
            # else:
            #     print("no")
            #     print(i.values(), '\n')
            #     if  prenom_entry.get() in i.values():
            #         if Email_entry.get() in i.values():
            #             messagebox.showinfo("info", "Vous êtes connecté ")  
            
            # else: 
            #     messagebox.showinfo(" Info ","  Vous n'êtes inscrit")
           
              
        
           
        
    btn = Button(frame, text ="Se Connecter", font= "Roboto 15" ,command=data, width=10, height=2)
    btn.grid(row=3, columnspan=2, sticky="N")
    
    connexion.mainloop()
