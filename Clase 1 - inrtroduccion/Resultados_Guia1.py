# Resultado guia 1 10/08/2026

# Respuesta 1:
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


# Respuesta 2:
def datos_transmitidos2(segundos):
    
    velocidad = 100
    return velocidad * segundos;

for tiempo in [0, 100, 1000]:
    resultado = datos_transmitidos2(tiempo)
    print(f"{tiempo} segundos: {resultado} bits")

range(0, 100, 1000);

# Respuesta 3:
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

#Respuesta 4:
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
plt.title("Instalación del cable de fibra óptica")
plt.grid()
plt.show()



