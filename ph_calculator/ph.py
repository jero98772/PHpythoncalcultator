from math import log, exp, expm1 ,sqrt,log10
Moles=eval(input("entra los moles    \n"))
kb_o_ka =eval(input("k sub_b o k sub_a  \n exponete es 'e' \n  "))
ph ="pH"
poh ="pOH"
h= "H+"
oh="OH-"
entrada =str(input())
if entrada.lower() ==ph.lower():
	paso_uno=Moles*kb_o_ka
	print('"despejamos "',paso_uno)
	paso_dos=sqrt(paso_uno)
	print("raiz de",paso_dos)
	paso_tres=-log10(paso_dos)
	print("log",paso_dos)
	if paso_tres>0:
		paso_cuarto=14-paso_tres
		print("14-",paso_tres,"=",paso_cuarto)
	else:
		paso_cuarto=14+paso_tres
		print("14+",paso_tres,"=",paso_cuarto)
if entrada.lower() ==poh.lower():
	paso_uno=Moles*kb_o_ka
	print('"despejamos "',paso_uno)
	paso_dos=sqrt(paso_uno)
	print("raiz de",paso_dos)
	paso_tres=-log10(paso_dos)
	print("log",paso_dos)
	print("POH=",paso_tres)
if entrada.lower() ==h.lower():
	paso_uno=Moles*kb_o_ka
	print('"despejamos "',paso_uno)
	paso_dos=sqrt(paso_uno)
	print("raiz de",paso_dos)
	paso_tres=-log10(paso_dos)
	print("log",paso_dos)
	if paso_tres>0:
		paso_cuatro=14-paso_tres
		print("14-",paso_tres,"=",paso_cuatro)
		paso_cinco=10**paso_cuatro
		print("10elvado",paso_cuatro,"=",paso_cinco)
	else:
		paso_cuatro=14+paso_tres
		print("14+",paso_tres,"=",paso_cuatro)
		paso_cinco=10**paso_cuatro
		print("10elvado",paso_cuatro,"=",paso_cinco) 
if entrada.lower() ==oh.lower():
	paso_uno=Moles*kb_o_ka
	print('"despejamos "',paso_uno)
	paso_dos=sqrt(paso_uno)
	print("raiz de",paso_dos)
	paso_tres=-log10(paso_dos)
	print("log",paso_dos)
	if paso_tres>0:
		paso_cuatro=14-paso_tres
		print("14-",paso_tres,"=",paso_cuatro)
		paso_cinco=10**paso_cuatro
		print("10elvado",paso_cuatro,"=",paso_cinco)		
	else:
		paso_cuarto=14+paso_tres
		print("14+",paso_tres,"=",paso_cuatro)
		paso_cinco=10**paso_cuatro
		print("10elvado",paso_cuatro,"=",paso_cinco) 