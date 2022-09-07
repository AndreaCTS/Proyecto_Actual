from random import random
from math import log,e

seed = random()
generatedNumbers = []
lambdaNumber = 0.429


def generar(seed, quantity, generatedNumbers):
    for i in range(quantity):
        seed = fixSeed(seed)
        seed= ((-(log(1 - seed,e)))/lambdaNumber)
        seed= fixSeed(seed)
        generatedNumbers.append(int(seed*10))
    return generatedNumbers

def fixSeed(seed):
    while seed >= 1:
        seed = seed/10
    return seed



with open("C:\\Users\\Andrea Terraza\\OneDrive\\Documentos\\document.txt","a") as document:
    contador=1
    count=1
    document.write("NEW LINES\n")
   
    #se hacen 10 repeticiones, en cada repeticion se agregran 1000 numeros a la lista
    #se escriben en el archivo, luego se borra la lista y en la siguiente repetición se
    #vuelven a generar los 1000 números
    while(count<=10):
        count+=1
        generatedNumbers = generar(seed, 1000, generatedNumbers)
        for i in (generatedNumbers):
                
            if(contador % 7 == 0):
                document.write(str(i)+",\n")
            else:
                document.write(str(i)+",")
            contador+=1

        contador=0
        generatedNumbers.clear()

    document.close()    
        