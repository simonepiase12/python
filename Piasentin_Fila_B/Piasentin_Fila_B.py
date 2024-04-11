"""
# Aiuto per il punto 7
tempi = [(2, 15, 50), (2, 27, 45), (3, 10, 30)]
max_tempo = max(tempi)
print(max_tempo)

# Aiuto per il punto 9
def tempo_medio(tempi):
    # Inizializza le variabili per sommare i tempi
    totale_minuti = 0
    totale_secondi = 0
    totale_centesimi = 0

    # Somma i tempi
    #  ...

    # Calcola il numero totale di tempi
    #totale_tempi = ....

++++++++++++++++++++
    media_minuti = totale_minuti / totale_tempi
    media_secondi = totale_secondi / totale_tempi
    media_centesimi = totale_centesimi / totale_tempi


    return [int(media_minuti), int(media_secondi), int(media_centesimi)]


tempi_di_gara = [(2, 45, 50), (2, 32, 65), (2, 48, 80)]

media = tempo_medio(tempi_di_gara)

print(f"Tempo medio di gara: {media[0]:2d}:{media[1]:2d}.{media[2]:02d}")
"""


def addEvent(event):
    for chiave in dict.keys():
        if(chiave == "Giuseppe Gullo"):
            dict[chiave].append((event,(5,10,0),"Juniores mas"))
        elif(chiave=="Antonia Barbera"):
            dict[chiave].append((event,(7,21,5),"Juniores fem"))
        elif(chiave=="Nicola Esposito"):
            dict[chiave].append((event,(4,32,21),"Juniores mas"))
        elif(chiave=="Simone Piasentin"):
            dict[chiave].append((event,(4,26,15),"Juniores mas"))
    print("Disciplina aggiunta:\n",dict)

def printTuple(name,event):
    found = False
    for chiave in dict.keys():
        if(chiave==name):
            for first,second,third,fourth in dict.values():
                discipline,time,cat=first
                if(discipline==event and not found):
                    found = True
                    print("Giuseppe Gullo tupla campestre:\n",dict[chiave][0])

def printEvent(name,event):
    found=False
    for chiave,*altro in dict.items():
        if(chiave==name):
            for first,second,third,fourth in altro:
                discipline,time,cat=third
                min,sec,mil=time
                if(discipline==event and not found):
                    found=True
                    print("Name:",name,"\nEvent:",event,"\nTime:",min,":",sec,":",mil,"\nCathegory:",cat)

def printTime(name,event):
    found=False
    for chiave,*altro in dict.items():
        if(chiave==name):
            for first,second,third,fourth in altro:
                discipline,time,cat=second
                min,sec,mil=time
                if(discipline==event and not found):
                    found=True
                    print("Name:",name,"\nEvent:",event,"\nTime:",min,":",sec,":",mil,"\nCathegory:",cat)

def maxTime(event,cat):
    time=[]
    for chiave,*altro in dict.items():
        for first,second,third,fourth in altro:
            discipline,timeG,cate=third
            if(discipline==event and cat==cate):
                time.append(timeG)
    maxTime = max(time)
    print("Tempo massimo:",maxTime)


def minTime(event,cat):
    time=[]
    name=[]
    for chiave,*altro in dict.items():
        for first,second,third,fourth in altro:
            discipline,timeG,cate=second
            if(discipline==event and cat==cate):
                time.append(timeG)
                name.append(chiave)

    minTime = min(time)
    minName = name[time.index(minTime)]
    print("Tempo minimo:",minTime,"\nAtleta:",minName)


def mediaTime(event,cat):
    totMin=0
    totSec=0
    totMil=0
    cont=0
    for chiave,*altro in dict.items():
        for first,second,third,fourth in altro:
            discipline,time,cate=first
            min,sec,mil=time
            cont+=1
            totMin+=min
            totSec+=sec
            totMil+=mil
    mediaMin=totMin/cont
    mediaSec=totSec/cont
    mediaMil=totMil/cont
    time=[int(mediaMin), int(mediaSec), int(mediaMil)]
    print(f"Tempo medio di gara: {time[0]:2d}:{time[1]:2d}.{time[2]:02d}")

def addAtleta():
    sesso=""
    atleta=input("Inserisci nome ecognome dell'atleta:")
    while(sesso!="M" and sesso!="F"):
        sesso=input("Maschio o femmina(M/F)?")
    campestre=addCampestre(sesso)
    centoMetri=addCentoMetri(sesso)
    duecentoMetri=addDuecentoMetri(sesso)
    milleMetri=addMilleMetri(sesso)
    dict[atleta]=[campestre,centoMetri,duecentoMetri,milleMetri]
    print("Atleta aggiunto")

def addCampestre(sesso):
    min=int(input("Inserisci minuti della campestre:"))
    sec=int(input("Inserisci secondi della campestre:"))
    mil=int(input("Inserisci millesimi della campestre:"))
    if(sesso=="F"):
        return["Corsa Campestre",(min,sec,mil),"Juniores fem"]
    else:
        return["Corsa Campestre",(min,sec,mil),"Juniores mas"]

def addCentoMetri(sesso):
    min=int(input("Inserisci minuti dei 100 metri:"))
    sec=int(input("Inserisci secondi dei 100 metri:"))
    mil=int(input("Inserisci millesimi dei 100 metri:"))
    if(sesso=="F"):
        return["100 Metri",(min,sec,mil),"Juniores fem"]
    else:
        return["100 Metri",(min,sec,mil),"Juniores mas"]
    
def addDuecentoMetri(sesso):
    min=int(input("Inserisci minuti dei 200 metri:"))
    sec=int(input("Inserisci secondi dei 200 metri:"))
    mil=int(input("Inserisci millesimi dei 200 metri:"))
    if(sesso=="F"):
        return["200 Metri",(min,sec,mil),"Juniores fem"]
    else:
        return["200 Metri",(min,sec,mil),"Juniores mas"]
    
def addMilleMetri(sesso):
    min=int(input("Inserisci minuti dei 1000 metri:"))
    sec=int(input("Inserisci secondi dei 1000 metri:"))
    mil=int(input("Inserisci millesimi dei 1000 metri:"))
    if(sesso=="F"):
        return["1000 Metri",(min,sec,mil),"Juniores fem"]
    else:
        return["1000 Metri",(min,sec,mil),"Juniores mas"]
dict = {
        "Giuseppe Gullo":[("Corsa Campestre",(40,21,0),"Juniores mas"),("100 metri",(0,12,0),"Juniores mas"),("200 metri",(0,29,12),"Juniores mas")],
        "Antonia Barbera":[("Corsa Campestre",(0,39,11),"Juniores fem"),("100 metri",(0,18,0),"Juniores fem"),("200 metri",(0,0,0),"Juniores fem")],
        "Nicola Esposito":[("Corsa Campestre",(0,43,22),"Juniores mas"),("100 metri",(0,14,0),"Juniores mas"),("200 metri",(0,36,19),"Juniores mas")]
    }

#2
dict["Simone Piasentin"] = [("Corsa Campestre",(4,18,7),"Juniores mas"),("100 metri",(0,18,0),"Juniores mas"),("200 metri",(0,30,12),"Juniores mas")]
print("Atleta aggiunto:\n",dict)

print("\n")

#3
addEvent("1000 metri")

print("\n")

#4
printTuple("Giuseppe Gullo","Corsa Campestre")

print("\n")

#5
printEvent("Nicola Esposito","200 metri")

print("\n")

#6
printTime("Antonia Barbera","100 metri")

print("\n")

#7
maxTime("200 metri","Juniores mas")

print("\n")

#8
minTime("100 metri","Juniores mas")

print("\n")

#9
mediaTime("Corsa Campestre","Juniores mas")

print("\n")

#10
addAtleta()