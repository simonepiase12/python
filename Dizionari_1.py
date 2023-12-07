
#1
dizionario={"Giuseppe Gullo":[("Matematica",9, 0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
            "Antonio Barbera":[("Matematica",8, 1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
            "Nicola Spina":[("Matematica",7.5, 2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]
            }

#3
def add(dic):
    for chiave,altro in dic.items():
        if(chiave=="Giuseppe Gullo"):
            altro.append(("Fisica",9.5,0))
        elif(chiave=="Antonio Barbera"):
            altro.append(("Fisica",8,1))
        elif(chiave=="Nicola Spina"):
            altro.append(("Fisica",8,3))
        elif(chiave=="Albert Einstein"):
            altro.append(("Fisica",10,0))

#4 
#5
def showData(name,sub):
    for chiave,altro in dizionario.items():
        if(chiave==name):
            for materia,voto,assenze in altro:
                if(materia==sub):
                    print(chiave,"in",materia,"ha come voto",voto,"e",assenze,"assenze")

#6
def showGrade(name,sub):
    for chiave,altro in dizionario.items():
        if(chiave==name):
            for materia,voto,assenze in altro:
                if(materia==sub):
                    print("Voto di",name,"in",sub,":",voto)

#7
def mediaStudent(name):
    media=0
    i=0
    for chiave,altro in dizionario.items():
        if(chiave==name):
            for materia,voto,assenze in altro:
                media+=voto
                i+=1
    media=media/i
    print("Media di",name,":",round(media,2))

#8
def mediaTot():
    media=0
    i=0
    for chiave,altro in dizionario.items():
            for materia,voto,assenze in altro:
                media+=voto
                i+=1
    media=media/i
    print("Media totale:",round(media,2))

#9
def maxAss(name):
    max=0
    mat=[]
    for chiave,altro in dizionario.items():
        if(chiave==name):
            for materia,voto,assenze in altro:
                if(assenze>=max):
                    max=assenze
            for materia,voto,assenze in altro:
                if(assenze==max):
                    mat.append(materia)
    print("Materia con più assenze di",name,":",mat)


#2
dizionario["Albert Einstein"]=[("Matematica",10, 0),("Italiano",10,0),("Inglese",10,0),("Storia",10,0),("Geografia",10,0)]

#3
add(dizionario)

#4
showData("Giuseppe Gullo","Matematica")

#5
showData("Nicola Spina","Inglese")

#6
showGrade("Antonio Barbera","Geografia")

#7
mediaStudent("Nicola Spina")

#8
mediaTot()

#9
maxAss("Nicola Spina")