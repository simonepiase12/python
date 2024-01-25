# Dizionario che rappresenta la scacchiera con 9 posizioni, inizialmente libere
# mentre la partita si svolge il valore associato sarà o X oppure O
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
chiavi=[]
def printBoard(board,chiavi):
    print(board['top-L'],"|",board['top-M'],"|",board['top-R'])
    print("--+---+--")
    print(board['mid-L'],"|",board['mid-M'],"|",board['mid-R'])
    print("--+---+--")
    print(board['low-L'],"|",board['low-M'],"|",board['low-R'])

def controllaPosizione(board,mossa,segno):
  board[mossa]=segno

def controllaVittoria(board):
    vittoria=False
    if(board['top-L']==board['top-M']==board['top-R'] and board['top-L']!=' '):
        vittoria=True
    elif(board['mid-L']==board['mid-M']==board['mid-R'] and board['mid-L']!=' '):
        vittoria=True
    elif(board['low-L']==board['low-M']==board['low-R'] and board['low-L']!=' '):
        vittoria=True
    elif(board['top-L']==board['mid-L']==board['low-L'] and board['mid-L']!=' '):
        vittoria=True
    elif(board['top-M']==board['mid-M']==board['low-M'] and board['mid-M']!=' '):
        vittoria=True
    elif(board['top-R']==board['mid-R']==board['low-R'] and board['mid-R']!=' '):
        vittoria=True
    elif(board['top-L']==board['mid-M']==board['low-R'] and board['top-L']!=' '):
        vittoria=True
    elif(board['top-R']==board['mid-M']==board['low-L'] and board['mid-M']!=' '):
        vittoria=True
    return vittoria
#stabilisce il turno iniziale
turn = 'X'
#ciclo per gestire le 9 mosse
for i in range(9):
    #stampa la scacchiera
    #gestisci input mossa
    #aggiorna dizionario
    #cambia turno
    mossa=""
    printBoard(theBoard,chiavi)
    while(mossa!="top-L" and mossa!="top-M" and mossa!="top-R"
          and mossa!="mid-L" and mossa!="mid-M" and mossa!="mid-R"
          and mossa!="low-L" and mossa!="low-M" and mossa!="low-R"):
        mossa=input("Turno di "+turn+". Quale posizione scegli?")
    controllaPosizione(theBoard,mossa,turn)
    if(controllaVittoria(theBoard)):
        printBoard(theBoard,chiavi)
        print("Partita Terminata! Vittoria di "+turn)
        break
    else:
        if(turn=="X"):
            turn="Y"
        elif(turn=="Y"):
            turn="X"
if(not controllaVittoria(theBoard)):
   printBoard(theBoard,chiavi)
   print("Pareggio!")