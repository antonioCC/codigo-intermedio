import re

archivo=open("datosx.txt","r")
mensaje=archivo.read()

#se inician las list yvariables a utilizar
lista = []
lista2 = []
lista3 =[]
m = 0
m1=0
var = ""


#patron = re.compile('\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w')
a=str(mensaje)#se guarda en a lo que hay en el txt

#ciclo for para pasar cada elemento de a en lista
for b in a:
	lista.append(b)

#ciclo for para verificar si encontro un [+-/*], si lo encuentra verifica que su sucesor y antecesor no esten vacios
#para poder asignar a var el triplo, ingresarlo en lista2 y al final quita los elementos que tomo de lista
for n in a:
	if n == "*" or n == "/" or n == "+" or n == "-":
		if  lista[m1-2]!=" " and lista[m1+2]!=" ":
				var = "t"+str(m),"= ",a[m1-2],n,a[m1+2]
				m+=1
				lista2.append(var)
				lista.remove(a[m1-2])
				lista.remove(n)
				lista.remove(a[m1+2])
	m1+=1
	#print(m1,n)

#en este ciclo verifica si los elementos que quedan cumplen las condiciones para relizar un ultimo triplo usando el triplo anterior
#para luego remover tambien los elentos que tomo
m1=0
for c in lista:
	if re.match('[+*-/]',c) and lista[m1+2]==" ":
		var = "t"+str(m),"= ",lista[m1-2],c,"t"+str(m-1)
		lista2.append(var)
		lista.remove(lista[m1-2])
		lista.remove(c)
	elif re.match('[+*-/]',c) and lista[m1-2]==" ":
		var = "t"+str(m),"= ",lista[m1+2],c,"t"+str(m-1)
		lista2.append(var)
		lista.remove(c)
		lista.remove(lista[m1+1])
	m1+=1

#imprime los elementos de lista2
d=None
for d in lista2:
	print(d)

archivo.close()




