class Cristian:
    def __init__(self, nombre, ocupacion, carrera, altura):
        self.nombre = nombre
        self.ocupacion = ocupacion 
        self.carrera = carrera
        self.altura = altura
        
    def mostrar(self):
        print(f"{self.nombre} dice: soy un {self.ocupacion}, mi carrera es {self.carrera} y mido {self.altura}")
        
persona1 = Cristian("Cristian", "estudiante", "Ing informatica", 1.70)

persona1.mostrar()

   