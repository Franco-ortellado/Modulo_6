from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def paridad (x):
    if x % 2 == 0:
        return True

def suma (a,b):
    return a+b

print (f"Numeros Pares:{list(filter(paridad,lista))}")
print(f"Suma de numeros pares:{reduce(suma,filter(paridad,lista))}")