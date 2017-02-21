'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def div(n,m):
    if m > n :
        return 0;
    return div(n-m, m) + 1
print(programa que divide un numero de manera recursiva)
n= input("ingrese n: ")
m= input("ingrese m: ")
print(div(n,m))