class Espacio:

    def __init__(self,nombre,largo=10,ancho=0):

        self.nombre=nombre
        self.persona=[] #lista vacia
        self.largo=largo
        self.ancho=ancho

    def anadir_persona(self,persona): #metodo que añade algo
        self.persona.append(persona) #append lo ponemos pq persona es una lista

        print(f"He añadido a {persona} al espacio {self.nombre}")

    def __str__(self): #represenatcion astring de un objeto, va ser lo q va a pintar cuando haga print de un objeto
        return f"Este espacio es: {self.nombre} y mide {self.largo} metros por {self.ancho} metros" #se puede hacer asi o con string normal