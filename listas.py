'''
Created on 20/02/2017

@author: Casper
'''
def fun(p1,p2,p3):
    if len(p1)==1 and len(p2)==1 and len(p3)==1:
        return p1+","+p2+","+p3
    else:
        if p1[0]<p[len(p)-1]:
            return fun(p1[0],p2,p3)
        
print("menores numeros de varis listas")
lista1= raw_input("Ingrese lista 1: ")
lista2= raw_input("Ingrese lista 2: ")
lista3= raw_input("Ingrese lista 3: ")
print fun(lista1,lista2,lista3)
