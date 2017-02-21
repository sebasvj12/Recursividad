'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def pot (n , m):
    if m==1:
        return n
    return n*pot(n,m-1)
print("potenciaa de un numero, de manera recursiva")
n1= input("ingrese n: ")
m1=input("ingrese m: ")
print(pot(n1 , m1))