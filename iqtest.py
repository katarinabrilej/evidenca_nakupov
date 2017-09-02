import tkinter as tk
import random
from seznami import *

rezultat = 0
stevilka_vprasanja = 0

def pobrisi_odgovore(x1):
    del odgovoriA[x1]
    del odgovoriB[x1]
    del odgovoriC[x1]
    del odgovoriD[x1]

def preberi_datoteko(ime_datoteke, seznam, mesto):
    with open(ime_datoteke, "a", encoding = "utf-8") as d:
        print(" Pravilni odgovor: {} \n Tvoj odgovor: {} \n".format(pravilni_odgovor(mesto),seznam[mesto]), file = d)
    
    
def preveriA(x, stevilka_vprasanja,okno2):

    preberi_datoteko("resitve.txt", odgovoriA, x)
    pobrisi_odgovore(x)

    okno2.destroy()
    
    global rezultat
    
    pravilen_odgovor = resitve[x]
    del resitve[x]
    
    if pravilen_odgovor == "A":
        rezultat += 1
        novo_vprasanje(stevilka_vprasanja)
    else:
        novo_vprasanje(stevilka_vprasanja)

    

def preveriB(x, stevilka_vprasanja,okno2):

    preberi_datoteko("resitve.txt", odgovoriB, x)

    pobrisi_odgovore(x)

    okno2.destroy()
    global rezultat
    
    pravilen_odgovor = resitve[x]
    del resitve[x]
    

    if pravilen_odgovor == "B":
        rezultat += 1
        novo_vprasanje(stevilka_vprasanja)
    else:
        novo_vprasanje(stevilka_vprasanja)

def preveriC(x, stevilka_vprasanja,okno2):

    preberi_datoteko("resitve.txt", odgovoriC, x)

    pobrisi_odgovore(x)
        
    okno2.destroy()
    global rezultat
    
    pravilen_odgovor = resitve[x]
    del resitve[x]
    

    if pravilen_odgovor == "C":
        rezultat += 1
        novo_vprasanje(stevilka_vprasanja)
    else:
        novo_vprasanje(stevilka_vprasanja)

def preveriD(x, stevilka_vprasanja,okno2):

    preberi_datoteko("resitve.txt", odgovoriD, x)

    pobrisi_odgovore(x)
    
    okno2.destroy()
    global rezultat
    
    pravilen_odgovor = resitve[x]
    del resitve[x]
    

    if pravilen_odgovor == "D":
        rezultat += 1
        novo_vprasanje(stevilka_vprasanja)
    else:
        novo_vprasanje(stevilka_vprasanja)
           
def naprej(x, stevilka_vprasanja, okno2):


    odgovor1 = polje1.get()

    with open("resitve.txt", "a", encoding = "utf-8") as d:
        print(" Pravilni odgovor: {} \n Tvoj odgovor: {} \n".format(pravilni_odgovor(x),odgovor1), file = d)
    
    pobrisi_odgovore(x)

    okno2.destroy()
    global rezultat

    pravilen_odgovor = resitve[x]
    del resitve[x]

    if pravilen_odgovor == odgovor1:
        rezultat += 1
        novo_vprasanje(stevilka_vprasanja)
    else:
        novo_vprasanje(stevilka_vprasanja)

def pravilni_odgovor(x):

    if resitve[x] == "A":
        return odgovoriA[x]
    
    elif resitve[x] == "B":
        return odgovoriB[x]
    
    elif resitve[x] == "C":
        return odgovoriC[x]
    
    elif resitve[x] == "D":
        return odgovoriD[x]
    else:
        return resitve[x]
    
            
def novo_okno(x, stevilka_vprasanja):
    
    stevilka_vprasanja += 1

    okno2 = tk.Tk()
    okno2.geometry('500x280')
    zgoraj = tk.Frame(okno2)
    zgoraj.pack()
    prazna1 = tk.Label(zgoraj, text = "")
    prazna1.pack()
    oznaka_vprasanja = tk.Label(zgoraj, text = str(stevilka_vprasanja) + ". vprašanje", font = (None, 20))
    oznaka_vprasanja.pack()
    prazna2 = tk.Label(zgoraj, text = "")
    prazna2.pack()
    vprasanje = tk.Label(zgoraj, text = vprasanja[x])
    vprasanje.pack()
    prazna3 = tk.Label(zgoraj, text = "")
    prazna3.pack()
    spodaj = tk.Frame(okno2)
    spodaj.pack()

    with open("resitve.txt", "a", encoding = "utf-8") as d:
        print("{}. {} \n " .format(stevilka_vprasanja, vprasanja[x]), file = d)



    if odgovoriA[x] == "mhm":

        global polje1

        polje1 = tk.Entry(spodaj)
        polje1.pack()

        prazna4 = tk.Label(spodaj, text = "")
        prazna4.pack()
        
        potrdi = tk.Button(spodaj, text = "Potrdi", command = lambda: naprej(x, stevilka_vprasanja, okno2))
        potrdi.pack()

      


    else:
        
        gumbA = tk.Button(spodaj, text = odgovoriA[x], command = lambda: preveriA(x,stevilka_vprasanja, okno2))
        gumbB = tk.Button(spodaj, text = odgovoriB[x], command = lambda: preveriB(x,stevilka_vprasanja, okno2))
        gumbC = tk.Button(spodaj, text = odgovoriC[x], command = lambda: preveriC(x,stevilka_vprasanja, okno2))
        gumbD = tk.Button(spodaj, text = odgovoriD[x], command = lambda: preveriD(x,stevilka_vprasanja, okno2))

        gumbA.pack()
        gumbB.pack()
        gumbC.pack()
        gumbD.pack()


    
    del vprasanja[x]

    okno2.mainloop()
    
def izhod(x):
    x.destroy()

def izpisi_resitve(ime_datoteke):
    with open(ime_datoteke, "r", encoding = "utf-8") as f:
        besedilo = f.read()
    return besedilo


def prikazi_resitve():

    
    okno3 = tk.Tk()
    okno3.geometry('500x450')

    izpisane_resitve = tk.Text(okno3)
    izpisane_resitve.insert('1.0',"{}".format(izpisi_resitve("resitve.txt")))
    izpisane_resitve.pack()

    prazna = tk.Label(okno3, text = "")
    prazna.pack()
    gumb_za_konec = tk.Button(okno3, text = "Končaj", command = lambda: izhod(okno3))
    gumb_za_konec.pack()

    

def novo_vprasanje(stevilka_vprasanja):



    if dolzina == stevilka_vprasanja:
        
        okno2 = tk.Tk()
        okno2.geometry('500x250')
        
        prazna1 = tk.Label(okno2, text = "")
        prazna1.pack()
        izpis_rezultata = tk.Label(okno2, text = "Pravilno si odgovoril/a na {} od {} vprašanj".format(rezultat, dolzina))
        izpis_rezultata.pack()
        prazna2 = tk.Label(okno2, text = "")
        prazna2.pack()

        gumb_za_resitve = tk.Button(okno2, text = "Preveri rešitve" ,command = lambda: prikazi_resitve())
        gumb_za_resitve.pack()

        prazna3 = tk.Label(okno2, text = "")
        prazna3.pack()
        
        gumb_za_konec = tk.Button(okno2, text = "Končaj", command = lambda: izhod(okno2))
        gumb_za_konec.pack()


        

    else:
        x = random.randint(0, len(vprasanja)-1)
    
        novo_okno(x, stevilka_vprasanja)
        
        

def zapri_oknoD(stevilka_vprasanja):
    
    global dolzina
    dolzina = 4
    okno.destroy()
    novo_vprasanje(stevilka_vprasanja)


def zapri_oknoK(stevilka_vprasanja):

    global dolzina
    dolzina = 2
    okno.destroy()
    novo_vprasanje(stevilka_vprasanja)
        
    
             
open("resitve.txt","w").close()
okno = tk.Tk()
okno.geometry('500x600')
okno.configure(background = "pink")
navodila = tk.Label(okno, text = "Super IQ kviz!!", background = "pink", font = (None, 50))
navodila.pack()

vpr = tk.Label(okno, text = "Želiš reševati krajši(10 vprašanj) ali daljši(20 vprašanj) kviz?",background = "pink", font = (None, 15))
vpr.pack()

prazna1 = tk.Label(okno, text = "",background = "pink")
prazna1.pack()

krajsi_gumb = tk.Button(okno, text = "krajši", command = lambda: zapri_oknoK(stevilka_vprasanja))
krajsi_gumb.pack()

prazna2 = tk.Label(okno, text = "",background = "pink")
prazna2.pack()

daljsi_gumb = tk.Button(okno, text = "daljši", command = lambda: zapri_oknoD(stevilka_vprasanja))
daljsi_gumb.pack()


prazna3 = tk.Label(okno, text = "",background = "pink")
prazna3.pack()

photo = tk.PhotoImage(file = "smart.gif")
slika = tk.Label(okno, image = photo)
slika.photo = photo
slika.pack()

okno.mainloop()

