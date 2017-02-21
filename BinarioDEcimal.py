'''
Created on 9/02/2017
Convertir de binario a decimal y decimal a binario
@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def Conv_bin(dato):
    if(dato<2):
        return dato
    else:
       
        print (dato%2)
        return  Conv_bin(dato/2)
        
        
def conv_dec(dato):
    if(dato<10):
        return dato
    else:
        return (dato%2)+conv_dec(dato/2)*10
def main():
    print("Programa que convierte un numero decimal a binario o binario a decimal)
    num=input("Escriba 1 para Binario a Decimal o 2 de decimal a binario")
    num2=input("escriba numero: ")
    if(num==1):
        print (conv_dec(num2))
        
    elif(num==2):
        print(Conv_bin(num2))
    else:
        print("Numero incorrecto")
main()