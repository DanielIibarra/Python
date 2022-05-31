import sqlite3

file = sqlite3.connect("sql1.sqlite")
cur = file.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (email TEXT,count INTEGER)")

fname= input("Archivo a buscar: ")
if len(fname)<1: 
    fname="mbox-short.txt"
data=open(fname)
for line in data:
    if not line.startswith("From: "): continue
    pieza = line.split()
    email = pieza[1]
    cur.execute("SELECT count FROM Counts WHERE email=?",(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (email,count) VALUES(?,1)",(email,))
    else:
        cur.execute("UPDATE Counts SET count=count + 1 WHERE email=?",(email,))
    file.commit()

sqlstr = "SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10"
for line1 in file.execute(sqlstr):
    print(line1)

