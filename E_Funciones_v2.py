print(" ")
print("Funciones creadas por el usuario")
#Las funciones

print("Funciones usando Listas")
def Mi_lista():
    amigos=["Larro", "Pao", "Edgar", "Cesar"]
    for emi in amigos:
        print(emi)
Mi_lista()
print(" ")
 
print("Funciones usando Conjuntos")
def Mi_conjunto():
    carros=["Challenger", "Camaro", "Mustang"]
    for x in carros:
        print(x)
Mi_conjunto()

print(" ")

print("Funciones usando Tuplas")
def Mis_tuplas():
    arcoiris=("azul", "verde", "rojo", "morado")
    for y in arcoiris:
        print(y)
Mis_tuplas()

print(" ")

print("Funciones usando Diccionarios")
def Mi_diccionario():
    carros2 = {
    "chevrolet": "Camaro",
    "Ford": "Mustang",
    "Dodge": "Challenger"}

    for f in carros2:
     print(f)
Mi_diccionario()
