'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def abs(n):  
    if n>0:
        return n;
    return abs(n*-1);
print("valor absoluto de un numero")
numero =input("Introduce un numero:")
print(abs(numero))    