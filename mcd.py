'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def mcd(a, b):
    if(b==0):
        return a
    else:
        return mcd(b, a % b)
print("programa que halla el mcd de dos numeros")
a=input("ingrese a: ")
b=input("ingrese b: ")
print(mcd(a,b))