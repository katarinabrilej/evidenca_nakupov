class Shramba:

    def __init__(self):
        self.slovar = {}
        self.nalozi_slovar()

    def nalozi_slovar(self):
        slovar = {}
        with open("shramba.txt", encoding = "utf-8") as f:
            for vrstica in f:
                izdelek, količina = vrstica.split()
                slovar[izdelek] = int(količina)
        self.slovar = slovar
        
    def povprasaj_po_nakupu(self):
        izdelek = input("napiši ime izdelka: ")
        cena = input("koliko si zapravil/a? ")
        količina = input("napiši količino ")

        with open("shramba.txt", "a", encoding = "utf-8") as shramba:
                with open("nakup_hrane.txt", "a", encoding = "utf-8") as nakup:
                    print("{} {}".format(izdelek, količina), file = shramba)
                    print("{}".format(cena), file = nakup)

        self.nalozi_slovar()

    def ali_imam_dovolj_sestavin(self):
        zeljena_jed = 
        zeljena_kolicina =
        

    

# program
#s = Shramba() # se tudi že naloži slovar!
#s.povprasaj_po_nakupu()


##def mesecna_poraba(ime_datoteke):
##    poraba = 0
##    wiht open(ime_datoteke, encoding = "utf-8") as f:
##        for vrstica in f:
##            cena = 
class Recept:

    def __init__(self):
        
        self.ime = ""
        self.sestavine = {}

    def povprasaj_po_receptu(self):
        ime = input("katero jed bi rad pripravil? ")
        sestavine = {}
        s = input("katero sestavino potrebuješ? ")
        while s != "nič več":
            koliko = float(input("koliko? "))
            sestavine[s] = koliko
            s = input("katero sestavino potrebuješ? ")

        self.ime = ime
        self.sestavine = sestavine

    
