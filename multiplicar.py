'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def mul(n,m):
    if n==0 or m==0:
        return 0
    return n+mul(n,m-1)
print("multiplicacion recursiva")
n= input("ingrese n: ")
m= input("ingrese m: ")
print(mul(n,m))