from tkinter import*
import json

def rooms():     
    rooms = Tk()
    rooms.title("Gestion Des Patients")
    rooms.resizable(False, False)
    rooms.geometry("800x800")
    heading = Label(rooms, text="Toutes Les Chambres Des Patients", bg="skyblue", highlightbackground="black", highlightthickness= 1, font="Roboto 20").pack(pady=30, ipadx=150, ipady=10)

    btn1 = Button(rooms, text="CHAMBRE 01", command= room1, width=15, height=2).pack(pady=40)
    btn2 = Button(rooms, text="CHAMBRE 02", command= room2, width=15, height=2).pack(pady=45)
    btn3 = Button(rooms, text="CHAMBRE 03", command= room3, width=15, height=2).pack(pady=35)
    btn4 = Button(rooms, text="CHAMBRE 04", command= room4, width=15, height=2).pack(pady=35)
    
    rooms.mainloop()
    
def room1(): 
    room1 = Tk()
    room1.title("Gestion Des Patients")
    room1.resizable(False, False)
    room1.geometry("800x800")
    heading = Label(room1, text="CHAMBRE 01", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=30, ipadx=150, ipady=10)   
    
    frame = Frame(room1, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)
    
    
    
    
    btn = Button(room1, text="Nouveau patient", font="Roboto 15", width=15, height=2).pack()
    room1.mainloop()
    
def room2(): 
    room2 = Tk()
    room2.title("Gestion Des Patients")
    room2.resizable(False, False)
    room2.geometry("800x800")
    heading = Label(room2, text="CHAMBRE 02", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=30, ipadx=150, ipady=10)   
    
    frame = Frame(room1, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)
    
    
    btn = Button(room2, text="Nouveau patient", font="Roboto 15", width=15, height=2).pack()
    room2.mainloop()
    
def room3(): 
    room3 = Tk()
    room3.title("Gestion Des Patients")
    room3.resizable(False, False)
    room3.geometry("800x800")
    heading = Label(room3, text="CHAMBRE 03", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=30, ipadx=150, ipady=10)   
    
    frame = Frame(room1, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)
    
    
    btn = Button(room3, text="Nouveau patient", font="Roboto 15", width=15, height=2).pack()
    room3.mainloop()
    
def room4(): 
    room4 = Tk()
    room4.title("Gestion Des Patients")
    room4.resizable(False, False)
    room4.geometry("800x800")
    heading = Label(room4, text="CHAMBRE 04", bg="skyblue", highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=30, ipadx=150, ipady=10)   
  
    frame = Frame(room1, highlightbackground="black", highlightthickness=2)
    frame.pack(pady=50)
    
    btn = Button(room4, text="Nouveau patient", font="Roboto 15", width=15, height=2).pack()
    room4.mainloop()

