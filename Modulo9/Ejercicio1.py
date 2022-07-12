a = input("Ingrese Paises: ")

paises = [pais for pais in a.split(",")]

print(", ".join(sorted(list(set(paises)))))