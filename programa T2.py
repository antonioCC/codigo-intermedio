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

#lista.append(mensaje)
#a=a.strip("[").strip("]")
#c=c.replace("e","a")
#lista.remove("5")
m1=0
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

m1=0
for c in lista:
	if re.match('[+*-/]',c) and lista[m1+2]==" ":
		#print(m1,": si paso",c,"element ",lista[m1+2])
		var = "t"+str(m),"= ",lista[m1-2],c,"t"+str(m-1)
		lista2.append(var)
		lista.remove(lista[m1-2])
		lista.remove(c)
		#lista.remove(lista[m1+2])
	elif re.match('[+*-/]',c) and lista[m1-2]==" ":
		var = "t"+str(m),"= ",lista[m1+2],c,"t"+str(m-1)
		lista2.append(var)
		#lista.remove(lista[m1-2])
		lista.remove(c)
		lista.remove(lista[m1+1])
	m1+=1

d=None
for d in lista2:
	print(d)

archivo.close()




