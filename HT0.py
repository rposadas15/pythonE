masa = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu Estatura en m: "))
indice = float((masa / altura**2))
print(f"Tu indice de masa corporal es: {round(indice, 2)}")