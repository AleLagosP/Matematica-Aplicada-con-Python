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

# 2) Respuesta de: Si se sabe que el metro se demora 1,2 minutos en llegar desde una estación a otra y espera 30 segundos en cada estación, indique el dominio contextualizado para f(t).
#Datos del caso:
# Son 9 estaciones, por lo que el tiempo total del metro es de (9 * 1.2) + (9 * 0.5) minutos.
# Se demora 1.2 minutos en llegar de una estación a otra 
# espera 30 segundos en cada estación.

tiempo_total_metro = (9 * 1.2) + (9 * 0.5)
print("Tiempo total del metro:", tiempo_total_metro, "minutos")

# 3) Respuesta de: Mediante análisis gráfico, indique cuál medio de transporte es más conveniente en términos de tiempo, para el turista. Justifique.

# El medio de transporte más conveniente en términos de tiempo para el turista es el metro, ya que recorre una mayor distancia en menos tiempo en comparación con el bus. 
# Esto se puede observar en el gráfico, donde la pendiente de la línea del metro es más pronunciada que la del bus, indicando que el metro avanza más rápido a lo largo del tiempo.

# 4) Respuesta de: Si se sabe que desde estación La Moneda hasta Tobalaba son aproximadamente 6 kilómetros ¿cuántos tiempo tardará el turista en llegar a su destino con cada una de las opciones?
#Datos del caso:
# La distancia entre La Moneda y Tobalaba es de 6 kilómetros.
# Para el metro, la velocidad es de 0.4 km/h.

tiempo_metro_6km = 6 / 0.4
print("Tiempo que tardará el turista en llegar a su destino con el metro:", tiempo_metro_6km, "horas")


#-----
# Problema 6 - Respuesta:
# datos del problema:
# variable dependiente : T(t) = temperatura del servidor en C°
# Variable independiente : t = tiempo transcurrido desde las 08:00 horas

# 1) Agregando un grafico de la funcion, indicando el dominio contextuado:
import numpy as np
import matplotlib.pyplot as plt

inicio = 0
final = 9

def temperatura(t):
    return -0.5 * t**2 + 3 * t + 20

tiempos = np.linspace(0, 9, 100)
temperaturas = temperatura(tiempos)

plt.plot(tiempos, temperaturas)
plt.xlabel("Tiempo (horas)")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura del Servidor - Problema 6")
plt.grid()
plt.show()

# 2) Respuesta de:  Mediante un análisis gráfico, estime cuándo el servidor alcanza la máxima temperatura y calcule cuánto es.
a = -0.5 
b = 3

tiempo_maximo = -b / (2 * a)
temperatura_maxima = temperatura(tiempo_maximo)

print("Temperatura maxima", temperatura_maxima, "°C")
print("Ocurre", tiempo_maximo, "Hora despues de la 08:00 hrs")

# 3) Respuesta de : Determine la temperatura del servidor a las 13:00 horas y al finalizar la jornada laboral.
# Vamos a determinar el transcurso de las 13 hrs y la temperatura que tiene:
temp_13 = temperatura(5)
print("Tenemos a las 13:00: ", temp_13, "°C")

# tambien vamos a determinar el trascurso de 9 hrs (17:00) y la temperatura que tiene:
temp_17 = temperatura(9)
print("Tenemos a las 17:00: ", temp_17, "°C")
