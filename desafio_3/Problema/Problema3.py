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

import funcoes  #Importa as funções do arquivo funções
import os
import time
opcoes= ['1','2','3','4','5','6','7','8','9','10','11','12']# Opções do menu 
variavel = 1 # Variável para fazer o looping do menu
while variavel == 1:
    print('-='*30)
    opcao_menu=str(input('[1]Adicionar cliente\n[2]Editar Dados do cliente\n[3]Excluir Cliente\n[4]Listar Clintes\n[5]Agendar Manutenção\n[6]Editar Manuteção\n[7]Excluir Manuteção\n[8]Realizar Manuteção\n[9]Listar Manuteção\n[10]Imprimir Manuteções\n[11]Balanço do mês\n[12]Sair\nDigite a opção a ser realizada:'))

    while opcao_menu not in opcoes:# Tratamento de erro caso o usuário digite um opção diferente das opções disponíveis 
        os.system('cls')
        print('-=-'*30)
        opcao_menu=str(input('[1]Adicionar cliente\n[2]Editar Dados do cliente\n[3]Excluir Cliente\n[4]Listar Clintes\n[5]Agendar Manutenção\n[6]Editar Manuteção\n[7]Excluir Manuteção\n[8]Realizar Manuteção\n[9]Listar Manuteção\n[10]Imprimir Manuteções\n[11]Balanço do mês\n[12]Sair\nDigite apenas o número referente as operações dispoíveis :'))

    if opcao_menu == '1':
        funcoes.adicionarCliente() # Chama a função adicionarCliente

    elif opcao_menu == '2':
        funcoes.editarCliente() # Chama a função editarCliente
    elif opcao_menu == '3':
        funcoes.excluirCliente() # Chama a função excluirCliente
    elif opcao_menu == '4':
        funcoes.listarCliente() # Chama a função listarCliente
    elif opcao_menu == '5':
        funcoes.agendarManutenção() # Chama a função AgendarManutenção
    elif opcao_menu == '6':
        funcoes.editarManutenção() # Chama a função editarManutenção
    elif opcao_menu == '7':
        funcoes.excluirManutenção() # Chama a função excluirManutenção
    elif opcao_menu == '8':
        funcoes.realizarManutenção() # Chama a função realizarManutenção
    elif opcao_menu == '9':
        funcoes.listarManutenção() # Chama a função listarManutenção
    elif opcao_menu == '10':
        funcoes.imprimirManutenção() # Chama a função imprimirManutenção
    elif opcao_menu == '11':    
        funcoes.balançoDoMes() # Chama a função balançoDoMes
    else:
        variavel = 2
        print('Obrigado por utilizar o sistema')
  



