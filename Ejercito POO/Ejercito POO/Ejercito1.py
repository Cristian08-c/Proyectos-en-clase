class MiembroEjercito:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        
    def presentarse(self):
        print(f"Soy {self.nombre}, rango: {self.rango} del ejercito.")

class Soldado(MiembroEjercito):
    def __init__(self, nombre, rango):
        super().__init__(nombre, rango)
    
    def entrenar(self):
        print(f"El soldado {self.nombre} esta entrenando para su proxima mision")

class Medico(MiembroEjercito):
    def __init__(self, nombre, rango):
        super().__init__(nombre, rango)
        
    def curar(self):
        print(f"El medico {self.nombre} esta sanando las heridas de sus compañeros")

class Ingeniero(MiembroEjercito):
    def __init__(self, nombre, rango):
        super().__init__(nombre, rango)
        
    def reparar(self):
        print(f"El ingeniero {self.nombre} ha reparado el equipo")

soldado1 = Soldado("Ramirez", "Cabo")
medico1 = Medico("Robles", "Teniente")
ingeniero1 = Ingeniero("Villamil", "Tecnico Primero")

soldado1.presentarse()
medico1.presentarse()
ingeniero1.presentarse()

print("Acciones")
soldado1.entrenar()
medico1.curar()
ingeniero1.reparar()


