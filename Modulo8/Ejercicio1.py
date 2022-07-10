f = open("Ejercicio.txt","w")
f.write("escribiendo el archivo\n")
f.close()

f = open("Ejercicio.txt","a")
f.write("Escribiendo el archivo otra vez")
f.close()