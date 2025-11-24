class Senku:
    def __init__(self, nombre, aldea, edad ):
        self.nombre = nombre
        self. aldea = aldea
        self.edad = edad
        
    def presentacion(self):
        print(f"Hola, mi nombre es {self.nombre} de la {self.aldea} en el nuevo mundo de piedra, soy un cientifico del viejo mundo, tenia {self.edad} antes de la petrificacion")
    
    def experimentar(self):
        print(f"Yo, {self.nombre} estoy realizando un nuevo experimento...")
    
    def crear_invento(self):
        print(f"{self.nombre} acaba de crear un invento usando el poder de la ciencia!")
    
    def descansar(self):
        print(f"{self.nombre} esta descansando para descansar su mente")
        
senku1 = Senku("Senku Ishigami", "Aldea ishigami", 18)

senku1.presentacion()
senku1.experimentar()
senku1.crear_invento()
senku1.descansar()
    

