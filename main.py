from tkinter import*
from modules import fonctions

#Creating the frame for the main page and adding the different buttons with their functions.
window = Tk()
window.title("Gestion Des Patients")
window.resizable(False, False)
window.geometry("700x700")

#The Header and it's title
heading = Label(window, text="Gestion Des Patients", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 15").pack(pady=30, ipadx=150, ipady=10)

#The Frame and the Buttons 
frame = Frame(window, highlightbackground="black", highlightthickness=2)
frame.pack(pady=25, ipady=30, ipadx=25)

#The first Button goes to the first function which is the Sign-up form.
btn1 = Button(frame, text=" S'Inscrire " , command= fonctions.inscription, font="Roboto 15", width=15, height=2).pack(pady=40)

#The Second Button goes to the second function which is the Login Form.
btn2 = Button(frame, text=" Se Connecter ", command= fonctions.connexion, font="Roboto 15", width=15, height=2).pack(pady=20)

#The Third Button goes to the third function which allows you to leave the program  
btn3 = Button(frame, text=" Deconnexion " , command= window.quit, font="Roboto 15", width=15, height=2).pack(pady=30)

window.mainloop()