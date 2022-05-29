
from platform import node
import networkx as nx
import matplotlib.pyplot as plt
from numpy import matrix
import numpy as np
import os
##
#TALLER DISCRETAS II
#PUNTO 1
#AUTOR JOSE DAVID SUAREZ CARDONA
##


def construir_grafo():
    numero_nodos, numero_aristas = map(int, input().split())
    if numero_nodos >= 1 and numero_aristas < pow(10, 5):
        grafo = nx.Graph()
        grafo = grafo.to_undirected()
        lista_aristas = []
        grafo.add_nodes_from([i+1 for i in range(numero_nodos)])
        for i in range(numero_aristas):
            node_a, node_b = map(int, input().split())
            arista = (node_a,node_b)
            lista_aristas.append(arista)
            grafo.add_edge(node_a,node_b)    
        matrix_adyancencia = np.array( nx.adjacency_matrix(grafo).todense())
        lista_nodos = [i+1 for i in range(numero_nodos)]
        #Descomentar si quiere visualizar la representacion grafica del grafo       
        nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
        plt.show()

        print(algoritmo(matrix_adyancencia,lista_nodos))
        
        
def algoritmo(MR,etiquetas):
      #NOTA
      #el algoritmo empieza en el nodo inicial que es 1,por lo tanto el nodo actual es 1, 
      # analiza el peso de sus vecinos y toma el de menor peso, despues a actualzia el nodo actual al nodo que haya escogido de menor peso
      #y despues vuelve y aplica el algoritmo al nodo actual y asi sucecivamente hasta obtener la secuencia lexicografica 
      
    lista_nodos_recorridos=[1]#lista de salida
    nodo_actual = 1 #nodo actual
    nodo_escogido =0#donde se almacena el nodo vecino con menor peso
    while(True):
            peso_actual = float("inf")              
            for i in range(MR.shape[0]):                                
                for j in range(MR.shape[1]):
                    if (etiquetas[i] == nodo_actual) and MR[i][j]==1:
                        v = etiquetas[j]#nodo vecino                                      
                        peso_vecino = v  #se toma el peso del nodo vecino   
                        if not( v in lista_nodos_recorridos ):# se valida que el nodo vecino no haya sido recorrido
                             if peso_vecino<peso_actual  :
                                peso_actual = peso_vecino
                                nodo_escogido = v #se escoge temporalmente el nodo si se comple de que el peso es menor al actual peso
                                
                nodo_actual = nodo_escogido#se le asigna al nodo actual el nodo que haya escogido con menor peso                                                                                       
                if not(nodo_actual in lista_nodos_recorridos):             
                     lista_nodos_recorridos.append(nodo_actual)                             
                if nodo_actual <= i+1:#PARA QUE NO SIGA BUSCANDO EL NODO EN EL RESTO DE LA MATRIZ
                    break                                        
            if peso_actual == float("inf"):#SI  el peso actual es infinito significa que el peso no fue modificado y por lo tanto el nodo actual no tiene nodos vecinos
                    indice_nodo_actual = lista_nodos_recorridos.index(nodo_actual)#se obtiene el indice del nodo actual 
                    nodo_escogido=lista_nodos_recorridos[indice_nodo_actual-1]#despues le asigno al nodo actual el nodo recorrido anterior de el para que se devuelva en caso de que no encuentre vecinos
            
            if len(lista_nodos_recorridos)==len(etiquetas):#condicio para saber si se ha recorrido todos los nodos en caso de que si, se para el algoritmo y retorna la lista lexicografica
                break                                                                                        
    return lista_nodos_recorridos          
                    
            

    
#implementacion del grafo       
construir_grafo()