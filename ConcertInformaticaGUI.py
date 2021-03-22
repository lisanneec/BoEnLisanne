### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import ConcertInformatieSQL
### --------- Hoofdprogramma ---------------
venster = Tk()
venster.wm_title("LBConcert")
venster.iconbitmap("icon.ico")

#tonen van gebouw gegevens in een list box 
def ToonMenuGebouwInListbox():
    listboxMenuGebouw.delete(0, END) #dit zorgt ervoor dat de list box leeg wordt
    Gebouwgegevens_tabel = ConcertInformatieSQL.vraagopGegevensGebouwgegevens_tabel()
    for regel in Gebouwgegevens_tabel: 
        listboxMenuGebouw.insert(END, regel)
listboxMenuGebouw.insert(0, "ID \t Plaats \t Postcode \t Adres \t Naam")

def ToonMenuConcertInListbox():
    listboxMenuConcert.delete(0, END) #dit zorgt ervoor dat de list box leeg wordt
    Gebouwgegevens_tabel = ConcertInformatieSQL.vraagopGegevensConcertgegevens_tabel()
    for regel in Concertgegevens_tabel: 
        listboxMenuConcert.insert(END, regel)
listboxMenuConcert.insert(0, "ID \t Plaats \t Postcode \t Adres \t Naam")

#tekstINTRO
tekstWelkom = Label(venster, text="Hallo! Zoek uit waar jouw favoriete artiest speelt.")
tekstWelkom.grid( row = 0, column = 0, sticky= "W")

#zoekenARTIEST
artiest = Label(venster, text="Artiestnaam: ")
artiest.grid(row = 1, column = 0, sticky = "W")
input_ariest = StringVar()
inputField_artiest = Entry(venster, textvariable=input_ariest)
inputField_artiest.grid(row = 1, column = 1, sticky = "W")
btnSearchArtiest = Button(venster, text ="Zoek Artiest", width=15, command= ConcertInformatieSQL.zoekArtiest)
btnSearchArtiest.grid(row=1, column=2, sticky = "W")

#artiestBand
bandArtiest = Label(venster, text="Artiest Band: ")
bandArtiest.grid(row = 2, column = 0, sticky = "W")
variabele = StringVar()
Num_Entry = Entry(venster, textvariable=variabele)
Num_Entry.grid(row=2, column= 1, sticky = "W")

#gegevens van de artiest
btnToonGegevens = Button(venster, text="Toon gegevens", width=15,  command= "toonGegevens" ) #toonGegevens moet nog geschreven worden!!!
btnToonGegevens.grid(row = 2, column = 2, sticky = "W")
tkst = Label(venster, text="Gegevens van de Artiest:" )
tkst.grid(row = 3, column = 0, sticky = "W")

#Concert
concertnaamLbl = Label( venster, text = "Naam van concert: " )
concertnaamLbl.grid(row = 4, column = 0, sticky = "W")
ListboxmenuConcert = Listbox(venster, height=6, width=50)
ListboxmenuConcert.grid(row=4, column=1)

#Gebouw
gebouwnaamLbl = Label(venster, text = "Gebouwnaam: ")
gebouwnaamLbl.grid(row = 5, column = 0, sticky = "W")
menuGebouw = Listbox(venster,height=6, width=50)
menuGebouw.grid(row=5, column=1)

#GegevensConcert
ConcertgegLbl = Label(venster, text="Concertgegevens: ")
ConcertgegLbl.grid(row=6, column=0, sticky = "W")
menuGegevens = Listbox(venster, height=6, width=50)
menuGegevens.grid(row=6, column= 1)

#BTN TOON GEGEVENS 2
toonGegevensknop2 = Button(venster, text = "Toon gegevens", width = 15, command="ToonMenuConcertInListbox")
toonGegevensknop2.grid(row=6, column=2, sticky = "W")

#sluitenVENSTER
closebtn = Button(venster, text="Sluit venster", width=15, command=venster.destroy)
closebtn.grid(row = 8, column = 2, sticky = "W")

#venster blijft open
venster.mainloop()