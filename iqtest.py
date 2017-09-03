import tkinter as tk
import random

def ustvari_seznam():
    
    global vprasanja, odgovoriA, odgovoriB, odgovoriC, odgovoriD, resitve
    vprasanja = []
    odgovoriA = []
    odgovoriB = []
    odgovoriC = []
    odgovoriD = []
    resitve = []
    
    with open("vprasanja.txt", "r", encoding = "utf-8") as dat:
        for vrstica in dat:
            global podatki
            podatki = vrstica.strip().split("*")
            dodano_vprasanje = podatki[0].replace("\\n", "\n")
            dodan_odgovorA = podatki[1]
            dodan_odgovorB = podatki[2]
            dodan_odgovorC = podatki[3]
            dodan_odgovorD = podatki[4]
            dodana_resitev = podatki[5]
            vprasanja.append(dodano_vprasanje)
            odgovoriA.append(dodan_odgovorA)
            odgovoriB.append(dodan_odgovorB)
            odgovoriC.append(dodan_odgovorC)
            odgovoriD.append(dodan_odgovorD)
            resitve.append(dodana_resitev)


rezultat = 0
stevilka_vprasanja = 0



def pobrisi_odgovore(x):
    del odgovoriA[x]
    del odgovoriB[x]
    del odgovoriC[x]
    del odgovoriD[x]

def preberi_datoteko(ime_datoteke, seznam, mesto):
    with open(ime_datoteke, "a", encoding = "utf-8") as d:
        print(" {} {} {} {} \n \n Pravilni odgovor: {} \n Tvoj odgovor: {} \n".format(odgovoriA[mesto], odgovoriB[mesto],odgovoriC[mesto],odgovoriD[mesto],pravilni_odgovor(mesto),seznam[mesto]), file = d)

    

def preveri(x, stevec, okno2, seznam, crka):

    preberi_datoteko("resitve.txt", seznam, x)
    pobrisi_odgovore(x)

    okno2.destroy()
    
    global rezultat
    
    ustrezen_odgovor = resitve[x]
    del resitve[x]
    
    if ustrezen_odgovor == crka:
        rezultat += 1
        novo_vprasanje(stevec)
    else:
        novo_vprasanje(stevec)
    
           
def naprej(x, stevec, okno2):


    odgovor1 = polje1.get().upper()

    with open("resitve.txt", "a", encoding = "utf-8") as d:
        print(" Pravilni odgovor: {} \n Tvoj odgovor: {} \n".format(pravilni_odgovor(x),odgovor1), file = d)
    
    pobrisi_odgovore(x)

    okno2.destroy()
    global rezultat

    ustrezen_odgovor = resitve[x]
    del resitve[x]

    if ustrezen_odgovor == odgovor1:
        rezultat += 1
        novo_vprasanje(stevec)
    else:
        novo_vprasanje(stevec)

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
    
            
def novo_okno(x, stevec):

    global stevilka_vprasanja
    stevilka_vprasanja += 1
    stevec += 1

    okno2 = tk.Tk()
    okno2.geometry('500x280')
    zgoraj = tk.Frame(okno2)
    zgoraj.pack()
    prazna1 = tk.Label(zgoraj, text = "")
    prazna1.pack()
    oznaka_vprasanja = tk.Label(zgoraj, text = str(stevec) + ". vprašanje", font = (None, 20))
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
        print("{}. {} \n " .format(stevec, vprasanja[x]), file = d)



    if odgovoriA[x] == "N":

        global polje1

        polje1 = tk.Entry(spodaj)
        polje1.pack()

        prazna4 = tk.Label(spodaj, text = "")
        prazna4.pack()
        
        potrdi = tk.Button(spodaj, text = "Potrdi", command = lambda: naprej(x, stevec, okno2))
        potrdi.pack()

      


    else:
        
        gumbA = tk.Button(spodaj, text = odgovoriA[x], command = lambda: preveri(x, stevec, okno2, odgovoriA, "A"))
        gumbB = tk.Button(spodaj, text = odgovoriB[x], command = lambda: preveri(x, stevec, okno2, odgovoriB, "B"))
        gumbC = tk.Button(spodaj, text = odgovoriC[x], command = lambda: preveri(x, stevec, okno2, odgovoriC, "C"))
        gumbD = tk.Button(spodaj, text = odgovoriD[x], command = lambda: preveri(x, stevec, okno2, odgovoriD, "D"))

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
    gumb_za_konec = tk.Button(okno3, text = "Zapri", command = lambda: izhod(okno3))
    gumb_za_konec.pack()

    okno3.mainloop()

    

def novo_vprasanje(x):

    if dolzina == x:
        
        okno2 = tk.Tk()
        okno2.geometry('500x250')
        
        prazna1 = tk.Label(okno2, text = "")
        prazna1.pack()
        izpis_rezultata = tk.Label(okno2, text = "Pravilno si odgovoril/a na {} od {} vprašanj".format(rezultat, dolzina),font = (None, 20))
        izpis_rezultata.pack()
        prazna2 = tk.Label(okno2, text = "")
        prazna2.pack()

        gumb_za_resitve = tk.Button(okno2, text = "Preveri rešitve", command = lambda: prikazi_resitve())
        gumb_za_resitve.pack()

        prazna3 = tk.Label(okno2, text = "")
        prazna3.pack()
        
        gumb_za_konec = tk.Button(okno2, text = "Končaj", command = lambda: izhod(okno2))
        gumb_za_konec.pack()


        

    else:
        global mesto_vprasanja
        mesto_vprasanja = random.randint(0, len(vprasanja)-1)
    
        novo_okno(mesto_vprasanja, x)
        
        

def dolg_kviz(x):

    ustvari_seznam()
    global dolzina
    dolzina = 4
    okno.destroy()
    novo_vprasanje(x)


def kratek_kviz(x):
    
    ustvari_seznam()
    global dolzina
    dolzina = 2
    okno.destroy()
    novo_vprasanje(x)
        
    
             
open("resitve.txt","w").close()
okno = tk.Tk()
okno.geometry('500x600')
okno.configure(background = "pink")
naslov = tk.Label(okno, text = "Super IQ kviz!!", background = "pink", font = (None, 50))
naslov.pack()

dolzina_kviza = tk.Label(okno, text = "Želiš reševati krajši(10 vprašanj) ali daljši(20 vprašanj) kviz?",background = "pink", font = (None, 15))
dolzina_kviza.pack()

prazna1 = tk.Label(okno, text = "",background = "pink")
prazna1.pack()

krajsi_gumb = tk.Button(okno, text = "krajši", command = lambda: kratek_kviz(stevilka_vprasanja))
krajsi_gumb.pack()

prazna2 = tk.Label(okno, text = "",background = "pink")
prazna2.pack()

daljsi_gumb = tk.Button(okno, text = "daljši", command = lambda: dolg_kviz(stevilka_vprasanja))
daljsi_gumb.pack()


prazna3 = tk.Label(okno, text = "",background = "pink")
prazna3.pack()

photo = tk.PhotoImage(file = "smart.gif")
slika = tk.Label(okno, image = photo)
slika.photo = photo
slika.pack()

okno.mainloop()
