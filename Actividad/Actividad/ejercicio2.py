class vehiculo:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad
        
    def arrancar(self):
        print(f"El {self.marca} esta arrancando!!")
        
    def frenar(self):
        print(f"El {self.marca} se ha detenido.")
        
    def mostrar_info(self):
        print(f"Marca:{self.marca}, color:{self.color}, velocidad:{self.velocidad}km/h")
    
carro1 = vehiculo("Ferrari", "Rojo",100 )

carro1.mostrar_info()
carro1.arrancar()
carro1.frenar()