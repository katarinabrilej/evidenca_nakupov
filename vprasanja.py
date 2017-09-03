import tkinter as tk


def dodaj():
        
    vprasanje = entry_vprasanje.get()
    odgovorA = entry_odgovorA.get().upper()
    odgovorB = entry_odgovorB.get().upper()
    odgovorC = entry_odgovorC.get().upper()
    odgovorD = entry_odgovorD.get().upper()
    resitev = entry_resitev.get().upper()

    with open("vprasanja.txt", "a", encoding = "utf-8") as f:
        print("{}*{}*{}*{}*{}*{}".format(vprasanje, odgovorA, odgovorB, odgovorC, odgovorD, resitev), file = f)


    entry_vprasanje.delete(0,"end")
    entry_odgovorA.delete(0,"end")
    entry_odgovorB.delete(0,"end")
    entry_odgovorC.delete(0,"end")
    entry_odgovorD.delete(0,"end")
    entry_resitev.delete(0,"end")
       
def izhod(x):
    x.destroy()
    
def naprej():

    okno.destroy()
    okno2 = tk.Tk()
    okno2.geometry('350x280')

    global entry_vprasanje, entry_odgovorA ,entry_odgovorB, entry_odgovorC, entry_odgovorD, entry_resitev

    label_vprasanje = tk.Label(okno2, text = "vprašanje:").grid(row = 0, column = 0)
    entry_vprasanje = tk.Entry(okno2)
    entry_vprasanje.grid(row = 0, column = 1)
    
    label_odgovorA = tk.Label(okno2, text = "odgovor A:").grid(row =1, column = 0)
    entry_odgovorA = tk.Entry(okno2)
    entry_odgovorA.grid(row = 1, column = 1)
    
    label_odgovorB = tk.Label(okno2, text = "odgovor B:").grid(row = 2, column = 0)
    entry_odgovorB = tk.Entry(okno2)
    entry_odgovorB.grid(row = 2, column = 1)
    
    label_odgovorC = tk.Label(okno2, text = "odgovor C:").grid(row = 3, column = 0)
    entry_odgovorC = tk.Entry(okno2)
    entry_odgovorC.grid(row = 3, column = 1)
    
    label_odgovorD = tk.Label(okno2, text = "odgovor D:").grid(row = 4, column = 0)
    entry_odgovorD = tk.Entry(okno2)
    entry_odgovorD.grid(row = 4, column = 1)
    
    label_resitev = tk.Label(okno2, text = "rešitev:").grid(row = 5, column = 0)
    entry_resitev = tk.Entry(okno2)
    entry_resitev.grid(row = 5, column = 1)

    prazna = tk.Label(okno2, text = "").grid(row = 6, column = 0)

    dodaj_gumb = tk.Button(okno2, text = "dodaj vprašanje", command = lambda: dodaj()).grid(row = 7, column = 1)
    koncaj_gumb = tk.Button(okno2, text = "končaj", command = lambda: izhod(okno2)).grid(row = 8, column = 1)

    okno2.mainloop()
        
    
             
okno = tk.Tk()
okno.geometry('500x180')
okno.configure(background = "peach puff")

prazna1 = tk.Label(okno, text = "",background = "peach puff")
prazna1.pack()
naslov = tk.Label(okno, text = "Vnos vprašanj za Super IQ kviz", background = "peach puff", font = (None, 30))
naslov.pack()

prazna2 = tk.Label(okno, text = "",background = "peach puff")
prazna2.pack()

naprej_gumb = tk.Button(okno, text = "ZAČNI", command = lambda: naprej())
naprej_gumb.pack()

prazna2 = tk.Label(okno, text = "",background = "peach puff")
prazna2.pack()


okno.mainloop()



