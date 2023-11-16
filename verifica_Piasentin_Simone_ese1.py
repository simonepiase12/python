#Esercizio 1
def struttura(t,r):
    tot=0
    cont=0
    max=0
    min=1000000
    t1=[]
    for reparto,*altro in t:
            dati=altro[0]
            if(r==reparto):
                for mese,entrate in dati:
                    if(entrate!="N/D"):
                        tot+=entrate
                        cont+=1
                        if(entrate>max):
                            max=entrate
                            meseMax=mese
                        if(entrate<min):
                            min=entrate
                            meseMin=mese
                medio=tot/cont
                t1.append(("%.2f"%medio,(max,meseMax),(min,meseMin)))
                return t1
        
    return "Reparto non trovato"
                


tupla=(
        ("Elettronica", [("Gennaio", 12000),("Febbraio", 16000),("Marzo", 11500),
                      ("Aprile", 16600),("Maggio", 13450),("Giugno", 19000),
                      ("Luglio", 13500),("Agosto", 19000),("Settembre", 21500),
                      ("Ottobre", 14500),("Novembre", 31000),("Dicembre", 24000)]),
        ("Domestica",  [("Gennaio", 15000),("Febbraio", 13300),("Marzo", 18500),
                      ("Aprile", 12700),("Maggio", 12430),("Giugno", 26000),
                      ("Luglio", 24500),("Agosto", 23000),("Settembre", 17500),
                      ("Ottobre", 11500),("Novembre", 17000),("Dicembre", 33000)])
    )

reparto=input("Inserisci nome reparto:")
print(struttura(tupla,reparto))


