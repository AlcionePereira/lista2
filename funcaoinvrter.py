'''Lista2_q15 Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''
from random import randint
def listaD():
    for i in range(max_lista):
        lista_D[i] = randint(0,100)
     
            
def inverterLista():
    lista_E = lista_D[::-1]
    return lista_E
    
max_lista = 5      
lista_D = list(range(max_lista))
#lista_e = list(range(max_lista))
listaD()
print("\nLista_D :", lista_D)
print("\nLista E: ", inverterLista())
            
