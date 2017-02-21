'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def fibo(n):
    if (n == 0 or n == 1 ):
        return 1
    return fibo(n-1) + fibo(n-2) 
print("1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610")
print("n_esimo numero de la serie fibonacci")
num=input("ingrese numero n-esimo:")
print(fibo(num))