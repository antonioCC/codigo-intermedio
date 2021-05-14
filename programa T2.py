import re

archivo=open("datosx.txt","r")
mensaje=archivo.read()

lista = []
lista2 = []
lista3 =[]
m = 0
m1=0
var = ""

#patron = re.compile('(([A-Za-z]+\w?|\d{1,7})[\+|\-|\*|\/]([A-Za-z]+\w?|\d{1,7}))')# expresion regular
patron = re.compile('\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w')
a=str(mensaje)

for b in a:
	lista.append(b)


m1=0
#este ciclo verifica si la expresion tiene parentesis para poder guardar el triplo en una lista
for n in lista:
	if n == "*" or n == "/" or n == "+" or n == "-":
		if lista[m1-4]=="(" and lista[m1+4]==")":
			if lista[m1-2]!=" " and lista[m1+2]!=" ":
				var = "t"+str(m),"= ",a[m1-2],n,a[m1+2]
				m+=1
				lista2.append(var)
				lista[m1-4]=" "
				lista[m1-2]=" "
				lista[m1]=" "
				lista[m1+2]=" "
				lista[m1+4]=" "
	m1+=1

m1=0
n=None
#este ciclo es para verificar si entre la expresion se encuentra (* o /) para ponerlos primero en la lista
for n in a:
	if n == "*" or n == "/":
		if  lista[m1-2]!=" " and lista[m1+2]!=" ":
			var = "t"+str(m),"= ",a[m1-2],n,a[m1+2]
			m+=1
			lista2.append(var)
			lista[m1-2]=" "
			lista[m1]=" "
			lista[m1+2]=" "
	m1+=1

m1=0
#este ciclo con una serie de condiciones solo verifica si queda alguna expresion de un termino y un signo aritmetico
#para despues asignarle un temporal y formar el triplo (t0 + 3) con los signos (*/)
for c in lista:
	if re.match('[*/]',c) and lista[m1+2]==" " and lista[m1-2]!=" ":
		var = "t"+str(m),"= ",lista[m1-2],c,"t"+str(m-1)
		m+=1
		lista2.append(var)
		lista[m1-2]=" "
		lista[m1]=" "
	elif re.match('[*/]',c) and lista[m1-2]==" " and lista[m1+2]!=" ":
		var = "t"+str(m),"= ","t"+str(m-1),c,lista[m1+2]
		m+=1
		lista2.append(var)
		lista[m1]=" "
		lista[m1+2]=" "
	elif re.match('[*/]',c) and lista[m1-2]==" " and lista[m1+2]==" ":
		var = "t"+str(m),"= ","t"+str(m-2),c,"t"+str(m-1)
		m+=1
		lista2.append(var)
	m1+=1

m1=0
n=None
#este ciclo es para verificar si entre la expresion se encuentra (- o +) para ponerlos en la lista
for n in lista:
	if n == "+" or n == "-":
		if  lista[m1-2]!=" " and lista[m1+2]!=" ":
			var = "t"+str(m),"= ",a[m1-2],n,a[m1+2]
			m+=1
			lista2.append(var)
			lista[m1-2]=" "
			lista[m1]=" "
			lista[m1+2]=" "
	m1+=1


m1=0
#este ciclo con una serie de condiciones solo verifica si queda alguna expresion de un termino y un signo aritmetico
#para despues asignarle un temporal y formar el triplo (t0 + 3) pero con los signos (+-)
for c in lista:
	if re.match('[+-]',c) and lista[m1+2]==" " and lista[m1-2]!=" ":
		var = "t"+str(m),"= ",lista[m1-2],c,"t"+str(m-1)
		m+=1
		lista2.append(var)
		lista[m1-2]=" "
		lista[m1]=" "
	elif re.match('[+-]',c) and lista[m1-2]==" " and lista[m1+2]!=" ":
		var = "t"+str(m),"= ","t"+str(m-1),c,lista[m1+2]
		m+=1
		lista2.append(var)
		lista[m1]=" "
		lista[m1+2]=" "
	elif re.match('[+-]',c) and lista[m1-2]==" " and lista[m1+2]==" ":
		var = "t"+str(m),"= ","t"+str(m-2),c,"t"+str(m-1)
		m+=1
		lista2.append(var)
	m1+=1


d=None
#imprime la lista 2 donde se guardaron los triplos
for d in lista2:
	print(d)

archivo.close()




