'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def sumar_dig (n):
    if n == 0:
        return n
    else:
        return sumar_dig (n / 10) + (n % 10)
print("programa que suma los digitos de un numero")
num=input("Ingrese numero");
print(sumar_dig(num))