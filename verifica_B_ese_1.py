#Esercizio 1
def struttura(t,c):
    tot=0
    cont=0
    max=0
    min=1000000
    t1=[]
    for citta,*altro in t:
            dati=altro[0]
            if(c==citta):
                for mese,piogge in dati:
                    if(piogge!="N/D"):
                        tot+=piogge
                        cont+=1
                        if(piogge>max):
                            max=piogge
                            meseMax=mese
                        if(piogge<min):
                            min=piogge
                            meseMin=mese
                medio=tot/cont
                t1.append(("%.2f"%medio,(max,meseMax),(min,meseMin)))
                return t1
        
    return "Citta non trovata"
                


tupla=(
        ("Milano", [("Gennaio", 120),("Febbraio", 160),("Marzo", 115),
                      ("Aprile", 50),("Maggio", 13),("Giugno", 19),
                      ("Luglio", 40),("Agosto", "N/D"),("Settembre", 215),
                      ("Ottobre", 145),("Novembre", 310),("Dicembre", 240)]),
        ("Firenze",  [("Gennaio", 150),("Febbraio", 133),("Marzo", 180),
                      ("Aprile", 12),("Maggio", 30),("Giugno", 60),
                      ("Luglio", 20),("Agosto", "N/D"),("Settembre", 50),
                      ("Ottobre", 110),("Novembre", 170),("Dicembre", 30)])
    )

citta=input("Inserisci nome città:")
print(struttura(tupla,citta))


