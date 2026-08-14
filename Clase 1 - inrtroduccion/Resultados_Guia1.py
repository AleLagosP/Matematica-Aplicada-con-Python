# Resultado guia 1 10/08/2026
#-----
# Problema 1 - Respuesta 1:
def datos_transmitidos(segundos):
    velocidad = 100 
    return velocidad * segundos;

#Caso 1
Caso1 = datos_transmitidos(45) #45 segundos 
print("45 segundos :", Caso1, "bits");

#Caso 2
Caso2 = datos_transmitidos(1.5 * 60) #1,5 minutos
print("1,5 minutos :", Caso2, "bits");

#Caso 3
Caso3 = datos_transmitidos(60 * 60) #1 hora
print("1 hora :", Caso3, "bits");

#-----

# Problema 2 - Respuesta 2:
def datos_transmitidos2(segundos):
    
    velocidad = 100
    return velocidad * segundos;

for tiempo in [0, 100, 1000]:
    resultado = datos_transmitidos2(tiempo)
    print(f"{tiempo} segundos: {resultado} bits")

range(0, 100, 1000);

#-----

# Problema 3 - Respuesta 3:
def calcular_latencia(latencia_estimada):
    latencia_real = latencia_estimada * 1.20
    return latencia_real

a = calcular_latencia(200) #Milisegundos del primer caso
b = calcular_latencia(149) #Milisegundos del segundo caso
c = calcular_latencia(74) #Milisegundos del tercer caso

#La calculadora de latencia real es:
print("Latencia real del primer caso:", a, "ms")
print("Latencia real del segundo caso:", b, "ms")
print("Latencia real del tercer caso:", c, "ms")

#-----

# Problema 4 - Respuesta 4:
# 1) Determinando la longitud del cable en metros, sabiendo que la velocidad de propagación es de 1.85 m/s y el tiempo de propagación es de 100 segundos.
def largo_cable(tiempo):
    return 1.85 * tiempo

print(largo_cable(100)) #100 segundos

# 2) Definicion variable dependiente e independiente, indicando unidad de medida.

# la variable independiente es el tiempo de propagacion, medido en segundos.
    # T= tiempo de hora 
# la variable dependiente es el largo del cable, medido en metros.
    # L(t) = kilometros de cable instalado 

# 3) Determinando el dominio contextuado de la funcion

# Tenemos : 6600 = 1.85 * t

# Despejando t, tenemos que t = 6600 / 1.85

# Resultado: t = 3567.567 segundos

# El dominio es : 0 <= t <= 3567.567 segundos

# 4) Grafico de la funcion, indicando el dominio contextuado
import matplotlib.pyplot as plt 
def largo_cable(tiempo):    
    return 1.85 * tiempo

tiempo_final = 6600 / 1.85

horas = []
kilometros = []

for t in range(0, int(tiempo_final) + 1):
    horas.append(t)
    kilometros.append(largo_cable(t))

plt.plot(horas, kilometros)
plt.xlabel("Tiempo (horas)")
plt.ylabel("Cable instalado (km)")
plt.title("Instalación del cable de fibra óptica problema 4 resultado")
plt.grid()
plt.show()

# 5) respuesta de ¿Cuántos metros de cable se instalaron al transcurrir 148 horas? ¿Y transcurridas 2.300 horas?
cable_148 = largo_cable(148)
cable_2300 = largo_cable(2300)

print("Metros de cable instalados en 148 horas:", cable_148 * 1000, "metros")
print("Metros de cable instalados en 2.300 horas:", cable_2300 * 1000, "metros")

# 6) Respuesta de: Si se han instalado 3.480 kilometros de cable, ¿cuántas horas llevan de trabajo?
tiempo_trabajo = 3480 / 1.85

print("Para instalar 3480 km:", round(tiempo_trabajo, 2), "horas")

# 7) Respuesta de: ¿Cuánto tiempo transcurrió para que se completara la obra?
print("Tiempo transcurrido para completar la obra:", round(tiempo_final, 2), "horas")

#-----

# Problema 5 - Respuesta 5:
#  Datos del caso:
# F(t) = 0.4t Metro
# G(t) = 0.3 Bus

# 1) determinar gafico de la funcion, indicando el dominio contextuado
import matplotlib.pyplot as plt
def metro(t):
    return 0.4 * t

def bus(t):
    return 0.3 * t

tiempo = range(0, 31)

distancia_metro = [] 
distancia_bus = [] 

for t in tiempo: 
    distancia_metro.append(metro(t))
    distancia_bus.append(bus(t))

plt.plot(tiempo, distancia_metro, label="Metro")
plt.plot(tiempo, distancia_bus, label="Bus")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Distancia (km)")
plt.title("Comparación de Distancia Recorrida -  Grafico Problema 5")
plt.legend()
plt.grid()
plt.show()
