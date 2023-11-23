#Esercizio 2
def media_globale(t):
    tot=0
    cont=0
    for zona,info in t:
        reparto,provisettore=zona
        prodotto,*altro=info
        for pagamento,costo in altro:
            tot+=costo
            cont+=1
    media=tot/cont
    return media


def media(t,s,p):
    tot=0
    cont=0
    for zona,info in t:
        reparto,settore=zona
        prodotto,*altro=info
        if(s==settore):
            for pagamento,costo in altro:
                if(p==pagamento):
                    tot+=costo
                    cont+=1
        media=tot/cont
        return media
    return "Categoria non trovata"

def venditaMax(t):
    max=0
    for posizione,dati in t:
        for zona,info in t:
            reparto,settore=zona
            prodotto,*altro=info
            for pagamento,costo in altro:
                if(costo>max):
                    max=costo
                    prodMax=prodotto
    return (prodMax(max))


def venditaMin(t):
    min=10000
    for posizione,dati in t:
        for zona,info in t:
            reparto,settore=zona
            r="Reparto A"
            prodotto,*altro=info
            if(reparto=="Reparto A"):
                for pagamento,costo in altro:
                    if(costo<min):
                        min=costo
                        prodMin=prodotto
    return (prodMin(min))
tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )

scelta=0
while(scelta!=9):
    scelta=int(input("1)Media globale;\n2)Media catgoria;\n3)Vendita più costosa;\n4)Vendita inferiore reparto A;\n5)Vendita per reparto rispetto al totale globale;\n9)Esci\n"))
    if(scelta==1):
        print("Media globale:%2.f"%media_globale(tupla_vendite))
    if(scelta==2):
        categoria=input("Inserisci la categoria:")
        tipo=input("Inserisci il tipo di pagamento:")
        print(media(tupla_vendite,categoria,tipo))
    if(scelta==3):
        print(venditaMax(tupla_vendite))
    if(scelta==4):
        print(venditaMin(tupla_vendite))
    if(scelta==5):
        print()