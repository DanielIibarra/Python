class prueba:
    x=0
    nom=""

    def __init__(self,nombre):
        self.nom=nombre
        print("Variable iniciada por",self.nom)
    
    def mas(self):
        self.x=self.x+1
        print("Numero:",self.x)