import sqlite3

from numpy import insert

date = sqlite3.connect("nuevo.sqlite")
cur = date.cursor()

#cur.execute("CREATE TABLE Prueba (Nombre TEXT,Años INTEGER)")
cur.execute("INSERT INTO Prueba (Nombre,Años) VALUES (?,?)",("Noe Daniel",23))
date.commit()

print("Nombre")
cur.execute("SELECT nombre,años FROM Prueba")
for line in cur:
    print(line)

#cur.execute("DELETE FROM Prueba WHERE Años<100")
date.commit()

cur.close()