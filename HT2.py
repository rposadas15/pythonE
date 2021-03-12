contraseña = input("Ingrese una contraseña: ")
contraseña1 = input("Ingrese nuevamente la contraseña: ")

if contraseña == contraseña1:
    print("Bienvenido")
else:
    print("Contraseñas diferentes")

name = input("¿Cual es tu nombre? ")
genero = input("¿Cuál es tu genero (M o F)? ")
if genero == "M":
    if name.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if name.lower() > "f":
        grupo = "A"
    else:
        grupo = "B"
print("Perteneces al grupo " + grupo)