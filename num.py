num = int(input("Ingresa un número, N: "))
aux = 0

for i in range(1, num+1):
    cubo = i**3
    impares = range(aux+1, aux+(i*2)+1, 2)
    aux = aux + (i*2)
    print("{} = {} al cubo = {}".format(cubo, i, "+".join(map(str, impares))))