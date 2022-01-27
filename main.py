from tkinter import*
from modules import fonctions

window = Tk()
window.title("Gestion Des Patients")
window.resizable(False, False)
window.geometry("500x500")
heading = Label(window, text="Gestion Des Patients", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 15").pack(pady=30, ipadx=150, ipady=10)

btn1 = Button(window, text=" S'Inscrire " , command= fonctions.inscription, font="Roboto 15", width=15, height=2).pack(pady=40)
btn2 = Button(window, text=" Se Connecter ", command= fonctions.connexion, font="Roboto 15", width=15, height=2).pack(pady=50)
btn3 = Button(window, text=" Deconnexion " , command= window.quit, font="Roboto 15", width=15, height=2).pack(pady=30)


window.mainloop()