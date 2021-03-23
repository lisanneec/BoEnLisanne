### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import ConcertInformaticaSQL
### --------- Hoofdprogramma ---------------
#tonen van gebouw gegevens in een list box 
'''
def ToonMenuGebouwInListbox():
    listboxMenuGebouw.delete(0, END) #dit zorgt ervoor dat de list box leeg wordt
    Gebouwgegevens_tabel = ConcertInformaticaSQL.vraagopGegevensGebouwgegevens_tabel()
    for regel in Gebouwgegevens_tabel: 
        listboxMenuGebouw.insert(END, regel)
listboxMenuGebouw.insert(0, "ID \t Plaats \t Postcode \t Adres \t Naam")

def ToonMenuConcertInListbox():
    listboxMenuConcert.delete(0, END) #dit zorgt ervoor dat de list box leeg wordt
    Gebouwgegevens_tabel = ConcertInformaticaSQL.vraagopGegevensConcertgegevens_tabel()
    for regel in Concertgegevens_tabel: 
        listboxMenuConcert.insert(END, regel)
listboxMenuConcert.insert(0, "ID \t Plaats \t Postcode \t Adres \t Naam")
'''
venster = Tk()
venster.wm_title("LBConcert")
venster.iconbitmap("icon.ico")
def leegVelden():
    entryVeldIDArtiest.delete(0, END)
    toonBandField.delete(0, END)
def zoekArtiest():
    gevonden_artiesten = ConcertInformaticaSQL.zoekArtiestInTabel(ingevoerde_artiest.get())
    zoekVeldArtiest.delete(0, END)
    for rij in gevonden_artiesten:
        entryVeldIDArtiest.insert(END, rij[0])
        toonBandField.insert(END, rij[2])

#tekstINTRO
tekstWelkom = Label(venster, text="Hallo! Zoek uit waar jouw favoriete artiest speelt. Voer de artiestnaam in, en krijg alle gegevens!")
tekstWelkom.grid( row = 0, column = 0, sticky= "W")

#zoekenARTIEST
artiestlbl = Label(venster, text="Artiestnaam: ")
artiestlbl.grid(row = 1, column = 0, sticky = "W")
ingevoerde_artiest = StringVar()
zoekVeldArtiest = Entry(venster, textvariable = ingevoerde_artiest)
zoekVeldArtiest.grid(row = 1, column = 1, sticky = "W")
btnSearchArtiest = Button(venster, text ="Info artiest", width=15, command= zoekArtiest)
btnSearchArtiest.grid(row=1, column=2, sticky = "W")

#artiestID
IDlabelArtiest = Label(venster, text="Aangewezen ID-nummer Artiest: ")
IDlabelArtiest.grid(row=2, column = 0, sticky="W")
entryVeldIDArtiest = Entry(venster)
entryVeldIDArtiest.grid( row = 2, column = 1, sticky="W")

#artiestBand
bandArtiest = Label(venster, text="Artiest Band: ")
bandArtiest.grid(row = 3, column = 0, sticky = "W")
variabele = StringVar()
toonBandField = Entry(venster, textvariable=variabele)
toonBandField.grid(row=3, column= 1, sticky = "W")

#Concert
concertnaamLbl = Label( venster, text = "Naam van concert: " )
concertnaamLbl.grid(row = 5, column = 0, sticky = "W")
ListboxmenuConcert = Listbox(venster, height=6, width=50)
ListboxmenuConcert.grid(row=5, column=1)

#Gebouw
gebouwnaamLbl = Label(venster, text = "Gebouwnaam: ")
gebouwnaamLbl.grid(row = 6, column = 0, sticky = "W")
menuGebouw = Listbox(venster,height=6, width=50)
menuGebouw.grid(row=6, column=1)

#GegevensConcert
ConcertgegLbl = Label(venster, text="Concertgegevens: ")
ConcertgegLbl.grid(row=7, column=0, sticky = "W")
menuGegevens = Listbox(venster, height=6, width=50)
menuGegevens.grid(row=7, column= 1)

#BTN TOON GEGEVENS 2
toonGegevensknop2 = Button(venster, text = "Toon gegevens", width = 15, command="ToonMenuConcertInListbox")
toonGegevensknop2.grid(row=8, column=2, sticky = "W")

#sluitenVENSTER
closebtn = Button(venster, text="Sluit venster", width=15, command=venster.destroy)
closebtn.grid(row = 9, column = 2, sticky = "W")

#resetButton
resetButton = Button(venster, text="Leeg velden", width=15, command=leegVelden)
resetButton.grid(row=2, column=2)

#venster blijft open
venster.mainloop()