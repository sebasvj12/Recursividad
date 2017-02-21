'''
Created on 8/02/2017

@authores: Diego Alejandro Parra Daza 20141020063
                     Sebastián Vargas Jiménez 20132020093
'''
def pal(p):
    if  len(p)==1 or len(p)==0:
        return "Palindroma"
    elif(p[0]== p[len(p)-1]):
        p=p[1:-1]
        return pal(p)
    else:
        return "no es plindroma"

print("Palabras palindromas")
palabra= raw_input("Ingrese palabra: ")
print pal(""+palabra)



