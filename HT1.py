print("EJERCICIO 1: ")
n = int(input("Introduzca un numero entero: "))
for i in range(n+1):
    print("*"*i)

print("EJERCICIO 2: ")
n1 = int(input("Introduzca un numero entero: "))

for i in range(n1):
    print(i)

print("EJERCICIO 3: ")
n2 = int(input("Introduzca un numero entero: "))
divisor = 2
while n2 > divisor:
    if n2 % divisor == 0:
        print("El numero no es primo")
        break
    elif n2 % divisor != 0:
        divisor += 1

if n2 == divisor:
    print("El numero si es primo")