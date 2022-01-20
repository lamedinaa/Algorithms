def pruebaContinue():
    lista = [1,2,3,4,5,6]
    while lista:
        print(lista)
        number = lista.pop(0)
        if number%2 == 0:
            continue
        print("impar")

def creandoGeneradores(): 
    for i in (n**2 for n in [1,2,3,4,5]):
        print(i)

def miGenerador(n,m,s):
    while(n<m):
        yield n
        n += s

def cuadrado(n):
    return n**2

if __name__ ==  "__main__":
    lista = [1,2,3,4,5,6,8]
    lista2 = [10,20,30,40,50,60,80]
    print("///////////FUNCIÓN MAP")
    listacuadrados = list(map(cuadrado,lista))                               ### map devuelve un objeto map por eso se debe volver lista
    listacuadrados2 = list(map(cuadrado,lista2))                             ### map devuelve un objeto map por eso se debe volver lista
    print("listacuadrados: %s "%listacuadrados)
    print("listacuadrados2: %s "%listacuadrados2)
    ###TAMBIÉN PUEDO CON FUNCIONES LAMBDA
    listacuadrados = list(map(lambda n : n**2,lista))
    print("listacuadradaos lambda: %s"%listacuadrados)
    listapares = list(filter(lambda n : n%2 == 0 ,listacuadrados))
    print("listapares: %s "%listapares)

    print("////////////COMPRESIÓN DE LISTAS")
    l2 = [ n**2 for n in lista]
    print("l2: %s"%l2)
    l2 = [ n**2 for n in lista if n%2 == 0]
    print("l2: %s"%l2)
    listaxlista2 = [ l1*l2 for l1 in lista for l2 in lista2]
    print("lista*lista1: {0}".format(listaxlista2))
    listaxlista2 = [ l1*l2 for l1 in lista for l2 in lista2 if l1 >3]
    print("lista*lista1: {0}".format(listaxlista2))
    print("///////////////////////generadores:")
    creandoGeneradores()
    print("usundo la función mi generador: ")
    for i in miGenerador(0,10,2):
        print(i)


    





