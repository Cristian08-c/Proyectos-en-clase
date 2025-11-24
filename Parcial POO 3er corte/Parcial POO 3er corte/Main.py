from Vehiculos import Vehiculos, Moto, Carro, Bicicleta

Carro1 = Carro("Toyota", "Corolla Cross", 2022, 0, 4)
Carro2 = Carro("Chevrolet", "Onix", 2021, 0 ,4 )

Moto1 = Moto("Yamaha", "NMAX 155", 2023 , 0 , 155)
Moto2 = Moto("AKT", "AK125NKD,", 2024, 0 , 125)

Bicicleta1 = Bicicleta("Trek", "Marlin 7", 2022, 0, "Montaña")
Bicicleta2 = Bicicleta("Giant", "Escape 3", 2023, 0, "Urbana/Ciudad")

Vehiculos.append(Carro1)
Vehiculos.append(Carro2)
Vehiculos.append(Moto1)
Vehiculos.append(Moto2)
Vehiculos.append(Bicicleta1)
Vehiculos.append(Bicicleta2)

Carro1.Acelerar()
Carro2.Acelerar()

Moto1.Frenar()
Moto2.Frenar()

Bicicleta1.Acelerar()
Bicicleta2.Acelerar()

#print("LISTA DE VEHICULOS")
#for Vehiculo in Vehiculos:
    #print(Vehiculo.mostrar_info())