

class Persona:
    def __init__(self,nombre,año,posicion_x=0,posicion_y=0): #atributos  #init sirve para poner los atributos en Persona() al final
        self.nombre=nombre                          #[ ] es una lista
        self.año=año
        self.posicion_x=posicion_x
        self.posicion_y=posicion_y
        self.posicion=posicion_x,posicion_y
        self.monedas_ganadas=0
        self.turnos_monedas=[] #para regristar monedas en cada turno
      
        
    def __str__(self): #represenatcion astring de un objeto, va ser lo q va a pintar cuando haga print de un objeto
        return f"Nombre: {self.nombre} | año nacimiento: {self.año} | posicion: {self.posicion_x,self.posicion_y} " #se puede hacer con string tambien
        
    