### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import ConcertInformaticaSQL
### --------- Hoofdprogramma ---------------

venster = Tk()
venster.wm_title("LBConcert")
venster.iconbitmap("icon.ico")
#functies voor knoppen 
def ToonUitGegevensInListBox():
    ingevoerde_artiest = zoekVeldArtiest.get() #haalt de gegevens van het invoerveld voor de artiest
    if ingevoerde_artiest == "Josh Dun":
        ListboxUit.insert(0, "De band Twenty One Pilots speelt in Amsterdam, Ziggo Dome.")
    elif ingevoerde_artiest == "Brendon Urie":
        ListboxUit.insert(0, "De band Panic! At The Disco speelt in Amsterdam, AFAS.")
    elif ingevoerde_artiest == "Ryan Ross":
        ListboxUit.insert(0, "De band Panic! At The Disco speelt in Nijmegen, Doornroosje." )
    else: 
        ListboxUit.insert(0, "Geen info")

def ToonInfoInListbox():
    listboxMenuGebouw.delete(0, END) #dit zorgt ervoor dat de list box leeg wordt
    Gebouwgegevens_tabel = ConcertInformaticaSQL.vraagOpGebouwgegevensTabel() #hierbij wordt de functie gelinkt aan variabele
    listboxMenuGebouw.insert(0, "ID \t Plaats \t Postcode \t Straatnaam \t Gebouwnaam") #kolomnamen
    for regel in Gebouwgegevens_tabel: #haalt alle gegevens uit tabel
        listboxMenuGebouw.insert(END, regel) #insert tabelgegevens
    ListboxmenuConcert .delete(0, END) #dit zorgt ervoor dat de list box leeg wordt
    Concertgegevens_tabel = ConcertInformaticaSQL.vraagOpConcertgegevensTabel() #hierbij wordt de functie gelinkt aan variabele
    ListboxmenuConcert.insert(0, "Artiest ID \t Concertnaam \t Concert ID") #kolomnamen
    for regel in Concertgegevens_tabel: #haalt alle gegevens uit tabel
        ListboxmenuConcert.insert(END, regel) #insert de tabelgegevens


def leegVelden():
    #deze functie leegt listbox + entryfields
    entryVeldIDArtiest.delete(0, END)
    toonBandField.delete(0, END)
    zoekVeldArtiest.delete(0, END)
    ListboxmenuConcert.delete(0, END)
    listboxMenuGebouw.delete(0, END)
    ListboxUit.delete(0, END)

def zoekArtiest():
    #zoek artiest vindt ingevoerde artiesten in database 
    gevonden_artiesten = ConcertInformaticaSQL.zoekArtiestInTabel(ingevoerde_artiest.get()) #gebruikt functie uit SQL 
    for rij in gevonden_artiesten: 
        #entryfields worden gevuld met ID en Band van artiest
        entryVeldIDArtiest.insert(END, rij[0])
        toonBandField.insert(END, rij[2])
        
#tekstINTRO
tekstWelkom = Label(venster, text="Hallo! Voer de artiestnaam in, en krijg alle gegevens!")
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

#GegevensConcert
ConcertgegLbl = Label(venster, text="Concertgegevens: ")
ConcertgegLbl.grid(row=7, column=0, sticky = "W")
listboxMenuGebouw = Listbox(venster, height=6, width=50)
listboxMenuGebouw.grid(row=7, column= 1)

#uiteindelijke gegevens
LabelUit = Label(venster, text = "Jouw artiest speelt: ")
LabelUit.grid(row = 8, column = 0, sticky="W")
ListboxUit = Listbox(venster, height=6, width=50)
ListboxUit.grid(row = 8, column = 1)
buttonUit = Button(venster, text="Informatie Concert", width = 15, command=ToonUitGegevensInListBox)
buttonUit.grid(row = 9, column = 2, sticky="W")

#BTN TOON GEGEVENS
toonGegevensknop2 = Button(venster, text = "Toon gegevens", width = 15, command=ToonInfoInListbox)
toonGegevensknop2.grid(row=8, column=2, sticky = "W")

#sluitenVENSTER
closebtn = Button(venster, text="Sluit venster", width=15, command=venster.destroy)
closebtn.grid(row = 10, column = 2, sticky = "W")

#resetButton
resetButton = Button(venster, text="Leeg velden", width=15, command=leegVelden)
resetButton.grid(row=2, column=2)

#venster blijft open
venster.mainloop()