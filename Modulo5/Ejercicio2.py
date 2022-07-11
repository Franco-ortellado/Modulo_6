def primo(num):
    contador = 1
    for i in range(1,num):
        if num%i == 0:
            contador+=1
    if contador == 2:
        return "Es Primo"
    elif contador > 2:
        return "No es Primo"

numero = int(input("Ingresa un numero entero: "))
print(primo(numero))