"""/*******************************************************************************
Autor: Mateus Antony Medeiros Carvalho
Componente Curricular: MI-Algoritmos
Concluido em: 26/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/"""

import keyboard
from time import monotonic,sleep
import os
from random import randint



# Mostrar matriz
def mostrar_matriz():
    print('-='*15)
    for v in range(30):
        for k in range(30):
            print(matriz[v][k],end='')
        print()       
    print('-='*15)

# Criar nave
def criarNave():
    matriz[28][15] = '*'
    matriz[29][14] = '*'
    matriz[29][15] = '*'
    matriz[29][16] = '*'
    meio_nave = 15 # Posição do primeiro asterisco  e do segundo asterisco  da proxima linha [*]  e *[*]* 
    lado_esquerdo=14 # Posição do primeiro asterisco da linha de baixo [*]**
    lado_direito = 16 # Posição do terceito asterisco da linha de baixo **[*]

    return [meio_nave,lado_esquerdo,lado_direito] # Retorna o valor da posição da coluna de cada asterisco da nave


# Mover para esquerda
def moverEsquerda(meio_nave,lado_esquerdo,lado_direito): # Recebe a coluna de cada asterisco da nave
    os.system('cls')

    if lado_esquerdo == 1 :  # Se a posição da  coluna do 1º asterisco da parte de baixo da nave chegar a 1(segunda coluna) e  se o usuário continuar apertando para esquerda a nave não vai mover mais 

        # A nave vai ser apagada, mas os asterisco vai ser colocado na mesma posição
        matriz[28][meio_nave] = ' '
        matriz[29][lado_esquerdo]= ' '
        matriz[29][meio_nave] = ' '
        matriz[29][lado_direito] = ' '

        matriz[28][meio_nave]='*'
        matriz[29][lado_esquerdo]='*'
        matriz[29][meio_nave]='*'
        matriz[29][lado_direito]='*'
    else:
        # Apaga os asterisco da posição que está
        matriz[28][meio_nave] = ' '
        matriz[29][lado_esquerdo]= ' '
        matriz[29][meio_nave] = ' '
        matriz[29][lado_direito] = ' '

        # Diminui um no  valor de cada posição de coluna dos asterisco
        meio_nave -=1        
        lado_esquerdo-=1
        lado_direito-=1
        # a coluna anterior recebe os asteriscos da nave
        matriz[28][meio_nave]='*'
        matriz[29][lado_esquerdo]='*'
        matriz[29][meio_nave]='*'
        matriz[29][lado_direito]='*'

    mostrar_matriz() # Mostra a matriz
    return [meio_nave,lado_esquerdo,lado_direito]# Retorna os valores das posições 

# mover para direita
def moverDireita(meio_nave,lado_esquerdo,lado_direito):
    os.system('cls')
    if lado_direito==28: # Se a posição da  coluna do 3º asterisco da parte de baixo da nave chegar ao valor de 28(penultima coluna) e  se o usuário continuar apertando para direita a nave não vai mover mais

        # A nave vai ser apagada, mas os asterisco vai ser colocado na mesma posição
        matriz[28][meio_nave] = ' '
        matriz[29][lado_esquerdo]= ' '
        matriz[29][meio_nave] = ' '
        matriz[29][lado_direito] = ' '

        matriz[28][meio_nave]='*'
        matriz[29][lado_esquerdo]='*'
        matriz[29][meio_nave]='*'
        matriz[29][lado_direito]='*'
    else:
        # Apaga os asterisco da posição que está
        matriz[28][meio_nave] = ' '
        matriz[29][lado_esquerdo]= ' '
        matriz[29][meio_nave] = ' '
        matriz[29][lado_direito] = ' '
        # Aumenta um no valor de cada posição de coluna dos asterisco
        meio_nave +=1
        lado_esquerdo+=1
        lado_direito+=1
        # A proxima coluna recebe os asteriscos da nave
        matriz[28][meio_nave]='*'
        matriz[29][lado_esquerdo]='*'
        matriz[29][meio_nave]='*'
        matriz[29][lado_direito]='*'
    
    mostrar_matriz()
    return [meio_nave,lado_esquerdo,lado_direito]# Retorna os valores das posições



# Cria o asteroide apartir do primeiro asterisco da primeira linha do asteroide [*]**
def criarAsteroides():

    crescimento=0 # Essa variável vai ser usada na soma com a linha inicial de cada asterisco do asteroide, para adicionar cada esterisco na linha correta

    numero_aleatorio=randint(3,24)# Número aleatório para nascer o primeiro  asterisco da primeira linha do asteroide [*]** 

    #Os asterisco que estiver em colchetes é aquele que está sendo mencionado na atribuição

    # Primeira linha ***
    matriz[0][numero_aleatorio]='*'     # [*]**
    matriz[0][numero_aleatorio+1]='*'   # *[*]*
    matriz[0][numero_aleatorio+2]='*'   # **[*]

    # Segunda linha *****
    matriz[1][numero_aleatorio]='*'     # **[*]**
    matriz[1][numero_aleatorio+1]='*'   # ***[*]*
    matriz[1][numero_aleatorio+2]='*'   # ****[*]
    matriz[1][numero_aleatorio -1]='*'  # *[*]***
    matriz[1][numero_aleatorio+3]='*'   #[*]****

    # Terceira linha *******
    matriz[2][numero_aleatorio]='*'     #**[*]****
    matriz[2][numero_aleatorio+1]='*'   #***[*]***
    matriz[2][numero_aleatorio+2]='*'   #****[*]**
    matriz[2][numero_aleatorio-1]='*'   #*[*]*****
    matriz[2][numero_aleatorio+3]='*'   #*****[*]*
    matriz[2][numero_aleatorio-2]='*'   #[*]******
    matriz[2][numero_aleatorio+4]='*'   #******[*]

    # Quarta linha *****
    matriz[3][numero_aleatorio]='*'
    matriz[3][numero_aleatorio+1]='*'
    matriz[3][numero_aleatorio+2]='*'
    matriz[3][numero_aleatorio -1]='*'
    matriz[3][numero_aleatorio+3]='*'

    # Quinta linha  ***
    matriz[4][numero_aleatorio]='*'
    matriz[4][numero_aleatorio+1]='*'
    matriz[4][numero_aleatorio+2]='*'


    return [numero_aleatorio,crescimento] 

# Mover asteroides                               
def moverAsteroides(numero_aleatorio,linha_asterisco):# Recebe o número aleatório da função anterior e a variável linha_asterisco que vai ser somada com os valores fixos do asteroide 


    # Essa condição vai ver se tem o simbolo 'o' na posições indicadas, pois se tiver significa que o tiro está a uma linha de diferença do asteroide
    # matriz[4+ linha_asterisco][numero_aleatorio]=='o' o primeiro asterisco da ultima linha do asteroide
    # matriz[4+ linha_asterisco][numero_aleatorio+1]=='o' o segundo asterisco da ultima linha do asteroide
    # matriz[4+ linha_asterisco][numero_aleatorio+2]=='o' o terceiro asterisco da ultima linha do asteroide
    # matriz[3+ linha_asterisco][numero_aleatorio -1]=='o' o primeiro asterisco da penultima linha do asteroide
    # matriz[3+ linha_asterisco][numero_aleatorio+3]=='o' o ultimo asterisco da penultima linha do asteroide
    # matriz[2+ linha_asterisco][numero_aleatorio-2] == 'o' o primeiro asterisco da 3º linha do asteroide
    # matriz[2+ linha_asterisco][numero_aleatorio+4]=='o o ultimo asterisco da 3º linha do asteroide

    if  matriz[4+ linha_asterisco][numero_aleatorio]=='o' or matriz[4+ linha_asterisco][numero_aleatorio+1]=='o' or matriz[4+ linha_asterisco][numero_aleatorio+2]=='o'or matriz[2+ linha_asterisco][numero_aleatorio-2]=='o' or matriz[2+ linha_asterisco][numero_aleatorio+4]=='o' or matriz[3+ linha_asterisco][numero_aleatorio -1]=='o' or matriz[3+ linha_asterisco][numero_aleatorio+3]=='o':


        linha_asterisco= 26 # Esse valor que vai servir para criar outro asteroide 
        acabou_tiro= 28 # Esse valor vai fazer sumir o tiro que está na frente do asteroide
        return [linha_asterisco,acabou_tiro]
 
    # Se linha asterisco ser igual a 25 ou 24, significa que os asterisco da ultima linha do asteroide estão na mesma linha que os asterisco da nave
    if linha_asterisco == 25 or linha_asterisco == 24: 
        # Se encontrar algum asterisco nas posições indicadas , significa que a nave está a uma linha de diferença do asteroide
        # Obs:Essas posições foram explicadas logo acima 
        if  matriz[4+ linha_asterisco][numero_aleatorio]=='*' or matriz[4+ linha_asterisco][numero_aleatorio+1]=='*' or matriz[4+ linha_asterisco][numero_aleatorio+2]=='*'or matriz[2+ linha_asterisco][numero_aleatorio-2]=='*' or matriz[2+ linha_asterisco][numero_aleatorio+4]=='*' or matriz[3+ linha_asterisco][numero_aleatorio -1]=='*' or matriz[3+ linha_asterisco][numero_aleatorio+3]=='*':
            linha_asterisco = 30 # Retorna o valor que vai fazer com que o jogo pare
            return [linha_asterisco]
        

    
    # Adiciona os asterisco em cada linha e em cada coluna referente
    #Vai somar com linha asterisco sempre, o que vai fazer com que mude de linha 

    # Primeira linha do asteroide
    matriz[0 + linha_asterisco][numero_aleatorio]='*'
    matriz[0+ linha_asterisco][numero_aleatorio+1]='*'
    matriz[0+ linha_asterisco][numero_aleatorio+2]='*'
    
    # Segunda linha do asteroide
    matriz[1+ linha_asterisco][numero_aleatorio]='*'
    matriz[1+ linha_asterisco][numero_aleatorio+1]='*'
    matriz[1+ linha_asterisco][numero_aleatorio+2]='*'
    matriz[1+ linha_asterisco][numero_aleatorio -1]='*'
    matriz[1+ linha_asterisco][numero_aleatorio+3]='*'

    # Terceira linha do asteroide
    matriz[2+ linha_asterisco][numero_aleatorio]='*'
    matriz[2+ linha_asterisco][numero_aleatorio+1]='*'
    matriz[2+ linha_asterisco][numero_aleatorio+2]='*'
    matriz[2+ linha_asterisco][numero_aleatorio-1]='*'
    matriz[2+ linha_asterisco][numero_aleatorio+3]='*'
    matriz[2+ linha_asterisco][numero_aleatorio-2]='*'
    matriz[2+ linha_asterisco][numero_aleatorio+4]='*'

    # Quarta linha do asteroide
    matriz[3+ linha_asterisco][numero_aleatorio]='*'
    matriz[3+ linha_asterisco][numero_aleatorio+1]='*'
    matriz[3+ linha_asterisco][numero_aleatorio+2]='*'
    matriz[3+ linha_asterisco][numero_aleatorio -1]='*'
    matriz[3+ linha_asterisco][numero_aleatorio+3]='*' 

    # Quinta linha do asteroide
    matriz[4+ linha_asterisco][numero_aleatorio]='*'
    matriz[4+ linha_asterisco][numero_aleatorio+1]='*'
    matriz[4+ linha_asterisco][numero_aleatorio+2]='*'


    os.system('cls') #LIMPA O TERMINAL
    mostrar_matriz() # Mostro a matriz junto com o asteroide
    
    # Apaga os asterisco em cada linha e em cada coluna referente

    # Primeira linha do asteroide
    matriz[0 + linha_asterisco][numero_aleatorio]=' '
    matriz[0+ linha_asterisco][numero_aleatorio+1]=' '
    matriz[0+ linha_asterisco][numero_aleatorio+2]=' '
    
    # Segunda linha do asteroide
    matriz[1+ linha_asterisco][numero_aleatorio]=' '
    matriz[1+ linha_asterisco][numero_aleatorio+1]=' '
    matriz[1+ linha_asterisco][numero_aleatorio+2]=' '
    matriz[1+ linha_asterisco][numero_aleatorio -1]=' '
    matriz[1+ linha_asterisco][numero_aleatorio+3]=' '

    # Terceira linha do asteroide
    matriz[2+ linha_asterisco][numero_aleatorio]=' '
    matriz[2+ linha_asterisco][numero_aleatorio+1]=' '
    matriz[2+ linha_asterisco][numero_aleatorio+2]=' '
    matriz[2+ linha_asterisco][numero_aleatorio-1]=' '
    matriz[2+ linha_asterisco][numero_aleatorio+3]=' '
    matriz[2+ linha_asterisco][numero_aleatorio-2]=' '
    matriz[2+ linha_asterisco][numero_aleatorio+4]=' '

    # Quarta linha do asteroide
    matriz[3+ linha_asterisco][numero_aleatorio]=' '
    matriz[3+ linha_asterisco][numero_aleatorio+1]=' '
    matriz[3+ linha_asterisco][numero_aleatorio+2]=' '
    matriz[3+ linha_asterisco][numero_aleatorio -1]=' '
    matriz[3+ linha_asterisco][numero_aleatorio+3]=' ' 

    # Quinta linha do asteroide
    matriz[4+ linha_asterisco][numero_aleatorio]=' '
    matriz[4+ linha_asterisco][numero_aleatorio+1]=' '
    matriz[4+ linha_asterisco][numero_aleatorio+2]=' '

    linha_asterisco+=1 # Aumento o valor dessa variável para ela modificar as linhas onde será adicionado o asteroide

    return [linha_asterisco]

# Criar Tiro
def criarTiro(meio_nave_do_tiro):# Vai receber como parâmetro a posição do meio da nave
    matriz[27][meio_nave_do_tiro] = 'o'
    diminuir= 1 #Valor que vai usar na subtração com o número inicial da linha  para fazer com que o projetil se mova

    return [diminuir,meio_nave_do_tiro] #Retorna diminuir


# Subir Tiro
def subir(posicao_do_tiro):# Recebe uma lista onde contem outras listas que guarda o valor do coluna que a nave estava quando atirou e o valor  de diminuir que foi mencionado na funçã anterior
    if len(posicao_do_tiro)==0: # Se não estiver nada nessa lista,ou seja, se não tiver dado o tiro, retorna a própria lista sem modificações 
        return posicao_do_tiro
    else:
        for elemento in posicao_do_tiro: # Para cada elemento na lista 
            if len(elemento) == 0: # Se na lista que está dentro não estiver nada,significa que o tiro foi apagado, ou seja, ele remove aquela lista 
                posicao_do_tiro.remove(elemento)
            elif elemento[0] != 28:  # Se diminuir(mencionado na função anterior) for diferente de 28, vai ocorrer a movimentação do projetil normalmente   
                matriz[27-elemento[0]][elemento[1]] = 'o'
                matriz[27-elemento[0]+1][elemento[1]] = ' '
                elemento[0] +=1 #somando 1 para aumantar o valor de diminuir
            else: 
                if elemento[0] == 28:
                    for p in range(27): #Número de linhas que o projetil pode está 
                        for q in range(1,29): # Número de colunas disponíveis
                            matriz[p][q] = ' ' # Todos os valores receber um espaço em branco, mas como o asteroide não para de se mover, ele não vai ser apagado, mas o projetil vai
                    elemento.pop(0) # Elimina o primeiro elemento da lista que está dentro da lista principal
                    elemento.pop(0) # Elimina o primeiro elemento da lista que está dentro da lista principal novamente, pois o valor que estava em elemento[1] passou a para o indice elemento[0]
                
                
        return posicao_do_tiro
        



keyboard.press('f11') #O pragrama vai pressionar a tecla f11 para ficar em tela cheia
#MENU
ordem = []  #Lista que vai guarda os valores da pontuação em ordem decrescente 
pessoa = [] #lista que guarda o nome e a pontuação de cada participante
recordes= [] #lista que guarda lista de pessoa

variavel_contadora = 0 # Variavel qualquer para ser utilizado com loop
while variavel_contadora ==0: 
    os.system('cls') 
    opcao = str (input('[1]Jogar\n[2]Recordes\n[3]Sobre\n[4]Sair\nQual a operação que você quer fazer ?'))
    # Tratamento de erro caso for digitado algum valor inválido
    while opcao not in ('1','2','3','4'):
        print('DIGITE UM OPÇÃO VÁLIDA')
        opcao = str (input('[1]Jogar\n[2]Recordes\n[3]Sobre\n[4]Sair\nQual a operação que você quer fazer ?'))

    opcao = int(opcao)
    if opcao == 1:
        # Jogo
        nome=str(input('DIGITE SEU NOME:'))
        #CRIAR MATRIZ
        matriz = [] 
        #Cria a matriz com as barras de canto para ser o cenário de fundo
        for x in range(30):
            linha =[]
            for y in range(30):
                if y == 29 or y ==0:
                    linha.append('|')
                else:
                    linha.append(" ")
            matriz.append(linha)


        nave= criarNave()  # recebe os valores iniciais da posição da nave
        mostrar_matriz()

        asteroide=criarAsteroides() #recebe o número da coluna e o crescimento 
                                 
        lista_de_tiros=[] # Lista que recebe as  listas com as diminuições e a posições de  onde saiu  os tiros
        tiro = [0,0] # lista com a diminuição e a posição de  onde saiu  o tiro, sendo modificado toda vez que apertar espaço
        variavel_qualquer =1 # Variável usada para o loop
        potuacao = 0 
        life = 10 # No lugar de colocar o número de asteroides, coloquei a vida com 10 e vai reduzindo a cada asteroide que não foi destruido

        while variavel_qualquer == 1:
            sleep(0.03) #Reduzir a velocidade de descida do asteroide
            linhaDoPrimeiroAsterisco = moverAsteroides(asteroide[0],asteroide[1])
            sleep(0)

            if len(linhaDoPrimeiroAsterisco) == 1: # Se a função retornar apenas um valor na lista
                linhaDoPrimeiroAsterisco = linhaDoPrimeiroAsterisco[0] # A variável vai receber apenas o valor de crescimento, que vai fazer o asteroide descer
            elif len(linhaDoPrimeiroAsterisco) == 2:# Se for retornado 2 valores na lista,significa que teve colisão entre o projetil e o asteroide
                if len(lista_de_tiros[0]) >0:
                    lista_de_tiros[0][0] = linhaDoPrimeiroAsterisco[1] # A primeira lista que está dentro de lista_de_tiros vai receber 28,ou seja, vai ser excluida futuramente
                linhaDoPrimeiroAsterisco = linhaDoPrimeiroAsterisco[0] # Aqui a variável vai receber seu novo valor, que vai ser sempre o linha_asterisco(crescimento)
                potuacao+=1 # Ja que o prejetil apagou e o asteroide apagou, o jogador vai ganhar mais um de pontuação

            if linhaDoPrimeiroAsterisco == 25:# Se chegou em 25, significa que a soma para resultar na linha que vai ser adicionado a linha do ultimo asterisco do asteroide vai ser 29,ou seja, ultima linha da matriz.Sendo assim, o jogador vai perder um de vida cada vez ques isso acontecer
                life -=1 
            elif linhaDoPrimeiroAsterisco == 30: # Se retornou 30, significa que teve colisão entre a nave e o asteroide
                life = 0 
            if life == 0:   # Se chegar a 0 de vida o jogo vai salvar a pontuação e o nome nos recorde e vai voltar ao menu  
                print('DERROTA!')

                if len(pessoa)>0: # Se tiver alguem cadastrado na lista pessoa
                    # Vai apagar o nome e a pontuação
                    pessoa.pop(0)
                    pessoa.pop(0)
                    # Vai adicionar um novo nome e uma nova pontuação
                    pessoa.append(nome)
                    pessoa.append(potuacao)
                    # Vai adicionar na lista de recordes
                    recordes.append(pessoa[:])
    
                else:
                    # Vai adicionar um novo nome e uma nova pontuação   
                    pessoa.append(nome)
                    pessoa.append(potuacao)
                    # Vai adicionar na lista de recordes
                    recordes.append(pessoa[:])
                
                
                variavel_qualquer = 2
            asteroide[1]= linhaDoPrimeiroAsterisco #O crescimento do asteroide recebe um novo valor

            if linhaDoPrimeiroAsterisco == 26:
                # linhaDoPrimeiroAsterisco é o crescimento que é usado para fazer o asteroide descer.
                asteroide=criarAsteroides() # Cria um novo asteroide
                
            if keyboard.is_pressed('left'): # Se for pressionado esquerda
                nave=moverEsquerda(nave[0],nave[1],nave[2]) # Recebe os valores da poscição da nave
            if keyboard.is_pressed('right'):   # Se for pressionado direita
                nave=moverDireita(nave[0],nave[1],nave[2]) # Recebe os valores da poscição da nave
            if keyboard.is_pressed('esc'): # Se for pressionado esc finaliza o jogo 
                print('JOGO FINALIZADO')
                if len(pessoa)>0:
                    pessoa.pop(0)
                    pessoa.pop(0)
                    pessoa.append(nome)
                    pessoa.append(potuacao)
                    recordes.append(pessoa[:])

                else:   
                    pessoa.append(nome)
                    pessoa.append(potuacao)
                    recordes.append(pessoa[:])
            
                variavel_qualquer =2 

            if keyboard.is_pressed('space'): # Se for pressionado espaço
                tiro= criarTiro(nave[0]) # Recebe o valor da coluna que está o meio da nave 
                lista_de_tiros.append(tiro)
            lista_de_tiros= subir(lista_de_tiros) # Essa função sempre vai está sendo executada,mas so moverá o tiro quando tiver algum tiro na lista_de_tiros
            # Exibe a pontuação e a vida
            print(f'Pontuação:{potuacao}')
            print(f'Vida:{life}')

    elif opcao == 2:
        # Recordes
        os.system('cls')
        print('-='*20)
        print('Recordes:')
        print('-='*20)
        print('NOMES     PONTUAÇÃO')
        for x in range(len(recordes)): # Para cada pessoa que estiver na matriz recordes
            if recordes[x][1] not in ordem: # Se a pontuação não estiver na lista ordem, vai ser adicionado
                ordem.append(recordes[x][1]) 
        ordem.sort(reverse=True) # Deixando me ordem decrescente
        for n in ordem: # Para cada pontuação em ordem
            for pessoas in recordes: # Para cada pessoa em recodes
                if n == pessoas[1]:# Se n(valor da pontuação em ordem) for igual a pessoas(valor da pontuação )
                    print(f'{pessoas[0]:<10}{pessoas[1]:<5}') # Vai mostrar na dela o nome e a pontuação
        sleep(5)# Vai mostra na tela isso por 5 segundo, depois vai apagar o terminal
        os.system('cls') 
        sleep(0)
    elif opcao == 3:
        # Informação sobre o criador
        os.system('cls')
        print('Criador : Mateus Antony Medeiros Carvalho\nFeira De Santan-Ba\nO Jogo ainda está em beta!Breve novos avanços ')
        sleep(8)
        os.system('cls')
        sleep(0)
    if opcao == 4:
        # Sair do programa
        variavel_contadora = 1
        print('Obrigado pela atenção')
