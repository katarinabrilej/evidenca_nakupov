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
            #datoteka resitve.txt vsebuje okoli 40 že napisanih vprašanj, odgovorov in rešitev
            #s programom v datoteki vprasanja.py pa je omogočen enostaven način dodajanja novih vprašanj v datoteko, ki jih lahko nato uporabimo v kvizu
            #vrstice v datoteki so napisane v obliki: vprašanje*odgovorA*odgovorB*odgovorC*odgovorD*rešitev
            #vrstico preberemo, razberemo podatke in jih dodamo seznamom
            #tako dobimo sezname vorašanj, odgovorov in rešitev, ki jih uporabljamo v kvizu
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
    #iz seznamom odgovorov pobrišemo že uporabljene
    del odgovoriA[x]
    del odgovoriB[x]
    del odgovoriC[x]
    del odgovoriD[x]

def pravilni_odgovor(x):
    #na podlagi ustrezne rešitve v seznamu rešitve (tu je zapisana črka rešitve, razen v primeru ko uporabnik sam vpiše rešitev,
    #je napisana dejanska rešitev), besedno rešitev poiščemo v pripadajočem seznamu odgovorov   
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

def preberi_datoteko(ime_datoteke, seznam, mesto):
    #v datoteko zapišemo možno rešitve, pravilno rešitev in uporabnikov odgovor
    with open(ime_datoteke, "a", encoding = "utf-8") as d:
        print(" {} {} {} {} \n \n Pravilni odgovor: {} \n Tvoj odgovor: {} \n".format(odgovoriA[mesto], odgovoriB[mesto],odgovoriC[mesto],odgovoriD[mesto],pravilni_odgovor(mesto),seznam[mesto]), file = d)
    
def preveri(x, stevec, okno2, seznam, crka):
    #funkcijo uporabimo vprimeru, ko uporabnik odgovor izbere s klikom na gumb
    preberi_datoteko("resitve.txt", seznam, x)
    pobrisi_odgovore(x)
    okno2.destroy()   
    global rezultat    
    ustrezen_odgovor = resitve[x]
    del resitve[x]
    #preverimo če je uporabnikov odgovor pravilen, če je, rezultatu prištejemo 1
    if ustrezen_odgovor == crka:
        rezultat += 1
        novo_vprasanje(stevec)
    else:
        novo_vprasanje(stevec)
             
def naprej(x, stevec, okno2):
    #funkcijo uporabimo v primeru, ko uporabnik sam vpiše odgovor 
    #pridobimo uporabnikov odgovor
    odgovor1 = polje1.get().upper()
    #v datoteko zapišemo pravilni odgovor in uporabnikov odgovor
    with open("resitve.txt", "a", encoding = "utf-8") as d:
        print(" Pravilni odgovor: {} \n Tvoj odgovor: {} \n".format(pravilni_odgovor(x),odgovor1), file = d)
    
    pobrisi_odgovore(x)
    okno2.destroy()
    global rezultat
    ustrezen_odgovor = resitve[x]
    del resitve[x]
    #preverimo če je uporabnikov odgovor pravilen, če je rezultatu prištejemo 1
    if ustrezen_odgovor == odgovor1:
        rezultat += 1
        novo_vprasanje(stevec)
    else:
        novo_vprasanje(stevec)
                
def novo_okno(x, stevec):

    global stevilka_vprasanja
    stevilka_vprasanja += 1
    stevec += 1
    #ustvarimo novo okno, izpišemo številko vprašanja in vprašanje
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
    #v datoteko resitve.txt zapišemo številko vprašanja in vprašanje
    with open("resitve.txt", "a", encoding = "utf-8") as d:
        print("{}. {} \n " .format(stevec, vprasanja[x]), file = d)

    # v seznamih odgovorov imajo vprašanja, kjer ni izbire odgovorov, temveč mora uporabnik sam zapisati ustrezno
    # rešitev, namesto odgovora napisano N
    #če je ustrezen odgovor enak N ustvarimo polje v katerega bo uporabnik lahko vpisal svojo rešitev
    if odgovoriA[x] == "N":
        global polje1
        polje1 = tk.Entry(spodaj)
        polje1.pack()
        prazna4 = tk.Label(spodaj, text = "")
        prazna4.pack()        
        potrdi = tk.Button(spodaj, text = "Potrdi", command = lambda: naprej(x, stevec, okno2))
        potrdi.pack()
        
    else:
        #če ustrezen odgovor ni enak N, je naloga oblike kjer uporabnik s klikom na gumb izbere eno od štirih možnosti
        #zato ustvarimo štiri gumbe
        gumbA = tk.Button(spodaj, text = odgovoriA[x], command = lambda: preveri(x, stevec, okno2, odgovoriA, "A"))
        gumbB = tk.Button(spodaj, text = odgovoriB[x], command = lambda: preveri(x, stevec, okno2, odgovoriB, "B"))
        gumbC = tk.Button(spodaj, text = odgovoriC[x], command = lambda: preveri(x, stevec, okno2, odgovoriC, "C"))
        gumbD = tk.Button(spodaj, text = odgovoriD[x], command = lambda: preveri(x, stevec, okno2, odgovoriD, "D"))
        gumbA.pack()
        gumbB.pack()
        gumbC.pack()
        gumbD.pack()
    #iz seznama vprašanj izbrišemo uporabljeno vprašanja da ga vprihodnje ne bomo mogli več uporabiti
    del vprasanja[x]
    okno2.mainloop()
    
def izhod(x):
    x.destroy()

def izpisi_resitve(ime_datoteke):
    #iz datoteke resitve.txt prebermo resitve
    with open(ime_datoteke, "r", encoding = "utf-8") as f:
        besedilo = f.read()
    return besedilo

def prikazi_resitve():

    #odpremo okno v katerem izpišemo rešitve, ki jih dobimo iz datoteke resitve.txt
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
    
    #ko je stevilka vprasanja enaka dolzini kviza, ki smo jo predhodno nastavili, se nam pojavi zadnje okno,
    #ki nam pove rezultat, nastavimo tudi gumb s katerim dostopamo do pravilnih resitev in nasih odgovorov
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
        #naključno izberemo katero vprašanje naj sledi in odpremo novo okno
        global mesto_vprasanja
        mesto_vprasanja = random.randint(0, len(vprasanja)-1)
        novo_okno(mesto_vprasanja, x)       
        
def dolg_kviz(x):
    
    #ustvarimo seznam vprašanj, odgovorov in rešitev s pomočjo datoteke vprasanja.txt
    ustvari_seznam()
    global dolzina
    #uporabnik bo reševal kviz dolžine 20 vprašanj
    dolzina = 20
    okno.destroy()
    novo_vprasanje(x)

def kratek_kviz(x):
    
    ustvari_seznam()
    global dolzina
    dolzina = 10
    okno.destroy()
    novo_vprasanje(x)
           
#poskrbimo da se datoteka z rešitvami, ki se izpiše na koncu kviza, zbriše ko kviz začnemo znova             
open("resitve.txt","w").close()

#ustvarimo začetno okno, z dvema gumboma s katerima lahko uporabnik izbere daljši ali krajši kviz
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
