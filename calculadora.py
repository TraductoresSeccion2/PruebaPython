def suma(x,y):
 return x+y 

def resta(x,y):
 return x-y 
 
def multiplicacion(x,y):
 return x*y 
 
def division(x,y):
 return x/y 
 
def exponencial(x,y):
 return x**y 
 
bandera = True
while (bandera):
   print "Bienvenido al menu de opciones :"
   print "1.-Suma"
   print "2.-Resta"
   print "3.-Multiplicacion"
   print "4.-Division"
   print "5.-Exponencial"
   opcion = input();
   x=input("Escribe Tu Primer Valor");
   y=input("Escribe Tu segundo Valor");
   if(opcion==1):
	   print suma(x,y)
   elif(opcion==2):
	    print resta(x,y)
   elif(opcion==3):
	    print multiplicacion(x,y)
   elif(opcion==4):
       print division(x,y)
   elif(opcion==5):
	   print exponencial(x,y)
   elif(opcion==6):
	    bandera==False
   else:
	    print "tu opcion no es la valida"
		
	   
	
   
      	
	   
	
   
