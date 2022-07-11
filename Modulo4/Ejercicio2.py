Num_Inicio = int(input("Introduce numero inicial: "))
Num_Fin = int(input ("introduce numero final: "))

print("Numeros impares entre ",Num_Inicio," y ",Num_Fin)

while Num_Inicio <= Num_Fin:
    if Num_Inicio % 2 != 0:
        print(Num_Inicio)
    Num_Inicio+=1 