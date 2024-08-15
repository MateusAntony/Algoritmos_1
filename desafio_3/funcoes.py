from datetime import date,timedelta
import os



def lerArquivo(nomeDoArquivo): # Recebe como parâmetro o nome do arquivo
    matriz = [] 
    arquivo = open(nomeDoArquivo,'r') # Ler todo arquivo
    for linha in arquivo: # Adiciona cada linha do arquivo na matriz
        linha=linha.split('|') 
        for x in range(len(linha)):
            linha[x]= linha[x].strip()
        matriz.append(linha)
    arquivo.close()
    return matriz # Retorna matriz

def existe_essa_Pasta(nome_da_pasta): 
    if os.path.exists(nome_da_pasta) == False: # Se não existir a pasta, vai ser criada
        os.makedirs(nome_da_pasta)

def existe_esse_Arquivo(nome_do_arquivo):
    if os.path.exists(nome_do_arquivo) == False: # Se não existir o arquivo , vai ser criado
        open(nome_do_arquivo,'w')

def adicionarCliente():
    #Criar dicionário
    print('-='*30)
    cliente = {} # Dicionário onde vai armazenar as informações do cliente
    # Coloco as informações
    cliente['Nome'] = str(input('Digite o nome do cliente:')).title()
    cliente['Endereco']= str(input('Digite o endereço:'))
    cliente['Telefone']= str(input('Digite o telefone:'))

    codigo_do_cliente = open('Arquivos/Código.txt','r') # Abrindo o arquivo do código

    for x in  codigo_do_cliente:
        codigo = x # Armazenando o código em uma variável
    codigo_do_cliente.close()
    codigo = int(codigo)  
    codigo +=1 #Somando mais um ao código 
    # Gera o novo código para o outro cliente
    cliente['Código']= codigo
    codigo = str(codigo)
    
    # Adiciono o código atualizado no arquivo de código
    codigo_do_cliente = open('Arquivos/Código.txt','w')
    codigo_do_cliente.write(codigo) # Adicionando o código atualizado no arquivo 
    codigo_do_cliente.close()
    arquivo_clientes=open('Arquivos/Cliente.txt','a')
    # Adiciono o dicionário no arquivo
    for informacao in cliente:
        arquivo_clientes.write(f'{cliente[informacao]}|') # Salvando as informações no arquvio Cliente.txt
    arquivo_clientes.write('\n')
    arquivo_clientes.close()
    
def editarCliente():
    print('-='*30)
    matriz = []
    cont = 0 # Contador usado para saber se encontrou ou não o código digitado
    print('-='*30)
    procurar_codigo= str(input('Digite o código do cliente:'))

    arquivo_clientes= open('Arquivos/Cliente.txt','r')
    print('-='*30)
    #Pecorre todo o arquivo procurando o código
    for linha in arquivo_clientes: # Analisando cada linha do arquivo

        linha=linha.split('|')
        linha.pop(4)
        for x in range(len(linha)):
            linha[x]= linha[x].strip()
        if procurar_codigo == linha[3]: # Se o código digitador for igual ao código que está na linha 
            mais_troca = 'S' # Usado para saber se o usuário quer fazer mais edições
            while mais_troca in 'Ss':
                cont=1 # Muda o valor do contador, para o sistema saber que achou o código
                print(f'Nome:{linha[0]}\nEndereço:{linha[1]}\nTelefone:{linha[2]}\nID:{linha[3]}')
                print('-='*30)
                opçoes = ['1','2','3'] # Opções de troca disponível
                trocar=str(input('[1]Trocar o nome\n[2]Trocar o endereço\n[3]Trocar o telefone\nEscolha a opção desejada:'))
                while trocar not in opçoes: # Tratamento de Erro
                    print('-='*30)
                    trocar=str(input('[1]Trocar o nome\n[2]Trocar o endereço\n[3]Trocar o telefone\nEscolha a opção desejada:'))

                # Trocar o nome    
                if trocar == '1':
                    print('-='*30)
                    print(f'Nome que foi cadastrado :{linha[0]}')
                    novo= str(input('Digite o novo nome:')).title()
                    linha[0]= novo 

                # Trocar endereço
                elif trocar == '2':
                    print('-='*30)
                    print(f'Endereço cadastrado que foi cadastrado :{linha[1]}')
                    novo= str(input('Digite o novo endereço:'))
                    linha[1]= novo

                # Trocar teleforne    
                elif trocar == '3':
                    print('-='*30)
                    print(f'Telefone que foi cadastrado :{linha[2]}')
                    novo= str(input('Digite o novo telefone:'))
                    linha[2]= novo

                # Opção de continnuar trocando ou não
                mais_troca=str(input('[S]Sim\n[N]Não\nDeseja trocar mais alguna coisa ?'))
                print('-='*30)

                while mais_troca not in 'SsNn': # Tratamento de erro
                    mais_troca=str(input('[S]Sim\n[N]Não\nDeseja trocar mais alguna coisa ? Digite apenas S ou N:'))
                    print('-='*30)

                if mais_troca in 'Nn': # Se não desejar fazer mais edições, é mostrado na tela as alterações
                    mais_troca = 'N'
                    print(f'Nome:{linha[0]}\nEndereço:{linha[1]}\nTelefone:{linha[2]}\nID:{linha[3]}')
                    print('-='*30)
        matriz.append(linha)
    if cont ==0: # Se o valor de cont não mudar, significa que o id não encontrado
        print('ID não encontrado')

    arquivo_clientes.close()

    #Adiciona as informações no arquivo
    arquivo_clientes= open('Arquivos/Cliente.txt','w')
    for x in range(len(matriz)):
        for y in range(4):
            if y != 3:
                arquivo_clientes.write(f'{matriz[x][y]}|')

            else:
                arquivo_clientes.write(f'{matriz[x][y]}|\n')
    arquivo_clientes.close()

def listarCliente():
    print('-='*30)
    listar = str(input('[1]Listar todos os clientes\n[2]Escolher um cliente específico\nDigite o número referente a operação que deseja fazer:'))
    print('-='*60)
    while listar not in '12':
        listar = str(input('[1]Listar todos os clientes\n[2]Escolher um cliente específico\nDigite o número referente a operação que deseja fazer:'))
        print('-='*60)

    if listar == '1':
        matriz=[] # Vai está todas as linha do arquivo
        emOrdem=[] # Vai está  o arquivo ordenado pelo nome  
        arquivo_clientes= open('Arquivos/Cliente.txt','r')
        for linha in arquivo_clientes:

            linha=linha.split('|')
            linha.pop(4)
            for x in range(len(linha)):
                linha[x]= linha[x].strip()
            matriz.append(linha)
        if len(matriz) == 0: # Se não tiver nenhuma linha em matriz
            print('nenhum cliente foi cadastrado ainda')
        else:
            for x in range(len(matriz)):
                # Deixando todas as letras de todos os nomes minuscusla
                matriz[x][0]=matriz[x][0].lower() 
                emOrdem.append(matriz[x][0])
            # Método de ordenação utilizado na aula da professora Claudia Pinto Pereira
            t = len(emOrdem)
            for i in range(0, t-1): # Vai repetir o processo de encontrar o menor e ordenar até chegar no penúltimo indice da lista
                min = i
                for j in range(i+1, t): # Econtra o menor item da lista e coloca na primeira posição
                    if emOrdem[j][0] < emOrdem[min][0]:
                        min = j                   
                emOrdem[i], emOrdem[min] = emOrdem[min], emOrdem[i]

            for x in range(len(emOrdem)):
                emOrdem[x]=emOrdem[x].title() # Deixando a primeira letra dos nomes em maiusculo

            # Comparando os nomes em ordem com os nomes que estão na matriz
            for y in emOrdem:
                cont = 0
                for x in range(len(matriz)):
                    matriz[x][0]= matriz[x][0].title()
                    if matriz[x][0] == y  and cont ==0: # Se for igual, exibi todas as informações
                        cont =1
                        print(f'Nome:{matriz[x][0]:<20}|Endereço:{matriz[x][1]:<35}|Telefone:{matriz[x][2]:<10}|ID:{matriz[x][3]:^5}')

    else:
        contador= 0 # Contado para saber se achou ou não o código
        procurar_codigo= str(input('Digite o código do cliente:'))
        arquivo_clientes= open('Arquivos/Cliente.txt','r')
        print('-='*30)
        #Pecorre todo o arquivo procurando o código
        for linha in arquivo_clientes: # Ler o arquivo  

            linha=linha.split('|')
            linha.pop(4)
            for x in range(len(linha)):
                linha[x]= linha[x].strip()
            if procurar_codigo == linha[3]: # Comparando o código digitado com os códigos dos clientes
                contador = 1
                print(f'Nome:{linha[0]}|Endereço:{linha[1]}|Telefone:{linha[2]}|ID:{linha[3]}')
                print('-='*30)
        if contador == 0: # Se o contador não mudar, significa que não foi achado o código
            print('Esse Id não existe')
            
        arquivo_clientes.close()

def agendarManutenção():
    clientes=lerArquivo('Arquivos/Cliente.txt') # Vai receber uma matriz com todas as linha do arquivo
    if len(clientes) == 0:
        print('-='*30)
        print('nenhum cliente foi cadastrado')
    else:
        print('-='*30)
        cont = 0 # Serve para analisar se o códio do usuário foi achado
        numeros_das_pecas=['1','2','3','4','5'] # Opções disponíveis
        manutencao ={} # Dicionário com as informações da manutenção
        informacao_da_peca=[] # Lista que vai conter o nome e o prazo da peça

        
        dia =[] 
        for x in range(1,32): # Vai preencher a lista dia
            dia.append(x)
            dia[x-1] = str(x)

        mes=[] # Preencher a lista mes 
        for x in range(1,13):
            mes.append(x)
            mes[x-1] = str(x)
        
        manutencao['Custo'] = float(input('Digite o valor da manuteção:'))

        # Ler o código da manutenção 
        codigo_da_manutecao = open('Arquivos/CódigoManutenção.txt','r')
        # Recebo o número que estiver no arquivo de codigos
        for x in  codigo_da_manutecao:
            codigo = x
        codigo_da_manutecao.close()
        codigo = int(codigo) 
        codigo +=1  # Soma mais um
        codigo= str(codigo)
        # Gera o novo código para o outro cliente
        manutencao['Código']= codigo
        codigo_da_manutecao = open('Arquivos/CódigoManutenção.txt','w')
        codigo_da_manutecao.write(codigo)
        codigo_da_manutecao.close()
        #Isso aqui já tem que está no sistema
        print('-='*30)
        nome_peca=(str(input('[1]filtro de polipropileno\n[2]cartucho carvão phb\n[3]bucha difusora completa\n[4]Bica móvel curta\n[5]Outro\nDigite o número referente a peça:')))
        
        while nome_peca not in numeros_das_pecas: # Tratamento de erro, caso não for escolhido uma das opções 
            print('-='*30)
            nome_peca=(str(input('[1]filtro de polipropileno\n[2]cartucho carvão phb\n[3]bucha difusora completa\n[4]Bica móvel curta\nDigite o número referente a peça:')))

        if nome_peca == '1':
            informacao_da_peca.append('filtro de polipropileno')
            informacao_da_peca.append('12')
        elif nome_peca == '2':
            informacao_da_peca.append('cartucho carvão phb')
            informacao_da_peca.append('6')
        elif nome_peca == '3':
            informacao_da_peca.append('bucha difusora completa')
            informacao_da_peca.append('12')
        elif nome_peca == '5': # Caso o usuário queira colocar outra peça
            informacao_da_peca.append((input('Digite o nome da peça:')))
            informacao_da_peca.append(int(input('Digite o prazo de duranção dessa peça:(meses)')))
        else:
            informacao_da_peca.append('Bica móvel curta')
            informacao_da_peca.append('Caso necessario')
        

        manutencao['Informações da Peça']=informacao_da_peca
        hoje = date.today() # Armazena a data de hoje
 
        dia_escolhido=str(input('Digite o dia da  manuteção:'))
        while dia_escolhido not in dia: # Tratamento de erro de dia, coso usuário digite um número de dia que não existe
        # Exemplo : 32
            print('-='*30)
            dia_escolhido=str(input('Digite o dia da  manuteção:'))
        # Fazer tratamento com as datas, com o prazo de manuteção
        
        dia_escolhido=int(dia_escolhido)

        mes_escolhido=str(input('Digite o número do mês da  manuteção:'))
        # Tratamento de erro do mes, coso usuário digite um número de mes que não existe
        # Exemplo: 13
        while mes_escolhido not in mes:
            print('-='*30)
            mes_escolhido=str(input('Digite o número do mês da  manuteção:'))

        mes_escolhido = int(mes_escolhido)
        
        ano_escolhido=int(input('Digite o ano da manuteção:'))
        ano_escolhido=int(ano_escolhido)

        data = date(ano_escolhido,mes_escolhido,dia_escolhido) # Transforma a data digitada em formato de data
        while data <= hoje : # Caso a data digitada seja menor ou igual que a data de hoje , ou seja, a data já passou
            print('A data escolhida não está adequada')
            print('-='*30)
            # Pede as informações de novo
            dia_escolhido=str(input('Digite o dia da  manuteção:'))
            while dia_escolhido not in dia:
                print('-='*30)
                dia_escolhido=str(input('Digite o dia da  manuteção:'))
            # Fazer tratamento com as datas, com o prazo de manuteção
            
            dia_escolhido=int(dia_escolhido)

            mes_escolhido=str(input('Digite o número do mês da  manuteção:'))
            while mes_escolhido not in mes:
                print('-='*30)
                mes_escolhido=str(input('Digite o número do mês da  manuteção:'))

            mes_escolhido = int(mes_escolhido)

            ano_escolhido=int(input('Digite o ano da  manuteção:'))
            ano_escolhido=int(ano_escolhido)
            data = date(ano_escolhido,mes_escolhido,dia_escolhido)

        # Formatação da data dia/mes/ano
        auxiliar = str(data.day)+'/' + str(data.month)+'/' + str(data.year)
        data = auxiliar 
        manutencao['Data'] = data
        
        
        id_procurar= int(input('Digite o Id do cliente:'))
        arquivo_clientes= open('Arquivos/Cliente.txt','r')
        # Vai procurar o código do cliente que foi digitado
        for linha in arquivo_clientes:
            linha=linha.split('|')
            linha.pop(4)
            for x in range(len(linha)):
                linha[x]= linha[x].strip()
            id_procurar=str(id_procurar)
            if id_procurar == linha[3]:
                cont = 1
                manutencao['Id do cliente'] = linha[3]
        arquivo_clientes.close()
        if cont ==0:
            print('Esse id não existe')
        else:
            print('-='*30)
            arquivo_manutencao= open('Arquivos/manutenção.txt','a')
            for informacao in manutencao:
                arquivo_manutencao.write(f'{manutencao[informacao]}|')
            arquivo_manutencao.write('\n')
            arquivo_manutencao.close()

        
def excluirCliente():
    print('-='*30)
    cliente= lerArquivo('Arquivos/Cliente.txt') # Matriz com as linhas do arquivo
    if len(cliente) == 0:
        print('Nenhum cliente foi cadastrado')
    else:
        ja_foram=[] # Lista com os códigos dos clientes que estão ligados a manutenções
        matrizManutenção = lerArquivo('Arquivos/manutenção.txt')
        matrizClientes = lerArquivo('Arquivos/Cliente.txt')
        novaMatriz = [] # Nova matriz com os clientes
        if len(matrizClientes) == 0:
            print('Nenhum cliente foi cadastrado ainda')
        else:
            for x in range(len(matrizClientes)):
                for y in range(len(matrizManutenção)):
                    if matrizClientes[x][3] == matrizManutenção[y][4] and matrizClientes[x][3] not in ja_foram:
                        novaMatriz.append(matrizClientes[x]) # Adiciona na nova lista de clientes
                        ja_foram.append(matrizClientes[x][3]) # Adiciona na lista de códigos de clientes que já foram analisádos


            arquivo_clientes=open('Arquivos/Cliente.txt','w')       
            # O novo arquivo Clientes é escrito, excluindo aqueles que não está ligados a nenhuma manutençãp    
            for x in range(len(novaMatriz)):
                for y in range(len(novaMatriz[x])):
                    if novaMatriz[x][y] != '':
                        arquivo_clientes.write(f'{novaMatriz [x][y]}|')
                arquivo_clientes.write('\n')
            arquivo_clientes.close()
            print('Clientes excluidos')
        

def editarManutenção():
    print('-='*30)
    manutencao = lerArquivo('Arquivos/manutenção.txt')
    if len(manutencao) == 0:
        print('Nenhuma manutenção foi cadastrada')
    else:
        matriz = []
        cont = 0
        contador = 0 # Contador de modificações
        print('-='*30)
        procurar_codigo= str(input('Digite o código da manutenção:'))
        arquivo_manutencao= open('Arquivos/manutenção.txt','r')
        print('-='*30)
        for linha in arquivo_manutencao:
            linha=linha.split('|')
            linha.pop(5)
            for x in range(len(linha)):
                linha[x]= linha[x].strip()
            if procurar_codigo == linha[1]: # Se o código digitado for igual a um dos código da manutenção vai realizar a edição
                mais_troca = 'S' # Variável usada para fazer mais de um troca ou não
                while mais_troca in 'Ss':
                    contador +=1
                    cont=1
                    if contador == 1:
                        # Transformaando a string com o nome da peça e o prazo da peça em uma lista 
                        linha[2]=linha[2].replace('\'','')
                        linha[2]=linha[2].replace('[','')
                        linha[2] =linha[2].replace(']','')
                        linha[2] = linha[2].split(',')
                    for x in range(len(linha[2])):
                        linha[2][x]=linha[2][x].strip()

                      
                    
                    print(f'Valor:{linha[0]}\nId da manutenção:{linha[1]}\nNome da peça:{linha[2][0]}\nDuração da peça:{linha[2][1]} meses\nData da manutenção:{linha[3]}\nId do cliente:{linha[4]}')

                    print('-='*30)
                    opçoes = ['1','2','3','4',] # Opções de troca
                    trocar=str(input('[1]Trocar o valor\n[2]Trocar o nome e a duração\n[3]Trocar a data da manutenção \n[4]Trocar o cliente vinculado\nEscolha a opção desejada:'))
                    # Tratamento de Erro
                    while trocar not in opçoes:
                        print('-='*30)
                        trocar=str(input('[1]Trocar o valor\n[2]Trocar o nome e a duração\n[3]Trocar a data da manutenção \n[4]Trocar o cliente vinculado\nEscolha a opção desejada:'))

                    # Mudar valor
                    if trocar == '1':


                        print(f'Valor atual da manuteção:{linha[0]}')
                        novo = float(input('Digite o novo valor:'))
                        linha[0]= novo


                    # Mudar nome da peça e duração
                    elif trocar == '2':
                        
                        informacao_da_peca = []
                        numeros_das_pecas=['1','2','3','4','5'] # Opções de número no menu das peças
                        print(f'Nome da peça e Duranção da peça:{linha[2]}')
                        print('-='*30)
                        novo= str(input('[1]filtro de polipropileno\n[2]cartucho carvão phb\n[3]bucha difusora completa\n[4]Bica móvel curta\n[5]Outro\nDigite o número referente a peça:'))
                        while novo not in numeros_das_pecas:
                            print('-='*30)
                            novo= str(input('[1]filtro de polipropileno\n[2]cartucho carvão phb\n[3]bucha difusora completa\n[4]Bica móvel curta\[5]Outro\nnDigite o número referente a peça:'))
                        if novo == '1':
                            informacao_da_peca.append('filtro de polipropileno')
                            informacao_da_peca.append('12')
                        elif novo == '2':
                            informacao_da_peca.append('cartucho carvao phb')
                            informacao_da_peca.append('6')
                        elif novo == '3':
                            informacao_da_peca.append('bucha difusora completa')
                            informacao_da_peca.append('12')
                        elif novo == '5':
                            informacao_da_peca.append((input('Digite o nome da peça:')))
                            informacao_da_peca.append(str(input('Digite o prazo de duranção dessa peça:(meses)')))
                        else:
                            informacao_da_peca.append('Bica movel curta')
                            informacao_da_peca.append('Caso necessario')
                        linha[2] = informacao_da_peca

                    # Mudar a data
                    elif trocar == '3':


                        informacao_da_peca =linha[2]
                        informacao_da_peca= list(informacao_da_peca)

                        # Algoritmo usado acima no agendamento 
                        dia =[]
                        for x in range(1,32):
                            dia.append(x)
                            dia[x-1] = str(x)

                        mes=[]
                        for x in range(1,13):
                            mes.append(x)
                            mes[x-1] = str(x)
                        
                        hoje = date.today()
                    

                        dia_escolhido=str(input('Digite o dia da sua manuteção:'))
                        while dia_escolhido not in dia:
                            print('-='*30)
                            dia_escolhido=str(input('Digite o dia da  manuteção:'))
                        # Fazer tratamento com as datas, com o prazo de manuteção
                        
                        dia_escolhido=int(dia_escolhido)

                        mes_escolhido=str(input('Digite o mês da  manuteção:'))
                        while mes_escolhido not in mes:
                            print('-='*30)
                            mes_escolhido=str(input('Digite o número do mês da  manuteção:'))

                        mes_escolhido = int(mes_escolhido)

                        ano_escolhido=int(input('Digite o ano da  manuteção:'))
                        ano_escolhido=int(ano_escolhido)

                        data = date(ano_escolhido,mes_escolhido,dia_escolhido)
                        
                        auxiliar = str(data.day)+'/' + str(data.month)+'/' + str(data.year)
                        data = auxiliar 
                        linha[3] = data


                    else:
                        contador_de_prits = 0 # Número de vezes que foi printado o cliente
                        existe_esse_Arquivo('Arquivos/Cliente.txt')
                        matrizClientes= lerArquivo('Arquivos/cliente.txt')
                        print('-='*30)
                        print(f'Id do cliente vinculado :{linha[4]}')
                        for linhaArquivo in matrizClientes: # Analisa o arquivo cliente procurando o código que está relacionado a manutenção
                            if linhaArquivo[3] == linha[4] and contador_de_prits == 0:
                                print('-='*30)
                                print(f'Cliente Vinculado')
                                print('-='*30)
                                print(f'Nome:{linhaArquivo[0]}\nEndereço:{linhaArquivo[1]}\nTelefone:{linhaArquivo[2]}\nID:{linhaArquivo[3]}')
                                contador_de_prits = 1
                                print('-='*30)
                        novoId=str(input('Digite o id do novo cliente que vai ser vinculado nessa manutenção:')) # Digita o novo id
                        contador_de_prits =0
                        for linhaArquivo in matrizClientes:
                            if linhaArquivo[3] == novoId and contador_de_prits == 0: # Se achar, é mostrado na tela
                                print('-='*30)
                                print(f'Id encontrado')
                                print('-='*30)
                                print(f'Nome:{linhaArquivo[0]}\nEndereço:{linhaArquivo[1]}\nTelefone:{linhaArquivo[2]}\nID:{linhaArquivo[3]}')
                                contador_de_prits = 1
                                print('-='*30)
                        if contador_de_prits == 0:
                            print('Id não encontrado')
                    
                        else: # Alteração do código
                            linha[4] = novoId


                    mais_troca=str(input('[S]Sim\n[N]Não\nDeseja trocar mais alguna coisa ?')) # Caso o usuário queira fazer mais troca
                    print('-='*30)
                    # Tratamento de erro
                    while mais_troca not in 'SsNn': 
                        mais_troca=str(input('[S]Sim\n[N]Não\nDeseja trocar mais alguna coisa ? Digite apenas S ou N:'))
                        print('-='*30)
                    if mais_troca in 'Nn':
                        mais_troca = 'N'

            matriz.append(linha)
        
        if cont ==0: # Se o valor de cont não for modificado, significa que não achou o código da manutenção que foi digitado
            print('ID não encontrado')
        arquivo_manutencao.close()
        #Adiciona devono no arquivo
        arquivo_manutencao= open('Arquivos/manutenção.txt','w') #Reescreve a lista de manutenção atualizada
        for x in range(len(matriz)):
            for y in range(5):
                if y != 4:
                    arquivo_manutencao.write(f'{matriz[x][y]}|')

                else:
                    arquivo_manutencao.write(f'{matriz[x][y]}|\n')
        arquivo_manutencao.close()

def excluirManutenção():
    print('-='*30)
    manutencao = lerArquivo('Arquivos/manutenção.txt')
    if len(manutencao) == 0:
        print('Nenhuma manutenção foi cadastrada')
    else:
        print('-='*30)
        cont = 0
        manutencoes=lerArquivo('Arquivos/manutenção.txt')
        id_excluir=str(input('Digite o cógido da manutenção a ser excluida:'))
        escrever = open('Arquivos/manutenção.txt','w')
        for linha in manutencoes:
            if linha[1] == id_excluir: # Se o código digitador for  mesmo que o da manutenção
                cont = 1
                # Bloco Criado apenas para exibição ficar melhor 
                linha[2]=linha[2].replace('\'','')
                linha[2]=linha[2].replace('[','')
                linha[2] =linha[2].replace(']','')
                linha[2] = linha[2].split(',')
                for x in range(len(linha[2])):
                    linha[2][x]=linha[2][x].strip()


                print('-='*30)
                print('Manutenção  removida :')
                print('-='*30)
                print(f'Valor:{linha[0]}\nId da manutenção:{linha[1]}\nNome da peça:{linha[2][0]}\nDuração da peça:{linha[2][1]} meses\nData da manutenção:{linha[3]}\nId do cliente:{linha[4]}')
                print('-='*30)
                manutencoes.remove(linha) # Remove a linha que tem o mesmo código que foi digitado
                print('-='*30)
        if cont == 0: # Se o valor de cont não for alterado, significa que não foi achado o código digitado
            print('Esse Id não existe')
        for linha in manutencoes : # Reescreve o arquivo manutenção
            escrever.write(f'{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|')
            escrever.write('\n')
        escrever.close()

def realizarManutenção():
    print('-='*30)
    manutencao = lerArquivo('Arquivos/manutenção.txt')
    if len(manutencao) == 0:
        print('Nenhuma manutenção foi cadastrada')
    else:
        remover= [] # Lista com as datas que tem que ser removida
        cont = 0
        manutencoes=lerArquivo('Arquivos/manutenção.txt')
        for linha in manutencoes:
            # Formatação para deixar as datas no formato ideal para usar a função date 
            auxiliar = linha[3]
            auxiliar = linha[3].split('/')
            dia = int(auxiliar[0])
            mes = int(auxiliar[1])
            ano = int(auxiliar[2])
            dia_da_manutenção= date(ano,mes,dia)
            hoje = date.today()

            if dia_da_manutenção == hoje: # Se a data de hoje for igual a data que está agendada, a manutenção é realizada
                cont = 1
                remover.append(linha)
        if cont == 0: # Se o valor de cont não for alterado, significa que não tem nenhuma manutenção para fazer hoje
            print('Não tem nenhuma manuteção para fazer hoje!')
        else: 
            # Adiciona essas manutenções realizadas no arquivo manutençõesRealizadas
            escrever = open('Arquivos/manutenção.txt','w')
            manutencoesRealizadas  = open('Arquivos/manutençõesRealizadas.txt','a')
            for x in range(len(remover)):
                for y in manutencoes:
                    if y == remover[x]:
                        manutencoes.remove(y)
                        print(f'A manutenção com o id {y[1]} foi realizada')
                        for t in range(len(y)):
                            if t == 5:
                                manutencoesRealizadas.write('\n')
                            else:
                                manutencoesRealizadas.write(f'{y[t]}|')
            manutencoesRealizadas.close()    
            # Reescreve o arquivo manutenção
            for linha in manutencoes:
                escrever.write(f'{linha[0]}|{linha[1]}|{linha[2]}|{linha[3]}|{linha[4]}|')
                escrever.write('\n')
            escrever.close()

        for x in range(len(remover)): # Agendamento automático
            op=str(input(f'Deseja fazer o agendamento automático da manutenção com o id {remover[x][1]}:[S/N]')).lower()
            while op not in 'sn': # Tratamento de erro
                op=str(input(f'Deseja fazer o agendamento automático da proxima manutenção:')).lower()
            if op == 's':
                informacoes = remover[x] # Salva as informações que estão na manutenção 
                codigo=lerArquivo('Arquivos/CódigoManutenção.txt')
                codigo= int(codigo[0][0])
                codigo+= 1 
                codigo = str(codigo)
                informacoes[1] = codigo # Dá um novo código a ela
                arquivo_codigo=open('Arquivos/CódigoManutenção.txt','w')
                arquivo_codigo.write(codigo)
                arquivo_codigo.close()
                #Mudar a data
                auxiliar =informacoes[2]
                auxiliar= auxiliar.replace('[','')
                auxiliar= auxiliar.replace('\'','')
                auxiliar= auxiliar.replace(']','')
                auxiliar= auxiliar.replace('\'','')
                auxiliar = auxiliar.split(',')
                if auxiliar[1] == 'Caso necessario': # Se a peça não tiver prazo de validade
                    print('Essa manutenção não tem agendamento automático')
                else:
                    # Mudando a data de acordo com o prazo de vencimento da peça
                    hoje = date.today()
                    dia = float(auxiliar[1])
                    dia *= 30.4375 # constante de número de mes que tem um ano
                    dia = int(dia) 
                    if auxiliar[1] == 12:
                        proxima_data= hoje + timedelta(days=365)
                    elif auxiliar[1] == 6:
                        proxima_data= hoje + timedelta(days=182)
                    else:
                        # Soma quantos dias tem a quantidade de meses da peça mais o dia de hoje
                        proxima_data= hoje + timedelta(days=dia)
                    auxiliar = str(proxima_data.day)+'/' + str(proxima_data.month)+'/' + str(proxima_data.year)
                    proxima_data = auxiliar
                    informacoes[3] = proxima_data

                    arquivo = open('Arquivos/manutenção.txt','a')
                    # Armazena essa manutenção no arquivo manutenção
                    for x in range(len(informacoes)):
                        if x == 5:
                            arquivo.write('\n')
                        else:
                            arquivo.write(f'{informacoes[x]}|')
def balançoDoMes():
    print('-='*30)

    meses=[]
    for x in range(1,13):
        meses.append(x)
        meses[x-1] = str(x)
    lista= [] # lista com o balaço do mes
    existe_essa_Pasta('./ArquivosUsuário') # Ver se existe a pasta ArquivosUsuário
    manutencoes=lerArquivo('Arquivos/manutençõesRealizadas.txt')
    if len(manutencoes) ==0:
            print('Nenhuma manutenção foi realizada')
    else:
        mes= str((input('Digite o número do mês que você quer filtrar:')))
        while mes not in meses:
            mes= str((input('Digite o número do mês que você quer filtrar:')))
        ano = int(input('Digite o ano que você quer filtrar:'))
        ano = str(ano)
        for linha in manutencoes:
            auxiliar = linha[3] # salvando o formato da data
            linha[3]= linha[3].split('/') # transformando a data em lista
            if linha[3][1] == mes and linha[3][2] == ano: # Se o mes e ano digitado for igual ao da data agendada 
                lista.append(linha)
            linha[3] = auxiliar
        print('-='*30)
        if len(lista) == 0:
            print('Não existe nenhuma manutenção realizada nesse mes e desse ano')
        
        else:
            total = 0
            nome= 'ArquivosUsuário/balanço '+ mes + ' de ' + ano +'.txt' # Nome do arquivo que vai ser criado
            existe_esse_Arquivo(nome) # Cria esse arquivo
            balanco= open(nome,'w') 
            contador = 0 # Variável usada para saber quantas vezes foi printado as linhas
            for x in lista:
                # Criado para uma melhor exibição
                x[2]= x[2].replace('[','')
                x[2]= x[2].replace('\'','')
                x[2]= x[2].replace(']','')
                x[2]= x[2].replace('\'','')
                x[2] = x[2].split(',')
                total += float(x[0])
                if contador == 0:  # Se for printado a primeira linha 
                    contador = 1 # Muda o valor de contador
                    print(f'Valor  |Id  |Nome da peca:             |Duracao da peca(meses):|Data:       |Id do cliente:   ')
                    print('-='*50)
                    print(f'{x[0]:<7}|{x[1]:<4}|{x[2][0]:<26}|{x[2][1]:^23}|{x[3]:<12}|{x[4]:<5}')
                    balanco.write(f'Valor  |Id  |Nome da peca:             |Duracao da peca(meses):|Data:       |Id do cliente:   \n')
                    balanco.write('-='*50)
                    balanco.write('\n')
                    balanco.write(f'{x[0]:<7}|{x[1]:<4}|{x[2][0]:<26}|{x[2][1]:^23}|{x[3]:<12}|{x[4]:<5}\n')
                elif contador == len(lista) -1: # Se chegar na ultima linha
                    print(f'{x[0]:<7}|{x[1]:<4}|{x[2][0]:<26}|{x[2][1]:^23}|{x[3]:<12}|{x[4]:<5}\n \nTotal:{total}')
                    balanco.write(f'{x[0]:<7}|{x[1]:<4}|{x[2][0]:<26}|{x[2][1]:^23}|{x[3]:<12}|{x[4]:<5}\n \nTotal:{total}\n')
                else:
                    contador +=1 # Somando mais um
                    print(f'{x[0]:<7}|{x[1]:<4}|{x[2][0]:<26}|{x[2][1]:^23}|{x[3]:<12}|{x[4]:<5}')
                    balanco.write(f'{x[0]:<7}|{x[1]:<4}|{x[2][0]:<26}|{x[2][1]:^23}|{x[3]:<12}|{x[4]:<5}\n')
            print('')
            print('Balanço realizado')
            balanco.close()


def listarManutenção():
    print('-='*30)
    op = str(input('[1]Lista de Manutenções Agendadas\n[2]Lista de Manutenções Realizadas\nDigite a opção desejada:'))
    # Tratamento de erro
    while op not in '12':
        op = str(input('[1]Lista de Manutenções Agendadas\n[2]Lista de Manutenções Realizadas\nDigite a opção desejada:'))
    if op == '1': # Exibi manutenções Agendada
        contador = 0 # Variável usada para facilitar a exibição
        manutencoesAgendadas =lerArquivo('Arquivos/manutenção.txt') 
        if len(manutencoesAgendadas) ==0:
            print('Nenhuma manutenção foi agendada')
        else:
            for linha in manutencoesAgendadas:
                # Criado para uma melhor exibição
                linha[2]= linha[2].replace('[','')
                linha[2]= linha[2].replace('\'','')
                linha[2]= linha[2].replace(']','')
                linha[2]= linha[2].replace('\'','')
                linha[2] = linha[2].split(',')
                if contador == 0:
                    contador = 1
                    print(f'Valor  |Id  |Nome da peca:             |Duracao da peca(meses):|Data:       |Id do cliente:   ')
                    print('-='*50)
                    print(f'{linha[0]:<7}|{linha[1]:<4}|{linha[2][0]:<26}|{linha[2][1]:^23}|{linha[3]:<12}|{linha[4]:<5}')
                else:
                    print(f'{linha[0]:<7}|{linha[1]:<4}|{linha[2][0]:<26}|{linha[2][1]:^23}|{linha[3]:<12}|{linha[4]:<5}')
    else: # Exibi manutenções Realizadas
        manutencoesRealizadas=lerArquivo('Arquivos/manutençõesRealizadas.txt')
        contador = 0
        if len(manutencoesRealizadas) ==0:
            print('Nenhuma manutenção foi realizada')
        else:
            for linha in manutencoesRealizadas:
                linha[2]= linha[2].replace('[','')
                linha[2]= linha[2].replace('\'','')
                linha[2]= linha[2].replace(']','')
                linha[2]= linha[2].replace('\'','')
                linha[2] = linha[2].split(',')
                if contador == 0:
                    contador = 1
                    print(f'Valor  |Id  |Nome da peca:             |Duracao da peca(meses):|Data:       |Id do cliente:   ')
                    print('-='*50)
                    print(f'{linha[0]:<7}|{linha[1]:<4}|{linha[2][0]:<26}|{linha[2][1]:^23}|{linha[3]:<12}|{linha[4]:<5}')
                else:
                    print(f'{linha[0]:<7}|{linha[1]:<4}|{linha[2][0]:<26}|{linha[2][1]:^23}|{linha[3]:<12}|{linha[4]:<5}')

def imprimirManutenção():

    contador =0
    lista_de_Datas= [] # Lista de datas ordenadas
    datas_personalizadas= [] # Lista de datas formatada ordenada
 
  
    manutencoes=lerArquivo('Arquivos/manutenção.txt')
    hoje = date.today() # Salva a data de hoje

    for linha in  manutencoes: 
        if len(manutencoes) ==0:
            print('Nenhuma manutenção foi agendada')
        else:
            auxiliar = linha[3]
            auxiliar= auxiliar.split('/')
            auxiliar[0]=int(auxiliar[0])
            auxiliar[1]=int(auxiliar[1])
            auxiliar[2]=int(auxiliar[2])
            auxiliar = date(auxiliar[2],auxiliar[1],auxiliar[0])
            lista_de_Datas.append(auxiliar)
            # Método de ordenação utilizado na aula da professora Claudia Pinto Pereira
            t = len(lista_de_Datas)
            for i in range(0, t-1):
                min = i
                for j in range(i+1, t):
                # Encontra o menor e ordena
                    if lista_de_Datas[j] < lista_de_Datas[min]:
                        min = j     
                lista_de_Datas[i], lista_de_Datas[min] = lista_de_Datas[min], lista_de_Datas[i]
            
        for data in lista_de_Datas:
            ajuda = str(data.day)+'/' + str(data.month)+'/' + str(data.year) # Formatação de data
            datas_personalizadas.append(ajuda)
        existe_essa_Pasta('./ArquivosUsuário') 
        existe_esse_Arquivo('ArquivosUsuário/manutençõesAgendadas.txt') # Cria o arquivo manutençõesAgendadas
        manutencoesAgendadas= open('ArquivosUsuário/manutençõesAgendadas.txt','w')
        for x in datas_personalizadas:
            for linha in manutencoes:
                if x == linha[3]: # Se a data organizada for igual a data que esta na manutenção, vai ser adicionado no arquivo
                    linha[2]= linha[2].replace('[','')
                    linha[2]= linha[2].replace('\'','')
                    linha[2]= linha[2].replace(']','')
                    linha[2]= linha[2].replace('\'','')
                    linha[2] = linha[2].split(',')
                    if contador == 0:
                        contador= 1
                        manutencoesAgendadas.write(f'Valor  |Id  |Nome da peca:             |Duracao da peca(meses):|Data:       |Id do cliente:   ')
                        manutencoesAgendadas.write('-='*50)
                        manutencoesAgendadas.write('\n')
                        manutencoesAgendadas.write(f'{linha[0]:<7}|{linha[1]:<4}|{linha[2][0]:<26}|{linha[2][1]:^23}|{linha[3]:<12}|{linha[4]:<5}\n')
                    else:
                        manutencoesAgendadas.write(f'{linha[0]:<7}|{linha[1]:<4}|{linha[2][0]:<26}|{linha[2][1]:^23}|{linha[3]:<12}|{linha[4]:<5}\n')




