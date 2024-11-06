#importamos elmentos de otras carpetas a estas 

from persona import Persona #de la carpeta persona, importamos la clase Persona
from espacio import Espacio
import utils
import random
from monedas import Monedas
import matplotlib.pyplot as plt


persona1=Persona("Lydia",2004,random.randint(-5,5),random.randint(-5,5))
print(persona1)

#añadimos a personas
persona2=Persona("Sevas",2001,random.randint(-5,5),random.randint(-5,5))
persona3=Persona("Alba",2004,random.randint(-5,5),random.randint(-5,5))
persona4=Persona("Alvaro",2004,random.randint(-5,5),random.randint(-5,5))

#añadimos espacios
espacio1= Espacio("UAX vilaneuva", 10,50 )
print (espacio1)
espacio2= Espacio("Albacete",40,20)
print (espacio2)

#añadimos la persona al espacio
espacio1.anadir_persona(persona2)
espacio1.anadir_persona(persona4)
espacio2.anadir_persona(persona3)

#contar personas
numero_personas1= utils.contar_personas_espacio(espacio1)
numero_personas2= utils.contar_personas_espacio(espacio2)

print(f"En {espacio1.nombre} hay {numero_personas1} personas")
print(f"En {espacio2.nombre} hay {numero_personas2} personas")

#distancia entre las personas 
distancia12= utils.calcular_distancia(persona1,persona2)
print("La distania entre", persona1.nombre,"con posicion",persona1.posicion,"es", persona2.nombre,"con posicion",persona2.posicion,"es", distancia12)

#creamos las monedas
monedas=[]
for i in range(1, 800):
    nueva_moneda=Monedas(random.randint(-10,10),random.randint(-10,10))
    monedas.append(nueva_moneda)
    #print(f"moneda {i} = {nueva_moneda}")


#asignar monedas a personas por turnos
turno=0
#comparamos la posicion de la moneda con la posicion de la persona
for moneda in monedas:
    turno += 1
    for persona in [persona1,persona2,persona3,persona4]:
        if moneda.posicion==persona.posicion:
             persona.monedas_ganadas += 1
             persona.turnos_monedas.append(persona.monedas_ganadas) #regristrar en que turno gano una moneda
             #print(f"{persona.nombre} tiene {persona.monedas_ganadas} monedas en su monedero")

#estado final de cada persona
for persona in [persona1,persona2,persona3,persona4]:
    print(f"{persona.nombre} finalizo con {persona.monedas_ganadas} monedas en su monedero")
    print(f"Turnos donde ganó monedas: {persona.turnos_monedas}\n")

#graficar monedas por turno,representa cómo cada persona va acumulando monedas a lo largo de los turnos
for persona in [persona1,persona2,persona3,persona4]:
    plt.plot(range(1, len(persona.turnos_monedas) + 1), persona.turnos_monedas, label=persona.nombre)

plt.xlabel("Turno")
plt.ylabel("Monedas ganadas")
plt.title("Monedas ganadas por turno")
plt.legend()
plt.show()

# Graficar la posición de las monedas y personajes

# Crear gráfico de dispersión con las monedas y las posiciones de las personas
plt.figure(figsize=(8, 8))

# Graficar posiciones de las monedas
monedas_x = [moneda.posicion[0] for moneda in monedas]
monedas_y = [moneda.posicion[1] for moneda in monedas]
plt.scatter(monedas_x, monedas_y, color='#FFd700', label='Monedas',s=150, alpha=0.8) #color amarillo fuerte #FFd700

# Graficar posiciones de las personas
colores = ['blue', 'red', 'green', 'purple']
personas = [persona1, persona2, persona3, persona4]

for i, persona in enumerate(personas):
    plt.scatter(persona.posicion[0], persona.posicion[1], color=colores[i], label=persona.nombre, s=50)

plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.title("Posición de monedas y personas")
plt.legend()
plt.grid(True)
plt.show()

# Simularemos que las personas se mueven aleatoriamente en cada turno y guardaremos su posición

# Definir cuántos turnos vamos a visualizar
num_turnos = 10  # por ejemplo, 10 turnos

# Crear una lista para registrar las posiciones de las personas en cada turno
posiciones_personas_por_turno = {persona.nombre: [] for persona in personas}

# Mover a las personas aleatoriamente en cada turno y registrar su posición
for turno in range(num_turnos):


    print(f"Turno {turno + 1}:")#regristamos su posicion para ver si coinciden con otra persona
    posiciones_ocupadas={}


    for persona in personas:
        # Movemos a la persona aleatoriamente
        nueva_posicion = (persona.posicion[0] + random.randint(-1, 1), persona.posicion[1] + random.randint(-1, 1))
        persona.posicion = nueva_posicion
        # Registramos la nueva posición
        posiciones_personas_por_turno[persona.nombre].append(nueva_posicion)


        # Verificamos si la posición ya está ocupada por otra persona
        if nueva_posicion in posiciones_ocupadas:
            otra_persona = posiciones_ocupadas[nueva_posicion]
            print(f"¡{persona.nombre} y {otra_persona.nombre} se encuentran en la misma posición {nueva_posicion}! Combaten a muerte.")
            # Aquí puedes decidir qué sucede en un "combate a muerte", por ejemplo, eliminar a uno
        else:
            # Si no está ocupada, añadimos la posición al diccionario
            posiciones_ocupadas[nueva_posicion] = persona
          

    print()  # Para dejar un espacio entre turnos

# Ahora graficamos las posiciones de las monedas y las trayectorias de las personas
plt.figure(figsize=(8, 8))

# Graficar posiciones de las monedas con un amarillo más fuerte y puntos más grandes
plt.scatter(monedas_x, monedas_y, color='#FFD700', label='Monedas', s=150, alpha=0.8)  # '#FFD700' es un amarillo fuerte

# Graficar las trayectorias de las personas a lo largo de los turnos
for i, persona in enumerate(personas):
    posiciones_x = [pos[0] for pos in posiciones_personas_por_turno[persona.nombre]]
    posiciones_y = [pos[1] for pos in posiciones_personas_por_turno[persona.nombre]]
    plt.plot(posiciones_x, posiciones_y, color=colores[i], label=persona.nombre, marker='o', markersize=5)

plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.title("Trayectorias de personas y posiciones de monedas (más visibles)")
plt.legend()
plt.grid(True)
plt.show()

