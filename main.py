from tkinter import*
from modules import fonctions

#Creating the frame for the main page and adding the different buttons with their functions.
window = Tk()
window.title("Gestion Des Patients")

#The Frame and the Buttons 
frame = Frame(window, highlightbackground="black", highlightthickness=2)
frame.pack(pady=200, ipady=20, ipadx=25)

#The Header and it's title
heading = Label(frame, text="Gestion Des Patients", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 15")
heading.pack(pady=20, ipadx=100, ipady=10)

#The first Button goes to the first function which is the Sign-up form.
btn1 = Button(frame, text=" S'Inscrire " , command= fonctions.inscription, font="Roboto 15", width=15, height=2, relief=FLAT)
btn1.pack(pady=30, )

#The Second Button goes to the second function which is the Login Form.
btn2 = Button(frame, text=" Se Connecter ", command= fonctions.connexion, font="Roboto 15", width=15, height=2 ,relief=FLAT)
btn2.pack(pady=30)

#The Third Button goes to the third function which allows you to leave the program  
btn3 = Button(frame, text=" Deconnexion " , command= window.quit, font="Roboto 15", width=15, height=2,relief=FLAT)
btn3.pack(pady=30)

window.mainloop()