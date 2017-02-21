'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def factorial(n):
    if n<=1:
        return 1;
    return n* factorial(n-1);
print("Programa recursivo que halla el fctoril e un numero")
numero = input("Introduce un numero:")
print(factorial(numero))    