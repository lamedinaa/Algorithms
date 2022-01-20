#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/submissions/code/1334694752
import sys

def sumaDefinitiva(n):
    if n%3 == 0: 
        div3 = int((n//3) - 1)
    else:
        div3 = int(n//3)

    if n%5 == 0: 
        div5 = int((n//5) - 1)
    else:
        div5 = int(n//5)

    if n%15 == 0: 
        div15 = int((n//15) -1)
    else:
        div15 = int(n//15)

    sumMultiples3 = 3*((div3*(div3 +1))/2)
    sumMultiples5 = 5*((div5*(div5 +1))/2)
    sumMultiples15 = 15*((div15 *(div15  +1))/2)
    sum = int(sumMultiples3+sumMultiples5-sumMultiples15)

    print(sum)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    sumaDefinitiva(n)
    
    