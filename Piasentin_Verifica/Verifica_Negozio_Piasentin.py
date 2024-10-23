#9:35
class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice = codice
    self.fornitore = fornitore
    self.marca = marca
    self.prezzo = prezzo
    self.quantita = quantita

  def scheda_articolo(self):
    return f"Codice: {self.codice}\nFornitore: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantità: {self.quantita}"

  def modifica_scheda(self):
    scelta = int(input("Scegli campo da modificare:\n1)Fornitore\n2)Marca\n3)Prezzo\n4)Quantità\n"))

    match scelta:
        case 1:
            fornitore = str(input("Inserisci nuvovo fornitore:"))
            self.fornitore = fornitore
        case 2:
            marca = str(input("Inserisci nuvova marca:"))
            self.marca = marca
        case 3:
            prezzo = int(input("Inserisci nuvovo prezzo:"))
            self.prezzo = prezzo
        case 4:
            quantita = int(input("Inserisci nuvova quantità:"))
            self.quantita = quantita

#9:39
class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      super().__init__(codice,fornitore,marca,prezzo,quantita)
      self.pollici = pollici
      self.tipo = tipo

    def scheda_articolo(self):
      return super().scheda_articolo()+f"\nPollici:{self.pollici}\nTipo: {self.tipo}"
    
#9:39
class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    super().__init__(codice,fornitore,marca,prezzo,quantita)
    self.dimensioni = dimensioni
    self.modello = modello

  def scheda_articolo(self):
    return super().scheda_articolo()+f"\nDimensioni:{self.dimensioni}\nModello: {self.modello}"

#10:13
class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    self.codice = codice
    self.data = data 
    self.piva = piva
    self.indirizzo = indirizzo
    self.lista_articoli = []

  def aggiungi_articolo(self,articolo):
    trovato = False
    for a in self.lista_articoli:
       if(articolo.codice==a.codice):
          trovato = True
    if(trovato):
       print("Articolo già presente nella lista")
       return
    
    if isinstance(articolo,Televisore):
      self.lista_articoli.append(articolo)
      tipo_articolo="televisore"
      print(f"{tipo_articolo} con codice {articolo.codice} aggiunto all'ordine {self.codice}")
    elif isinstance(articolo,Frigorifero):
      self.lista_articoli.append(articolo)
      tipo_articolo="frigorifero"
      print(f"{tipo_articolo} con codice {articolo.codice} aggiunto all'ordine {self.codice}")
    else:
       print("L'articolo non può esssere aggiunto alla lista")
    

  def rimuovi_articolo(self,articolo):
    for a in self.lista_articoli:
        if(a.codice==articolo.codice):
           self.lista_articoli.remove(articolo)
           print(f"Articolo con codice {articolo.codice} rimosso dall'ordine con codice {self.codice}")
           return
    print("Articolo non trovato")

  def importo_ordine(self):
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)
    n = 0
    somma = 0
    for articolo in self.lista_articoli:
        n += 1
        somma += articolo.prezzo*articolo.quantita
        
    print(f"Importo ordine con codice {self.codice} contenente {n} articoli = {somma}")
        

  def dettaglio_ordine(self):
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...
    sT=0
    sF=0
    for articolo in self.lista_articoli:
        if isinstance(articolo,Televisore):
            print("\nArticolo: Televisore\n")
            print(f"Importo: {articolo.prezzo*articolo.quantita}\n")
            print(articolo.scheda_articolo())
            sT += articolo.prezzo*articolo.quantita
        elif isinstance(articolo,Frigorifero):
            print("\nArticolo: Frigorifero\n")
            print(f"Importo: {articolo.prezzo*articolo.quantita}\n")
            print(articolo.scheda_articolo())
            sF += articolo.prezzo*articolo.quantita
    somma = sT + sF

    return([sT,sF,somma])

#10:46
class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio
    self.lista_ordini = []

  def aggiungi_ordine(self,ordine):
    trovato = False
    for o in self.lista_ordini:
       if(o.codice == ordine.codice):
          trovato = True
    if(trovato):
        print(f"Ordine di codice {ordine.codice} già presente")
        return
    self.lista_ordini.append(ordine)
    print(f"Ordine {ordine.codice} aggiunto alla lista ordini di codice {self.codice_negozio}")

  def rimuovi_ordine(self,ordine):
    for o in self.lista_ordini:
        if(o.codice==ordine.codice):
           self.lista_ordini.remove(ordine)
           print(f"Ordine con codice {ordine.codice} rimosso dalla lista ordini con codice {self.codice_negozio}")
           return
    print("Ordine non trovato")

  def totale_ordini(self):
    sT = 0
    sF = 0
    print(f"Lista ordini {self.codice_negozio}")
    for ordine in self.lista_ordini:
        print(f"Ordine {ordine.codice}")
        for articolo in ordine.lista_articoli:
            if isinstance(articolo,Televisore):
                print("\nArticolo: Televisore\n")
                print(f"Importo: {articolo.prezzo*articolo.quantita}\n")
                print(articolo.scheda_articolo())
                sT += articolo.prezzo*articolo.quantita
            elif isinstance(articolo,Frigorifero):
                print("\nArticolo: Frigorifero\n")
                print(f"Importo: {articolo.prezzo*articolo.quantita}\n")
                print(articolo.scheda_articolo())
                sF += articolo.prezzo*articolo.quantita
        somma = sT + sF
    return ([sT,sF,somma])



t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
t5 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
t1.modifica_scheda()
print(t1.scheda_articolo())

t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)
ordine1.aggiungi_articolo(t5)

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)

ordine1.importo_ordine()

importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")


ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")

