
from math import log ,sqrt,log10
print ('valor a entar es  kb o ka')
escoje_kb_o_ka =str(input())


Moles=eval(input("entra los moles    \n"))
kb_o_ka =eval(input("k sub_b o k sub_a  \n exponete es '**' \n  "))
print("escoje para calcular 'pH' 'pOH' 'H+' o 'OH-' o metodo henderson_hasselbalch 'ph2'")
entrada =str(input())
ph2 ="pH2"
ph ="pH"
poh ="pOH"
h= "H+"
oh="OH-"
def henderson_hasselbalch(a,b,c):
	paso_uno=c+log10(a/b)
	print (paso_uno,'=',c,'+','log10(',a,'/',b,')',)

	if paso_uno>0:
		paso_dos=14-paso_uno
		print(paso_dos,"=","14-",paso_uno)
	else:
		paso_dos=14+paso_uno
		print(paso_dos,"=","14+",paso_uno)
def despejar(a,b,c):
	disc=round(b*b-4*a*c,50)
	if(a!=0):
	 if(disc<0):
	  print("tiene raices imaginarias")
	 else:

	  x1=round(-b+(sqrt(disc))/(2*a),5)
	  x2=round(-b-(sqrt(disc))/(2*a),5)

	  print("X1 = "+str(x1)+" X2 = "+str(x2))
	else:
	 print("coefiente cuadratico debe ser diferente de cero")
	 
if escoje_kb_o_ka.lower()=="kb":
	if entrada.lower() ==poh.lower():
		paso_uno=Moles*kb_o_ka				
		print('"despejamos "',paso_uno)
		paso_dos=sqrt(paso_uno)
		print("raiz de",paso_dos)
		paso_tres=-log10(paso_dos)
		print("log",paso_tres)
		print("POH=",paso_tres)	
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

if escoje_kb_o_ka.lower()=="ka":
	print('es un acido') 
	if entrada.lower() ==ph.lower():
		paso_uno=Moles*kb_o_ka				
		print('"despejamos "',paso_uno)
		paso_dos=sqrt(paso_uno)
		print("raiz de",paso_dos)
		print('"despejamos "',paso_uno)
		paso_tres=-log10(paso_dos)
		print("log",paso_tres)
		if paso_tres>0:
			paso_cuarto=14-paso_tres
			print("14-",paso_tres,"=",paso_cuarto)
		else:
			paso_cuarto=14+paso_tres
			print("14+",paso_tres,"=",paso_cuarto)
	if entrada.lower() == ph2.lower():
		sal =eval(input("entar las sal\n "))		
		henderson_hasselbalch(sal,Moles,kb_o_ka)
		
	if entrada.lower() ==h.lower():
		paso_uno=Moles*kb_o_ka
		print('"despejamos "',paso_uno)
		paso_dos=sqrt(paso_uno)
		print("raiz de",paso_uno,'=',paso_dos)
		paso_tres=-log10(paso_dos)
		print("log",paso_dos,'=',paso_tres)
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

