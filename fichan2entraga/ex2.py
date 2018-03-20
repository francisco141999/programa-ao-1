n1 = input ("Introduza um numero: ")
n2 = input ("Introduza um numero: ")
n3 = input ("Introduza um numero: ")

''' a é uma variavel auxiliar
'''

if n2 > n1:   
  a=n1      
  n1=n2       
  n2=a      
if n3 > n2:
  if n3 >= n1:
    a=n1
    a2=n2
    n1=n3
    n2=a
    n3=a
  elif n3 >= n2 and n3 < n1:
    a=n2
    n2=n3
    n3=a

print ("A ordem decrescente ficou",n1,n2,n3)
print ("e a ordem crescente ficou",n3,n2,n1)  
     