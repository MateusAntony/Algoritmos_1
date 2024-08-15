"""/*******************************************************************************
Autor: Mateus Antony Medeiros Carvalho
Componente Curricular: MI-Algoritmos
Concluido em: 20/03/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/"""
 
#Mensagem de Boas Vindas 

print('-='*30)
print('Bem Vindo ao catálogo de vacinação')
print('-='*30)

#Algumas variáveis
#OBS: algumas variáveis são autoexplicativas, mas outras eu fiz questão de esclarecer sua existência

looping = 1 #váriavel que permite que o o looping do while continue sempre, a menos que seu valor seja trocado
porcentagem_masculina = 0
porcentagem_feminina = 0 
contador_masculino=0 #reposável por contar o número de cadastro de pessoas do sexo masculino
contador_feminina=0  #reposável por contar o número de cadastro de pessoas do sexo feminino
porcentagem_de_vacinas_manhã = 0
porcentagem_de_vacinas_tarde = 0
contador_de_vacinas_manhã = 0  #reponsável por contar o número de vacinas aplicadas pela manhã
contador_de_vacinas_tarde = 0  #reponsável por contar o número de vacinas aplicadas pela tarde
porcentagem_da_coronavac=0
porcentagem_da_Astrazeneca =0
porcentagem_de_idosos_vacinados=0
contador_da_coronavac= 0 #responsável por contar o número de pessoas que recebeu a vacina coronavac 
contador_da_Astrazeneca =0 #responsável por contar o número de pessoas que recebeu a vacina da Astrazeneca
contador_de_vacinados =0 #responsável por contar o número de vacidos 
contador_da_segunda_dose = 0 #responsável por contar o número de pessoas que recebeu a 2º dose
contador_de_doses = 0 #responsável por contar o número de doses aplicadas 
contador_de_idosos_vacinados = 0 #responsável por contar o número de idosos vacinados
contador_da_primeira_dose = 0 #responsável por contar o número de pessoas que recebeu a 1º dose

#Menu:Esse bloco vai receber a operação que o usuário vai querer fazer e se o usuário digitar um valor fora de números_da_operaçao01, o programa vai solicitar que ele digite o valor de  operação novamente 
while looping == 1:
    print('[1]Registrar dados da aplicação da vacina\n[2]Visualizar relatório de vacinação\n[3]Sair')
    operação= str(input('Digite o número referente a operação que você quer fazer:'))
    números_da_operaçao01=('1','2','3') #Tupla com os valores que a variavel operação pode receber
    while operação not in números_da_operaçao01:
        print('Operação não permitida!Escreva apenas de 1 á 3!')
        operação= (input('Digite o número referente a operção que você quer fazer:'))
    print('-='*30)


    #Registro de dados da aplicação da vacina
    if operação == '1':
        print('-='*30)
        print('Cadastro de dados')
        print('-='*30)

        #Dados pessoais
        nome=(str(input('Nome:')))  
        sexo=(str(input('Sexo:')))
        sexo= sexo.lower() #responsável por deixar a variável sexo toda minúscula
        sexo_permitidos = ('masculino','feminino') #tupla com os 2 tipos de sexos permitidos 

        #Tratamento de erro dos sexo: se o usuário digitar um valor fora de sexo_permitidos, o programa vai solicitar que ele digite o valor de sexo novamente. 
        while sexo not in sexo_permitidos:
            print('Erro!Digite apenas Masculino ou feminino ')
            sexo=(str(input('Sexo:'))) 
            sexo= sexo.lower()
        #Aqui vai começar a contar o número de pessoas do sexo masculino ou feminino 
        if sexo == 'masculino':     
            contador_masculino +=1
        else:
            contador_feminina +=1 
        cpf=(int(input('Cpf:')))
        idade=(int(input('Idade:')))
        print('-='*60)


        #Grupo Prioritário:bloco responsável por receber o grupo em que a pessoa cadastrada pertence. Esse bloco vai receber o valor da variável grupo e vai verificar se a mesma está na tupla números_da_operaçao02, se ela não estiver , o programa vai pedir novamente o grupo prioritário em que a pessoa se encaixa.
        print('[1] Trabalhador da saúde,idosos com idade ≥ 75,idosos com mais de sessenta anos que vivem em asilos e instituições psiquiátricas,indígenas,aldeados, povos e comunidades ribeirinhas\n\n[2]Pessoas de 60 a 74 anos\n\n[3]Pessoas com comorbidades crônicas, transplantados e obesos\n\n[4]Trabalhadores de Educação, Pessoas com deficiência severa, membros das forças e salvamento, funcionários dos sistemas de privação de liberdades, trabalhadores do transporte coletivo, transportadores rodoviários de carga, população privada de liberdade\n')
        grupo =str(input('Qual grupo prioritário ele pertence ?(Digite o número referente): '))
        números_da_operaçao02 = ('1','2','3','4')
        while grupo not in números_da_operaçao02:
            print('DIGITE APÉNAS UM NÚMERO DE 1 Á 4')
            grupo =str(input('Qual grupo priotário ele pertence ?(Digite o número referente): '))
        print('-='*30)


        #Local de Vacinação:bloco responsável por receber a informação do local de vacinação. Esse bloco vai receber o valor da variável local e vai verificar se a mesma está na tupla números_da_operaçao03, se ela não estiver , o programa vai pedir novamente o local em que a pessoa foi vacinada.
        print('[1]USF\n[2]UBS\n[3]Posto volante em visita\n[4]Hospital\n[5]Outro')
        local = str(input('Qual foi o local de vacinação:'))
        números_da_operaçao03=('1','2','3','4','5')
        while local not in números_da_operaçao03:
            print('DIGITE APENAS NÚMEROS DE 1 Á 5')
            local = str(input('Qual foi o local de vacinação:'))
        if local == '5':
            outro_local = str(input('Qual foi esse outro local?'))
        print('-='*30)


        #Horário de vacinação:bloco responsável por receber o horário de vacinação. Esse bloco vai receber o valor da variável horário e vai transforma-lo em número real, usando formatação de string. Além disso se o horário for maior que 18 ou menor que 8 ele vai pedir que cadastre o horário novamente.
        horário = str(input('Digite o horário de vacinação:(Ex: 09:00)'))
        #Tratamento de erro, caso o usuário coloque outra formatação de horário. Ex : 9:00 
        while len(horário) <= 4 or len(horário) >5:   
             horário = str(input('Digite o horário de vacinação:(Ex: 09:00)'))
        if horário[0]== 0:
            horário= horário[1]+'.' + horário[3] + horário[4]
        else:
            horário = horário[0] + horário[1]+'.' + horário[3] + horário[4]
        while float(horário) > 18 or float(horário) < 8:
            print('Esse horário não está de acordo com os horários de vacinação ')
            horário = str(input('Digite o horário de vacinação:'))
            if horário[0]== 0:
                horário= horário[1]+'.' + horário[3] + horário[4]
            else:
                horário = horário[0] + horário[1]+'.' + horário[3] + horário[4]
            float(horário)
        print('-='*30)


        #Fabricante da vacina:bloco responsável por receber qual fabricante da vacina foi administrada. Esse bloco vai receber o valor da variável vacina e se ela não estiver em  números_da_operaçao04 vai,  o programa vai pedir novamente.Além disso ,nesse bloco ele conta o número de pessoas que recebeu cada vacina.
        print('[1]Coronavac\n[2]Astrazeneca')
        vacina=str(input('Qual fabricante da vacina foi administrada?'))
        números_da_operaçao04 = ('1','2')
        while vacina not in números_da_operaçao04:  
            print('DIGITE APENAS 1 OU 2')
            vacina=str(input('Qual fabricante da vacina foi administrada?'))
        if vacina == '1':
            contador_da_coronavac +=1
        else:
            contador_da_Astrazeneca +=1
        print('-='*30)


        #Lote:bloco responsável por receber o lote da vacina. 
        lote = int(input('Digite o lote da vacina:'))
        print('-='*30)

        #Dose:bloco responsável por receber  a dose que foi aplicada. Esse bloco vai receber o valor da variável dose e se ela não estiver em  números_da_operaçao05 vai,  o programa vai pedir novamente.Além disso ,nesse bloco a variável horário será usados para contar o número de pessoas que foi vacinadas, de acordo com o perído do dia.Nesse bloco tbm contares outro valores de variáveis mais a frente.
        dose = str(input('[1]1º Dose\n[2]2º Dose\nQual foi a dose que foi aplicada?'))
        números_da_operaçao05=('1','2')
        while dose not in números_da_operaçao05:
            print('DIGITE APENAS 1 OU 2!')
            dose = str(input('[1]1º Dose\n[2]2º Dose\nQual foi a dose que foi aplicada?'))
        contador_de_doses +=1
        horário = float(horário)
        if float(horário) >= 8 and float(horário) < 12:
            contador_de_vacinas_manhã +=1
        elif horário >=12:
            contador_de_vacinas_tarde +=1

        #Condição criada para saber o número de vacinados e contar o número de pessoas que recebeu a primeira dose
        if dose == '1':
            contador_de_vacinados +=1
            contador_da_primeira_dose += 1
            #responsável por contar o número de idosos vacinados
            if idade >= 60:
                contador_de_idosos_vacinados +=1
        #Condição criada para saber  o número de pessoas que recebeu a segunda dose, além disso , é também usado a diminuição de contadores de tipos de vacinas e de cada sexo, pois se a pessoa cadastrada tomar a segunda dose, não precisa contabilizar como mais uma pessoa vacinada, porque a mesma já está cadastrada quando tomou a primeira dose.
        if dose == '2':
            contador_da_segunda_dose += 1
            if vacina == '1':
                contador_da_coronavac -=1
            else:
                contador_da_Astrazeneca -=1
            if sexo == 'masculino':
                contador_masculino -= 1 
            else :
                contador_feminina -=1 

        print('-='*30)

    #Relatório  
    if operação == '2':
        #Cálculo de Porcentagem : coronavac,Astrazeneca,Idosos,masculino e feminino
        if contador_de_vacinados!= 0: 
            porcentagem_da_coronavac = (contador_da_coronavac*100)/contador_de_vacinados
            porcentagem_da_Astrazeneca = (contador_da_Astrazeneca*100)/contador_de_vacinados
            porcentagem_de_idosos_vacinados = (contador_de_idosos_vacinados*100)/contador_de_vacinados
            porcentagem_masculina=(contador_masculino*100)/contador_de_vacinados
            porcentagem_feminina=(contador_feminina*100)/contador_de_vacinados
        #Condição criada para não acontecer o erro de divisão por zero
        else:
            porcentagem_da_Astrazeneca = 0
            porcentagem_da_coronavac =0
            porcentagem_de_idosos_vacinados = 0
            porcentagem_masculina = 0
            porcentagem_feminina =0

        #Cálculo da porcentagem de vacinas aplicadas em cada período
        if contador_de_doses != 0:
            porcentagem_de_vacinas_manhã = (contador_de_vacinas_manhã *100)/contador_de_doses
            porcentagem_de_vacinas_tarde = (contador_de_vacinas_tarde *100)/contador_de_doses
        else:
            porcentagem_de_vacinas_manhã = 0
            porcentagem_de_vacinas_tarde = 0

        #Saída de dados:

        #número de vacinados e número de doses
        print(f'Pessoas vacinadas:{contador_de_vacinados:}              Doses aplicadas: {contador_de_doses:}')
        #número de pessoas que receberam 1º dose e número de pessoas que receberam 2º dose
        print(f'Número de pessoas que receberam a 1º dose:{contador_da_primeira_dose}           Número de pessoas que receberam a 2º dose:{contador_da_segunda_dose}')
        #percentual de cada vacina
        print(f'{round(porcentagem_da_coronavac,2)}% das pessoas receberam a coravac e {round(porcentagem_da_Astrazeneca,2)}% receberam Astrazeneca')
        #percentual de idosos
        print(f'{round(porcentagem_de_idosos_vacinados,2)}% dos vacinados é idosos')
        #percentual de vacinas aplicadas em cada período
        print(f'{round(porcentagem_de_vacinas_manhã,2)}% das vacinas foram aplicadas de manhã e {round(porcentagem_de_vacinas_tarde,2)}% foram aplicadas pela tarde ')
        #percentual de pessoas vacinadas de cada sexo
        print(f'{round(porcentagem_masculina,2 )}% das pessoas é do sexo masculino e {round(porcentagem_feminina,2)}% é do sexo feminino')

        print('-='*30)
            
    if operação == '3':
        #mudando o valor da variável looping para sair do while
        looping = 2
print('Obrigado pelo ateção!Tenha um Bom dia!')