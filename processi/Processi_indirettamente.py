from multiprocessing import Process,Queue,current_process
import os 
"""
--Queue: classe che rappresenta una coda condivisa tra processi.
é utilizzata per consentire la comunicazione tra processi,
consentemdo loro di scambiarsi dati in modo sicuro.
put(item):Aggiunge un elemento alla coda
get():rimuove e restituisce un elemento dalla coda
empty():True se lacoda è vuota e False se non lo è
full():True se la coda è piena  e False se non lo è
qsize():Restituisce il numero di lementi nella coda
close():Chiude la coda
--current_process:funzione che restituisce un oggetto process che
rappresenta il processo in esecuzione
"""

def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name},ProcessPID: {current_process().pid}")

def process_function(data, result_queue): #Operazione processi
    process_id()
    print("Elabora:",data)
    result=data*2
    result_queue.put(result) #Risultato aggiunto alla coda

if __name__ == "__main__":
    data_list=[1,2,3,4]
    result_queue=Queue() #Creazione coda
    processes=[]

    for data in data_list:
        p=Process(target=process_function(data,result_queue)) #Chiamata operazione
        processes.append(p)  #Risultato aggiunto a lista processi
        p.start()

    for p in processes:
        p.join()
    
    print("Il main stampa i risultati")
    while not result_queue.empty(): #Finchè la coda dei risultati non è vuota viene estratto e stampato ogni elemento
        result=result_queue.get()
        print(result)