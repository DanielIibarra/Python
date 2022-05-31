import sqlite3

dato = sqlite3.connect("tabla.sqlite")
cur  = dato.cursor()

cur.execute("DROP TABLE IF EXISTS Correos")
cur.execute("CREATE TABLE Correos (correo TEXT,nada TEXT)")

file = open("mbox-short.txt")

for line in file:
    if not line.startswith("From: "): continue
    line = line.split()
    correo = line[1]
    cur.execute("INSERT INTO Correos (correo,nada) VALUES(?,0)",(correo,))
    
dato.commit()

cur.execute("SELECT correo,nada FROM Correos")
for line1 in cur:
    print(line1)