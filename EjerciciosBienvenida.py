import math

#Ejercicio1

def parImpar():
	num=(int(input("Por favor indique un número: ")))
	if num % 2 == 0:
		print("El numero es par")
		numPar=(num+num)
		print(numPar)
	else:
		print("El número es impar")
		numImpar=(num*num)
		print(numImpar)


#Ejercicio2

def nPrimos():
	
	a=int(2)

	num=int(input("Por favor indique un número: "))

	for x in range(1, num+1):
		b=False
		while(b==False):

			c=int(2)
			bandera=True

			while((bandera==True) and (c<a)):

				if(a % c == 0):
					bandera =False
				else:
					c = c+1;

			if(bandera==True):
				print(a)
				b=True;

			a=a+1;


#Ejercicio3

def palindromo():
	cadena = (input("Por favor indique la palabra o la frase: "))
	cadena = cadena.lower()
	cadena = cadena.replace(" ", "")
	longitud = len(cadena)
	
	if longitud % 2 == 0:
			inicio = cadena[:longitud // 2]
			final = cadena[longitud // 2:]

	else:
			inicio = cadena[:longitud//2]
			final = cadena[longitud // 2+1:]

	if inicio == final[::-1]:
		print("Es palindroma")
	else:
		print("No es palindroma")


#Ejercicio4

def potencia():
	N=int(input("Por favor ingrese un numero: "))
	a=1
	while a<N:
		a=a*2
	print(a==N)


#Ejercicio5

def ejCadena():
	
	cadena=[]
	for x in range(0, 5):
		cad=(input("Ingrese la primera cadena/caracter: "))
		cadena.append(cad)
		cadena.sort()

	print(cadena)

#Ejercicio 6

def polidivisible():
	count=0
	num=(int(input("Por favor indique un número: ")))
	num2=0
	num3=num

	while num>0:
			count=count+1
			num=num//10
	print("El número de digitos: ", count)

	if num3 != 0:
		if num3>=10:
			num2=num3
			while num2>=100:
				num2=num2//count

	else:
		print("No es polidivisible")

	while count>=2:
				if num3%count==0:
					print("Si es polidivisible")
					break
				else:
					print("No es polidivisible")
					break
	
					
#Ejercicio7

def fibonacci():

	n=(int(input("Ingrese un numero entero")))
	a=0
	b=1
	for x in range(n):
		print(a)	
		c=a+b
		a=b
		b=c
	

#Ejercicio8

def backwards():

	cadena=(input("Ingrese una cadena de caracteres:"))
	print(cadena)
	cadenaInv=cadena[::-1]

	print(cadenaInv+"lol")

print("----------------------------------------------------------")
print("Ejercicio1")
parImpar()
print("----------------------------------------------------------")
print("Ejercicio2")
nPrimos()
print("----------------------------------------------------------")
print("Ejercicio3")
palindromo()
print("----------------------------------------------------------")
print("Ejercicio4")
potencia()
print("----------------------------------------------------------")
print("Ejercicio5")
ejCadena()
print("----------------------------------------------------------")
print("Ejercicio6")
polidivisible()
print("----------------------------------------------------------")
print("Ejercicio7")
fibonacci()
print("----------------------------------------------------------")
print("Ejercicio8")
backwards()
print("----------------------------------------------------------")

