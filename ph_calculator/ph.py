from math import log ,sqrt,log10
Moles=eval(input("entra los moles    \n"))
kb_o_ka =eval(input("k sub_b o k sub_a  \n exponete es '**' \n  "))
print("escoje para calcular 'pH' 'pOH' 'H+' o 'OH-'")
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
	print("log",paso_tres)
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
	print("log",paso_tres)
	print("POH=",paso_tres)
if entrada.lower() ==h.lower():
	paso_uno=Moles*kb_o_ka
	print('"despejamos "',paso_uno)
	paso_dos=sqrt(paso_uno)
	print("raiz de",paso_dos)
	paso_tres=-log10(paso_dos)
	print("log",paso_tres)
	if paso_tres>0:
		paso_cuatro=14-paso_tres
		print("14-",paso_tres,"=",paso_cuatro)
		if paso_dos> 0:
			paso_cinco=10**paso_dos
			print("10elvado",paso_dos,"=",paso_cinco)
	else:
				
		paso_cuatro=14+paso_tres
		print("14+",paso_tres,"=",paso_cuatro)
		if paso_dos< 0:		
			paso_cinco=-10**paso_dos
			print("10elvado",paso_dos,"=",paso_cinco) 
if entrada.lower() ==oh.lower():
	paso_uno=Moles*kb_o_ka
	print('"despejamos "',paso_uno)
	paso_dos=sqrt(paso_uno)
	print("raiz de",paso_dos)
	paso_tres=-log10(paso_dos)
	print("log",paso_tres)
	if paso_tres>0:
		paso_cuatro=14-paso_tres
		print("14-",paso_tres,"=",paso_cuatro)
		if paso_dos> 0:
			paso_cinco=10**paso_dos

			print("10elvado",paso_dos,"=",paso_cinco)		
	else:
		paso_cuarto=14+paso_tres
		print("14+",paso_tres,"=",paso_cuatro)
			
		paso_cuatro=14+paso_tres
		print("14+",paso_tres,"=",paso_cuatro)
		if paso_dos< 0:		
			paso_cinco=-10**paso_dos
			print("10elvado",paso_dos,"=",paso_cinco)  
