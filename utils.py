
#modulo
def calcular_distancia(persona1,persona2):
    #raiz((persona1_x - persona2_x)^2 + (persona1_y - persona2_y)^2) Formula de distancia ecluidiana
    distancia = ((persona1.posicion_x-persona2.posicion_x)**2 + (persona1.posicion_y - persona2.posicion_y)**2)**0.5
    return distancia

def contar_personas_espacio(espacio):
    lista_personas=espacio.persona #[persona1,persona2,.....,personax]
    numero_personas= len(lista_personas) #len :contar cuantos elementos hay en una lista
    return numero_personas

