class Alumno:
    def _inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print ("NOMBRE:",self.nombre)
        print("NOTA:",self.nota)

    def resultado_nota(self):
        if self.nota >= 7:
            print(self.nombre,"Aprobo")
        else:
            print(self.nombre,"No Aprobo")

alumno = Alumno()
alumno._inicializar("Pepe",8)
alumno.imprimir()
alumno.resultado_nota()