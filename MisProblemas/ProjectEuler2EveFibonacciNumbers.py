#!/bin/python

import sys
 
def evenfib2(N):
    fibn2 = 0 
    fibn1 = 2
    if N == 0:
        return 0 
    elif N== 1:
        return 2
    for i in range(1,N):
        f = 4*fibn1+ fibn2
        fibn2 = fibn1
        fibn1 = f 
    return f

def sumEvenFibBound2(N):
    sum = 0
    count = 0
    even = evenfib2(0)
    while even <= N:
        sum += even
        count += 1 
        even = evenfib2(count)
    return sum


    

    
t = int(raw_input().strip())

for a0 in xrange(t):
    n = long(raw_input().strip())
    print(sumEvenFibBound2(n))                                                                                      