import pickle

class Vehiculo():
    
    def __init__(self,color,puertas):
        self.puertas = puertas
        self.color = color
    
    def __str__(self):
        return f"color {self.color}, {self.puertas} puertas"

auto = Vehiculo("rojo",5)
print(auto)

f= open("vehiculo","wb")
pickle.dump(auto,f)
f.close()

