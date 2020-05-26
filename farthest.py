
import utilities as ut
from random import sample

MAX= 9223372036854775807


def distanza(k, C, matrix): #k nodo, C un insieme e matrice come matrice di adiacenza
    minimo=MAX
    for i in range(0, len(C)):
        if minimo> matrix[k, int(C[i])]:
            minimo= matrix[k, int(C[i])]
    return minimo

def selezione(V,C,matrix):
    ############ SELEZIONE #######################
    massimo=-1
    k=-1 #nodo selezionato 
    for i in range(0, len(V)):
        dist=distanza(int(V[i]), C, matrix)
        if dist>massimo:
            massimo= dist
            k=int(V[i])
    return k

def printCycle(C):
    string=""
    for i in range(0, len(C)):
        val= int(C[i]) + 1
        string+= str(val) + " "
    print(string)

def farthest(file_name):

    ############# LETTURA FILE ###############
    print(file_name)
    matrix=ut.parseFile(file_name)
    n=len(matrix)
    #print(matrix)

    ############ VARIABILI DA UTILIZZARE ############
    C=[] #insieme di archi risultanti
    Tot=0 #peso totale del ciclo risultante
    V=[] #insieme di tutti i nodi iniziali che vengono estratti man mano
    for i in range(0, n):
        V.append(str(i))
    #print(V)

    ############# INIZIALIZZAZIONE ##################
    minimo= MAX
    j=-1
    for i in range(1, n):
        if matrix[0,i]<minimo:
            minimo=matrix[0,i]
            j=i
    
    #inserisco i primi due nodi nel circuito parziale
    C.append(str(0))
    C.append(str(j))
    #elimino i due nodi inseriti dall'insieme di tutti i vertici
    V.remove(str(0))
    V.remove(str(j))

    k=selezione(V,C,matrix)
    while k!=-1: #se ritorna -1 non ho più elementi da selezionare
        ########### INSERIMENTO #####################
        #arco {i, j} in C che minimizza matrix[i,k] + matrix[k,j] - matrix[i, j]
        minimo=MAX
        pos=-1 #dove inserire il nodo k dopo aver trovato la soluzione
        for i in range(0, len(C)): #controllo le coppie di archi all'interno di C
                if i+1< len(C):
                    val=matrix[int(C[i]),k] + matrix[k,int(C[i+1])] - matrix[int(C[i]), int(C[i+1])]
                    j=i+1
                else:
                    val=matrix[int(C[i]),k] + matrix[k,int(C[0])] - matrix[int(C[i]), int(C[0])]
                    j=0
                if val<minimo: 
                    minimo=val
                    pos=j

        #inserisco K tra i e j nella soluzione finale, elimino K da V e lo aggiungo a C
        V.remove(str(k))
        C.insert(pos, str(k))

        k=selezione(V,C,matrix)

    #calcolo peso del ciclo costruito 
    for i in range(0, len(C)):
        if i+1< len(C):
            Tot+= matrix[int(C[i]), int(C[i+1])]
        else:
            Tot+= matrix[int(C[i]), int(C[0])]
    
    printCycle(C)
    print('Totale: ', Tot)


farthest('burma14.tsp')
    
        

