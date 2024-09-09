print("Manejo de funciones")
def hola_mundo():
    print("Hola, estoy dentro de la funcion")

def Mensa(msg):
    print(msg)
def EscribeNC(Nombre, Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre complesto es: {Nombre} {Apellido}")
def suma2numero(n1, n2):
    s=n1+n2
    return f"La suma de {n1} + {n2} es igual a: ", s
#Llamando a la funcion
hola_mundo()
Mensa("hola whatsapp") #Llama a la funcion mensa con 1 parámetro
Mensa("El profe sorprendio enviando mensajes") #Llama a mensaje
EscribeNC("emiii", ".dss")
print("Funciones que regresan valores")
print(suma2numero(69, 13))
print(suma2numero(-1, 1))
