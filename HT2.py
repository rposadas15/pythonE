contraseña = input("Ingrese una contraseña: ")
contraseña1 = input("Ingrese nuevamente la contraseña: ")

if contraseña == contraseña1:
    print("Bienvenido")
else:
    print("Contraseñas diferentes")

nombre = input("¿Cual es tu nombre? ")
genero = input("¿Cuál es tu genero (M o F)? ")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "f":
        grupo = "A"
    else:
        grupo = "B"
print("Perteneces al grupo " + grupo)