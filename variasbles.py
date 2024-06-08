def suma(n1,n):
       resultado=n1+n2
       print(resultado)
def resta(n1,n):
       resultado=n1-n2
       print(resultado)
def multi(w,e):
       resultado=w*e
       print(resultado)
def divi(q,w):
       try:
              resultado=q/w
       except(ZeroDivisionError):
              print("No se puede dividir por 0")
              
n1=int(input("Ingrese el numero 1"))
n2=int(input("ingrese el numero 2"))
suma(n1,n2)
resta(n1,n2)
multi(n1,n2)
divi(n1,n2)
