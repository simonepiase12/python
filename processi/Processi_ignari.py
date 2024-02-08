from multiprocessing import Process
"""
multiprocessing è una libreria per la creazione, la comunicazione e la sincronizzazione tra processi
nella programmazione parallela e concorrente Process è una classe per creare processi eseguendo una funzione(o metodo)
specificata come target
"""

def process_function(data): #Operazione che deve svolgere ogni processo
    result=data*2
    print(result)

if __name__ == "__main__":
    data_list=[1,2,3,4]     #Lista dei dati
    processes=[]

    for data in data_list:
        p=Process(target=process_function,args=(data,)) #Esecuzione dell'operazione sull'elemento
        processes.append(p) #Finita l'operazione aggiunto alla lista processi
        p.start() #Avvia l'esecuzione del processo separato
    
    for p in processes:
        p.join() #Blocca il processo principale fino a quando il processo separato non termina