'''lista2_Q11 Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
==== =MENU========
1)Cadastar nome
2)Pesquisar nome
3)Listar todos os nome
0) Sair do programa'''


cont = 0
cadastrar = list()
aumentando = list()
nomes = [ 'Ana', 'Thiago', 'Luana', 'Felipe', ' Marcos', 'Sabrina']


posicao = int(input('Digite quantas posições você irá alimentar a lista: '))
for i in range(posicao):
    cont +=1
    print('''=====MENU========
                1)Cadastar nome
                2)Pesquisar nome
                3)Listar todos os nomes
                0) Sair do programa. ''')
    ação = input('Digite o que deseja fazer: ').lower()
    if ação == 'cadastrar nome':
        cadastrar.append(input('Digite o nome que deseja colocar na lista: '))
        aumentando = cadastrar  #acrescentando o nome a lista
        nomes.append(cadastrar)

        
    if ação == 'pesquisar nome':
            pesquisar_nome= input('Digite o nome que deseja pesquisar: ')
            if pesquisar_nome in aumentando:
                print(f'Esse é o nome que cadastrou {pesquisar_nome}')  
            elif pesquisar_nome in nomes:
                index = nomes.index(pesquisar_nome)  #mostrar a posição do nome
                print(f'{pesquisar_nome} está na lista {nomes}')
                print(f'O indice de {pesquisar_nome} é {index}') 
            else:
                print('Esse nome não está na lista')

    if ação == 'listar todos os nomes':
        print(nomes)
    

    if ação == 'sair do programa':
        if cont == 1:
          print('VOCÊ SAIU NA PRIMEIRA RODADA.')
          break
        else:
         print('Você saiu do programa')
        break

    
