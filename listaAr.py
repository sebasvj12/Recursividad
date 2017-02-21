'''
Created on 20/02/2017

@author: Casper
'''
def fun(p):
    if  len(p)==1 or len(p)==0:
        return p
    else:
        return p[-1]+fun(p[:-1])

print("cmbiar orden")
palabra= raw_input("Ingrese lista: ")
print fun(""+palabra)
