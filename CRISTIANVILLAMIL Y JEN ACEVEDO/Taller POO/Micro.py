#Equipo de micro, cada jugador puede hacer goles, el atributo de goles se debe poder incrementar, al finalizar el partido debe indicar cuantos goles hizo cada jugador
#Arquero, 2 laterales, un delantero, mediocentro
#Cada jugador debe tener un atributo individual
#El programa debe permitir ver quien hizo el gol y al final cuantos hizo
#Arquero debe indicar cuantos goles evito
#2 laterales deben mostrar cuantos jugadores han bloqueado
#El medio cuantos pases ha enviado
#El delantero cuantos tiros al arco ha hecho

class Equipo():
    def __init__(self, nombre, numero, posicion, energia ):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion
        self.energia = energia
        

        
    def descansar(self):
        if self.energia <= 0:
            self.energia +=20
            return (f"El jugador {self.nombre} ha descansado, energia restante: {self.energia}")
        else:
            return (f"El jugador {self.nombre} aun tiene energia para seguir jugando, agota su energia para poder descansar ")
        
    def pasar(self):
      while True:
        print("---Tipo de pase---")
        print("1. Pase largo")
        print("2. Pase corto")
        print("3. Pase aereo")
        print("4. salir")
        
       
        opc = int(input("Escoja un tipo de pase"))
        if opc == 1:
            self.energia -= 8
            return (f"El jugador ha hecho un pase largo, energia restante: {self.energia}")
        elif opc == 2:
            self.energia -= 5
            return(f"El jugador ha hecho un pase corto, energia restante:{self.energia} ")
        elif opc == 3:
            self.energia -=10
            return(f"El jugador ha hecho un pase aereo, energia restante:{self.energia}")
        elif opc == 4:
            print(f"El jugador no ha hecho ningun pase, energia restante: {self.energia}")
            break
        else:
            return(f"Seleccione un tipo de pase disponible")
        
class Arquero(Equipo):
    def __init__(self, nombre, numero, posicion, energia):
        super().__init__(nombre, numero, posicion, energia)
        self.tapados = 0
        self.tiros = 0
        self.goles = 0
        
    def presentarse(self):
        print(f"EL arquero {self.nombre} ha marcado {self.goles} goles usando su dorsal {self.numero}")
    
    def tapar(self, tapa = bool):
        if tapa and self.energia > 0:
            self.tapados +=1
            self.energia -=5
            return(f"El arquero {self.nombre} ha parado un disparo! energia restante: {self.energia}")
        elif tapa and self.energia <=0:
            return (f"El arquero {self.nombre} no tiene la energia suficiente para atajar el disparo")
        else:
            self.energia -=5
            return(f"El jugador no ha conseguido parar el gol, energia restante:{self.energia}")
    def disparo(self, gol = bool):
        if gol and self.energia > 0:
            self.tiros +=1
            self.goles +=1
            self.energia -=5
            return(f"El arquero {self.nombre} ha disparado al arco, marcando asi un gol, energia restante: {self.energia} ")
        
class Lateral(Equipo):
    def __init__(self, nombre, numero, posicion, energia):
        super().__init__(nombre, numero, posicion, energia)
        self.bloqueados = 0
        self.tiros = 0
        self.goles = 0
        
    def presentarse(self):
        print(f"El Lateral {self.nombre} ha marcado {self.goles} goles usando su dorsal {self.numero}")
                        
    def bloquear(self, bloquea = bool):
        if bloquea and self.energia >0:
            self.energia -=5
            return(f"El Lateral {self.nombre} ha bloqueado a un jugador, energia restante: {self.energia}")
        elif bloquea and self.energia <= 0:
            return(f"El Lateral {self.nombre} no tiene energia para bloquear al jugador")
        else:
            return(f"El Lateral {self.nombre} no puede bloquear al jugador")
    def disparo(self, gol = bool):
        if gol and self.energia > 0:
            self.tiros +=1
            self.goles +=1
            self.energia -=5
            return(f"El Lateral {self.nombre} ha disparado al arco, marcando asi un gol, energia restante: {self.energia} ")
class Armador(Equipo):
    def __init__(self, nombre, numero, posicion, energia):
        super().__init__(nombre, numero, posicion, energia)
        self.jugadas = 0
        self.tiros = 0
        self.goles = 0 
    def presentarse(self):
        print(f"El armador {self.nombre} ha marcado {self.goles} goles usando su dorsal {self.numero}")
    def jugada(self):
        if self.energia > 0:
            self.energia -=5
            self.jugadas +=1
            return(f"El Armador{self.nombre} ha realizado una jugada exitosa, energia restante: {self.energia}")
        else:
            return(f"El jugador no tiene energia suficiente para hacer una jugada")
    
    def pasar(self):
        return super().pasar()
    
    def disparo(self, gol = bool):
        if gol and self.energia > 0:
            self.tiros +=1
            self.goles +=1
            self.energia -=5
            return(f"El armador {self.nombre} ha disparado al arco, marcando asi un gol, energia restante: {self.energia} ")
class Delantero(Equipo):
    def __init__(self, nombre, numero, posicion, energia):
        super().__init__(nombre, numero, posicion, energia)
        self.tiros = 0
        self.goles = 0
    def presentarse(self):
        print(f"El delantero {self.nombre} ha marcado {self.goles} goles usando su dorsal {self.numero}")     
    def disparo(self, gol = bool):
        if gol and self.energia > 0:
            self.tiros +=1
            self.goles +=1
            self.energia -=5
            return(f"El jugador {self.nombre} ha disparado a la porteria y ha marcado {self.goles} gol, energia restante: {self.energia}")
        elif gol and self.energia <=0:
            self.tiros +=0
            self.goles += 0 
            return(f"El jugador no tiene la energia suficiente para hacer un disparo")
        
Arquero1 = Arquero("Estiven", 14, "Arquero", 100)
Lateral1 = Lateral("Daniel", 20, "Lateral", 100)
Lateral2 = Lateral("Jefferson", 18, "Lateral", 100)
Armador1 = Armador("Cristian", 12, "Armador", 100)
Delantero1 = Delantero("Miguel", 7, "Delantero", 100)

print(Arquero1.disparo())
print(Arquero1.tapar())
print(Lateral1.disparo())
print(Lateral1.disparo())
print(Lateral1.bloquear())
print(Lateral2.bloquear())
print(Armador1.disparo())
print(Armador1.jugada())
print(Delantero1.disparo())


print("====ESTADISTICAS DEL EQUIPO====")
print(Arquero1.presentarse())
print(Lateral1.presentarse())
print(Lateral2.presentarse())
print(Armador1.presentarse())
print(Delantero1.presentarse())
print("===============================")


                     

    
    
    

             
            
            
        