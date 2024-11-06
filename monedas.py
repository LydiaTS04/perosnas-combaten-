class Monedas:
    def __init__(self,posicion_x=0,posicion_y=0): 
        self.posicion_x=posicion_x
        self.posicion_y=posicion_y
        self.posicion=posicion_x,posicion_y

    def __str__(self):
        return f"la moneda esta en posicion: {self.posicion}"