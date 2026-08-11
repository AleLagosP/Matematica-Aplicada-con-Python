# Resultado guia 1 10/08/2026

# Respuesta 1:
def datos_transmitidos(segundos ):
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

