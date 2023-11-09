def prezzo_medio(t,p,g):
    somma=0
    i=0
    for prodotto,giorno,prezzo in t:
        if(prodotto==p and giorno==g):
            somma+=prezzo
            i+=1
    if(i==0):
        return "Prodotto non trovato o giorno non disponibile"
    return somma/i
prezzi_prodotti=(
    ("Mela","Lunedì",1.0),("Mela","Martedì",1.1),("Mela","Mercoledì",1.2),("Banana","Lunedì",0.8),("Banana","Martedì",0.9),("Banana","Mercoledì",1.1),
    ("Mela","Giovedì",1.4),("Mela","Venerdì",1.0),("Mela","Sabato",1.5),("Banana","Giovedì",1.0),("Banana","Venerdì",1.3),("Banana","Sabato",0.9),
    ("Mela","Lunedì",1.2),("Mela","Martedì",1.2),("Mela","Mercoledì",1.4),("Banana","Lunedì",1.1),("Banana","Martedì",0.5),("Banana","Mercoledì",0.6),
    ("Mela","Giovedì",0.7),("Mela","Venerdì",0.9),("Mela","Sabato",0.6),("Banana","Giovedì",1.3),("Banana","Venerdì",0.6),("Banana","Sabato",0.7),
)
prodotto=input("Inserisci il prodotto:")
giorno=input("Inserisci il giorno:")
print(prezzo_medio(prezzi_prodotti,prodotto,giorno))