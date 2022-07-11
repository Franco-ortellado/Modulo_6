año=int(input("Ingrese año: "))

def bisiesto(año):
    if((año%4 == 0) and ((año%100 != 0) or (año%400 == 0))):
        return "Es bisiesto"
    else:
        return "No es bisiesto"

print("El año",año,bisiesto(año))