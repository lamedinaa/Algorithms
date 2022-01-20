import sys

def listas_practice():
    a = [1,2,3,4,5]
    print("lista principal %s" % a)
    print("a[::]  %s"%a[::])
    print("a[::1] %s"%a[::1])
    print("a[::2] %s"%a[::2])
    print("a[::3] %s"%a[::3])
    print("a[1:]  %s"%a[1:])
    print("a[:2]  %s"%a[:2])
    print("a[::-1]  %s"%a[::])
    print("a[-1] %s "%a[-1])
    print("a/b %s"%(9//3))




if __name__ == "__main__":
    # print(sys.maxsize)
    # print(float("inf"))
    # print(2<float("inf"))
    # print(type(float("inf")))
    # print(float("inf")/2)
    # print(type(sys.maxsize))
    # print(sys.maxsize<float("inf"))

    print(10/5)
    for i in range(5,1):
        print(i)



####################ITERACIONES SOBRE LISTAS
def cuadrado(n):
    return n ** 2

l = [1, 2, 3]
l2 = map(cuadrado, l)


def es_par(n):
    return (n % 2.0 == 0)

l2 = filter(es_par, l)
l2 = filter(lambda n : n%2 ==0, l)    ###uso de la funcion lambda


import functools
def sumar(x, y):
    return x + y

l = [1, 2, 3]
l2 = functools.reduce(sumar, l)