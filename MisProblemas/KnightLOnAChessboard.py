#https://www.hackerrank.com/challenges/knightl-on-chessboard/submissions/code/210635015
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
def GrafoKnightL(grafo,mov1,mov2,n):
    #print("grafo inicial: {}".format(grafo))
    grafoAnterior = grafo.copy()
    nuevosNodos = []
    for casilla in grafo:
        if len(grafo[casilla]) == 0:
            #print("casilla: {}".format(casilla))
            for i in range(2):
                for j in range(2):
                    nuevaCasilla = (casilla[0]+pow(-1,i)*mov1,casilla[1]+pow(-1,j)*mov2)
                    if (nuevaCasilla not in grafo[casilla]) and (0<=nuevaCasilla[0]<=n and 0<=nuevaCasilla[1]<=n):
                        #print("salto: {}".format(nuevaCasilla))
                        grafo[casilla].append(nuevaCasilla)
                        if nuevaCasilla not in grafo:
                            nuevosNodos.append(nuevaCasilla)
                    nuevaCasilla2 = (casilla[0]+pow(-1,i)*mov2,casilla[1]+pow(-1,j)*mov1)
                    if (nuevaCasilla2 not in grafo[casilla]) and (0<=nuevaCasilla2[0]<=n and 0<=nuevaCasilla2[1]<=n):
                        #print("salto 2: {}".format(nuevaCasilla2))
                        grafo[casilla].append(nuevaCasilla2)
                        if nuevaCasilla2 not in grafo:
                            nuevosNodos.append(nuevaCasilla2)
    for nuevoNodo in nuevosNodos:
        grafo[nuevoNodo] = []
    if grafoAnterior != grafo:
        GrafoKnightL(grafo,mov1,mov2,n)
    return grafo

def BreadthFirstSearch(grafo):
    casillaInicial =(0,0)
    white = []
    black = []
    gray = []
    queue = []
    grafoDistancias = {}
    #print("debug 1")
    for nodo in grafo: 
        white.append(nodo)
    queue.append(casillaInicial)
    grafoPadres = {}
    white.remove(casillaInicial)
    gray.append(casillaInicial)
    grafoDistancias[casillaInicial] = 0
    #print("debug 2")
    while len(queue) != 0:
        #print("debug 3") 
        u = queue[0]
        queue.remove(u)
        distanciaU = grafoDistancias[u]
        for casillaConectada in grafo[u]:
            if casillaConectada in white:
                white.remove(casillaConectada)
                gray.append(casillaConectada)
                queue.append(casillaConectada)
                if casillaConectada not in grafoDistancias:
                    grafoDistancias[casillaConectada] = distanciaU + 1
                if casillaConectada not in grafoPadres:
                    grafoPadres[casillaConectada] = u
        gray.remove(u)
        black.append(u)
    return grafoDistancias

def knightlOnAChessboard(n):
    # Write your code here
    #print("funcion caballero!")
    resultTotal = []
    grafoInicial = grafo = {(0,0):[]}
    for movX in range(1,n):
        movListX = []
        for movY in range(1,n):
            grafoInicial = grafo = {(0,0):[]}
            grafoKnightL = GrafoKnightL(grafoInicial, movX, movY, n-1)
            #print("######################################################")
            #print("turno: ({},{})".format(movX,movY))
            #print(grafoKnightL)
            grafoDistancias = BreadthFirstSearch(grafoKnightL)
            #print("###GrafoDistancias: ")
            #print(grafoDistancias)
            #print("###Distancia: ")
            if (n-1,n-1) in grafoDistancias:
                #print(grafoDistancias[(n-1,n-1)])
                movListX.append(grafoDistancias[(n-1,n-1)])
            else: 
                #print("No existe el nodo: ({},{})".format(n-1,n-1))
                movListX.append(-1)
            #print("######################################################")
        resultTotal.append(movListX)
    return resultTotal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
