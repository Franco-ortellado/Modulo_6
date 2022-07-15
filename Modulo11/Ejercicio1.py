import sqlite3

conn = sqlite3.connect("Ejercicio1.db")
cursor= conn.cursor()
cursor.execute("CREATE TABLE Alumnos(Id INT, nombre TEXT, apellido TEXT)")

cursor.execute("INSERT INTO Alumno VALUES(1, 'Juan', 'Lopez')")
cursor.execute("INSERT INTO Alumno VALUES(2,'Rogelio', 'Fernandez')")
cursor.execute("INSERT INTO Alumno VALUES(3,'Franco', 'Ortellado')")
cursor.execute("INSERT INTO Alumno VALUES(4,'Mercedes', 'Diaz')")
cursor.execute("INSERT INTO Alumno VALUES(5,'Juana', 'Olivera')")
cursor.execute("INSERT INTO Alumno VALUES(6,'Pedro', 'Gutierrez')")
cursor.execute("INSERT INTO Alumno VALUES(7,'Sofia', 'Guevara')")
cursor.execute("INSERT INTO Alumno VALUES(8,'Cristian', 'Fernandez')")

conn.commit()

rows = cursor.execute("SELECT * FROM Alumno WHERE nombre ='Juan'")

for row in rows:
    print(row)


conn.close()