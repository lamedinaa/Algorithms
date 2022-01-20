import sys

def rotLeft(a, d):
    n = len(a)
    if n == d or n == 0: 
        return a
    if n%d == 0:
        start = True
        multiple = n/d
        for m in range(0,d):
            c = a[m]
            for k in range(0,int(multiple)+1):
                k1 = multiple - k
                i =int( (n - (m+d*(k1)) )%n )
                j = int( (n - (m+d*(k1-1)) )%n )
                b = a[j]
                a[j] = c
                c = b
                
        return a
    else:
        start = True
        i = n - 1
        c = a[i]
        while start:
            i = (i-d)%n
            b = a[i]
            a[i] = c
            c = b
            if i == (n-1):
                start = False
    return a




if __name__=="__main__":
    a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    c = rotLeft(a,10)
    print(c)


    