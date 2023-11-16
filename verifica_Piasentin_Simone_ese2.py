#Esercizio 2
def media_globale(t):
    tot=0
    cont=0
    for posizione,dati in t:
        citta,provincia=posizione
        anno,*altro=dati
        if(anno==2023):
            for mese,mm in altro:
                if(mm!="N/D"):
                    tot+=mm
                    cont+=1
    media=tot/cont
    return media


def media(t,p,m):
    tot=0
    cont=0
    for posizione,dati in t:
        citta,provincia=posizione
        anno,*altro=dati
        if(p==provincia):
            for mese,mm in altro:
                if(m==mese):
                    if(mm!="N/D"):
                        tot+=mm
                        cont+=1
            media=tot/cont
            return media  
    return "Provincia non trovata"

def pioggiaMax(t):
    max=0
    for posizione,dati in t:
        citta,provincia=posizione
        anno,*altro=dati
        n="Milano"
        for n in provincia:
            for mese,mm in altro:
                if(mm!="N/D"):
                    if(mm>max):
                        max=mm
                        meseMax=mese
    return "Pioggia massima a Milano nel mese di",meseMax,"con",max,"millimetri di pioggia"


def pioggiaMin(t):
    min=10000
    for posizione,dati in t:
        citta,provincia=posizione
        anno,*altro=dati
        for mese,mm in altro:
            if(mm!="N/D"):
                if(mm<min):
                    min=mm
                    meseMin=mese
    return "Mese con meno pioggia",meseMin,"con",min,"millimetri di pioggia"

def provinciaPer(t,n)
tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2023, ("gennaio",20))),(("Vittuone","Milano"),(2023, ("febbraio",50))),(("Vittuone","Milano"),(2023, ("marzo",80))),
                      (("Vittuone","Milano"),(2023, ("aprile",60))),(("Vittuone","Milano"),(2023, ("maggio",80))),(("Vittuone","Milano"),(2023, ("giugno","N/D"))),
                      (("Vittuone","Milano"),(2023, ("luglio",30))),(("Vittuone","Milano"),(2023, ("agosto","N/D"))),(("Vittuone","Milano"),(2023, ("settembre",80))),
                      (("Vittuone","Milano"),(2023, ("ottobre",120))),(("Vittuone","Milano"),(2023, ("novembre",165))),(("Vittuone","Milano"),(2023, ("dicembre",180))),
                      (("Sedriano","Milano"),(2023, ("gennaio",50))),(("Sedriano","Milano"),(2023, ("febbraio",40))),(("Sedriano","Milano"),(2023, ("marzo",60))),
                      (("Sedriano","Milano"),(2023, ("aprile",60))),(("Sedriano","Milano"),(2023, ("maggio",80))),(("Sedriano","Milano"),(2023, ("Giugno","N/D"))),
                      (("Sedriano","Milano"),(2023, ("luglio",30))),(("Sedriano","Milano"),(2023, ("agosto","N/D"))),(("Sedriano","Milano"),(2023, ("settembre",80))),
                      (("Sedriano","Milano"),(2023, ("ottobre",150))),(("Sedriano","Milano"),(2023, ("novembre",140))),(("Sedriano","Milano"),(2023, ("dicembre",240))),
                      (("Varenna","Lecco"),(2023, ("gennaio",150))),(("Varenna","Lecco"),(2023, ("febbraio",60))),(("Varenna","Lecco"),(2023, ("marzo",90))),
                      (("Varenna","Lecco"),(2023, ("aprile",160))),(("Varenna","Lecco"),(2023, ("maggio",80))),(("Varenna","Lecco"),(2023, ("Giugno","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",130))),(("Varenna","Lecco"),(2023, ("agosto",50))),(("Varenna","Lecco"),(2023, ("settembre",130))),
                      (("Varenna","Lecco"),(2023, ("ottobre",150))),(("Varenna","Lecco"),(2023, ("novembre",190))),(("Varenna","Lecco"),(2023, ("dicembre",200)))
                      )
scelta=0
while(scelta!=9):
    scelta=int(input("1)Media globale;\n2)Media provincia;\n3)Città più piovosa Milano;\n4)Mese con meno pioggia;\n5)Percentuale per provincia rispetto al totale globale;\n9)Esci\n"))
    if(scelta==1):
        print("Media globale:%2.f"%media_globale(tupla_pluviometrica))
    if(scelta==2):
        provincia=input("Inserisci la provincia:")
        mese=input("Inserisci il mese:")
        print(media(tupla_pluviometrica,provincia,mese))
    if(scelta==3):
        print(pioggiaMax(tupla_pluviometrica))
    if(scelta==4):
        print(pioggiaMin(tupla_pluviometrica))
    if(scelta==5):
        print()