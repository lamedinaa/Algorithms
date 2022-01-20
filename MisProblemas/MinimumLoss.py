#https://www.hackerrank.com/challenges/minimum-loss/submissions/code/211356659
#!/bin/python

import math
import os
import random
import re
import sys


def tomarElemento(elemento):
    return elemento[0]

def minimumLoss(price):
    lista = []
    for i in range(len(price)):
         lista.append((price[i], i))


    listaorganizada = sorted(lista,key=tomarElemento,reverse=True)


    loss = float("inf")
    for i in range(len(listaorganizada)-1):
        if listaorganizada[i][1]<listaorganizada[i+1][1]:
            loss = min(loss,listaorganizada[i][0]-listaorganizada[i+1][0])
    return loss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    price = map(long, raw_input().rstrip().split())
    
    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()


