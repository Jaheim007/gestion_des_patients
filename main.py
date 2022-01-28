from tkinter import*
from modules import fonctions

window = Tk()
window.title("Gestion Des Patients")
window.resizable(False, False)
window.geometry("700x700")
heading = Label(window, text="Gestion Des Patients", bg="#144087",fg="#fff", highlightbackground="black", highlightthickness= 2, font="Roboto 15").pack(pady=30, ipadx=150, ipady=10)

frame = Frame(window, highlightbackground="black", highlightthickness=2)
frame.pack(pady=25, ipady=30, ipadx=25)
btn1 = Button(frame, text=" S'Inscrire " , command= fonctions.inscription, font="Roboto 15", width=15, height=2).pack(pady=40)
btn2 = Button(frame, text=" Se Connecter ", command= fonctions.connexion, font="Roboto 15", width=15, height=2).pack(pady=20)
btn3 = Button(frame, text=" Deconnexion " , command= window.quit, font="Roboto 15", width=15, height=2).pack(pady=30)


window.mainloop()