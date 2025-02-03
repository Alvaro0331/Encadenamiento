import matplotlib.pyplot as plt
import networkx as nx

#Definir valores de los nodos
nodo={
    "A": None,"B":None,"C":None,"D":True,"E":True,"F":True,
    "G":None,"H":None,"I":None,"J":None,"K":None,"L":True,"M":None
}

#Reglas de inferencia
reglas={
    "C":["A","B"],
    "G":["D","E","F"],
    "J":["H","I"],
    "K":["C","G"],
    "L":["G","J"],
    "M":["K","L"],   
}

#Funcion de encadenamiento
def encadenamiento(objetivo):
    #Identificar si ya conocemos el valor del objetivo
    if nodo[objetivo] is not None:
        return nodo[objetivo]
    
    #Identificar si se puede inferir su valor a partir de las reglas
    if objetivo in reglas:
        dependencias, regla=reglas[objetivo]
        print(f"Evaluando {objetivo} con {regla}")
        valor_premisas=[]
        for premisa in dependencias:
            #Recursion
            valor_premisa=encadenamiento(premisa)
            valor_premisas.append(valor_premisa)
        
        #Identificar si todas las premisas son verdaderas
        if all(valor_premisas):
            nodo[objetivo]=True
            return True
        #Si alguna premisa es falsa, el objetivo actual tambien es falso
        else:
            nodo[objetivo]=False
            return False
    
    #Preguntar al usuario por el valor de un dodo
    respuesta=input(f"{objetivo} es Verdadero o Falso? (V/F): ").strip().lower()
    #Asignar el valor proporcionado al nodo
    nodo[objetivo]= True if respuesta =="v" else False
    return nodo[objetivo]


#Test
objetivo="M"
encadenamiento(objetivo)
print(f" {objetivo}")