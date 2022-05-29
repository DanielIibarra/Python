from poo1 import prueba

class prueba2(prueba):

    puntos = 0

    def seis(self):
        self.puntos = self.puntos+6
        self.mas()
        print(self.nom,"Puntos",self.puntos)

s=prueba("Noe")
s.mas()
j=prueba2("jim")
j.mas()
j.seis()
print(dir(j))