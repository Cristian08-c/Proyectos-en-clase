class vehiculo:
    def __init__(self, marca, modelo, año, velocidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = velocidad_actual
        
    def Acelerar(self):
        self.velocidad_actual +=10
        print(f"El vehiculo {self.modelo} ha incrementado su velocidad")
    
    def Frenar(self):
        self.velocidad_actual-=10
        print(f"El vehiculo {self.modelo} ha disminuido su velocidad")
        
        
    def mostrar_info(self):
        print("====DATOS DEL VEHICULO====")
        print(f"Marca:{self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Velocidad: {self.velocidad_actual}")

class Carro(vehiculo):
    def __init__(self, marca, modelo, año, velocidad_actual, num_puertas):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.num_puertas = num_puertas
        
    def mostrar_info(self):
        info =  super().mostrar_info()
        return (f"{info}, puertas:{self.num_puertas}")

class Moto(vehiculo):
    def __init__(self, marca, modelo, año, velocidad_actual, cilindraje):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.cilindraje = cilindraje
        
    def mostrar_info(self):
        info = super().mostrar_info()
        return (f"{info}, Cilindraje: {self.cilindraje} cc")

class Bicicleta(vehiculo):
    def __init__(self, marca, modelo, año, velocidad_actual, tipo):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.tipo = tipo
        
    def mostrar_info(self):
        info = super().mostrar_info()
        return(f"{info}, Tipo: {self.tipo}")

Vehiculos = []






        
        
    