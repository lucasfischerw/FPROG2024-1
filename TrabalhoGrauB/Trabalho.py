import csv

#Abre o arquivo CSV e lê os dados
arquivoCSV = open('Gatos.csv', encoding='utf-8')
leitor = csv.reader(arquivoCSV, delimiter=',')
dados = list(leitor)

opcaoSelecionadaMenu = 0        #Guarda a opção selecionada no menu
felinoCadastrado = []           #Guarda os dados do felino que está sendo cadastrado

#Converte os valores numéricos para inteiros e sobrescreve os valores na lista
for i in range(len(dados)):
    linha = []
    for j in range(len(dados[0])):
        if dados[i][j].isnumeric():
            linha.append(int(dados[i][j]))
        else:
            linha.append(dados[i][j].strip())

    dados[i] = linha

def mostrarMenu():
    global opcaoSelecionadaMenu
    #Mostra o menu
    print('-' * 20 + '    MENU    ' + '-' * 20)
    print('1 - Cadastrar felino\n2 - Alterar status de felino\n3 - Consultar informações sobre felino\n4 - Apresentar estatísticas gerais\n5 - Filtragem de dados\n6 - Salvar\n7 - Sair')
    print('-' * 52)
    #Pede para o usuário digitar a opção desejada e verifica se é válida
    while True:
        opcaoSelecionadaMenu = input('Digite a opção desejada: ')
        if opcaoSelecionadaMenu == '' or not opcaoSelecionadaMenu.isnumeric() or int(opcaoSelecionadaMenu) < 1 or int(opcaoSelecionadaMenu) > 7:
            print('Opção inválida, tente novamente')
            continue
        else:
            opcaoSelecionadaMenu = int(opcaoSelecionadaMenu)
            break

#Função para verificar se o input do usuário condiz com o tipo/formato esperado
def verificaInput(pergunta, tipoEsperado = 'string'):
    while True:
        resposta = input(pergunta)
        if resposta == '':                          #Se o usuário pressionar enter, deixa o campo em branco
            felinoCadastrado.append('-')
            break
        elif tipoEsperado == 'bool':                #Se o tipo esperado for booleano, verifica se a resposta é S ou N
            if resposta != 'S' and resposta != 'N': #Se não for, pede para o usuário digitar novamente
                print('Valor inválido, tente novamente ou pressione enter para deixar em branco')
                continue
            else:
                if resposta == 'S':                 #Se for S, adiciona 'Sim' ao campo
                    felinoCadastrado.append('Sim')
                else:                               #Se for N, adiciona 'Não' ao campo
                    felinoCadastrado.append('Não')
                break
        elif tipoEsperado == 'int':                 #Se o tipo esperado for numérico, verifica se a resposta é numérica
            if not resposta.isnumeric():            #Se não for, pede para o usuário digitar novamente
                print('Valor inválido, tente novamente ou pressione enter para deixar em branco')
                continue
            else:                                   #Se for, adiciona o valor convertido para inteiro ao campo
                felinoCadastrado.append(int(resposta))
                break
        elif tipoEsperado == 'date':                #Se o tipo esperado for data, verifica se a resposta tem o formato correto
            if len(resposta) != 10 or resposta[2] != '/' or resposta[5] != '/' or not resposta.split('/')[1].isnumeric() or not resposta.split('/')[0].isnumeric() or int(resposta.split('/')[1]) > 12 or int(resposta.split('/')[1]) < 1 or int(resposta.split('/')[0]) > 31 or int(resposta.split('/')[0]) < 1:
                print('Data inválida, tente novamente ou pressione enter para deixar em branco')
                continue
            else:                                   #Se tiver o formato correto, adiciona a resposta ao campo
                felinoCadastrado.append(resposta)
                break
        else:                                       #Se o tipo esperado for string, adiciona a resposta ao campo
            felinoCadastrado.append(resposta)
            break

#Função para salvar as mudanças no arquivo CSV
def salvarMudancas():
    with open('Gatos.csv', mode='w', newline='') as arquivoCSV:
        escritor = csv.writer(arquivoCSV, delimiter=',')
        for i in range(len(dados)):
            escritor.writerow(dados[i])
    print('Dados salvos com sucesso!')

while True:
    #Mostra o menu e guarda a opção selecionada
    opcaoSelecionadaMenu = 0
    mostrarMenu()

    #Verifica a opção selecionada
    if opcaoSelecionadaMenu == 1:

        #Cadastrar felino
        felinoCadastrado = []
        print('-' * 15 + '    NOVO CADASTRO    ' + '-' * 16)
        print('* Responda ou pressione enter para deixar em branco')

        #Pede para o usuário digitar as informações do novo felino e verifica se estão corretas
        for i in range(0, len(dados[0])):
            if i == 5 or i == 6 or i == 7 or i == 9 or i == 10:     #Campos booleanos
                verificaInput(dados[0][i] + ' (S/N): ', 'bool')
            elif i == 2: #Idade                                     #Campos numéricos
                verificaInput(dados[0][i] + ': ', 'int')
            elif i == 8 or i == 11 or i == 14 or i == 15 or i == 16:#Campos de data
                verificaInput(dados[0][i] + ' (DD/MM/AAAA): ', 'date')
            else:                                                   #Campos de texto
                verificaInput(dados[0][i] + ': ')
        
        #Adiciona o felino cadastrado à lista de dados
        dados.append(felinoCadastrado)
        print('-' * 52)
        print('Felino cadastrado com sucesso!')

    elif opcaoSelecionadaMenu == 2:

        #Alterar status de felino
        print('-' * 12 + '    FELINOS CADASTRADOS    ' + '-' * 13)

        #Mostra os nomes dos felinos, ignorando o cabeçalho
        if len(dados) == 1:
            print('Nenhum felino cadastrado')
            print('-' * 52)
            input('Pressione enter para continuar...')
            continue
        
        print('* Selecione um felino para alterar alguma informação')
        for i in range(1, len(dados)):
            print(str(i) + ' - ' + dados[i][0])
        print('-' * 52)

        #Pede para o usuário digitar o número do felino que deseja alterar e verifica se é válido
        while True:
            felinoSelecionado = input('Digite o número do felino desejado: ')
            if felinoSelecionado == '' or not felinoSelecionado.isnumeric() or int(felinoSelecionado) < 1 or int(felinoSelecionado) >= len(dados):
                print('Opção inválida, tente novamente')
                continue
            else:
                felinoSelecionado = int(felinoSelecionado)
                break

        #Mostra as informações do felino selecionado até que o usuário decida voltar ao menu
        while True:
            print('-' * 14 + '    STATUS DO FELINO    ' + '-' * 14)

            #Imprime as informações do felino selecionado
            for i in range(0, len(dados[0])):
                if i < 10:
                    print(' ' + str(i) + ' - ' + dados[0][i] + ': ' + str(dados[felinoSelecionado][i]))
                else:
                    print(str(i) + ' - ' + dados[0][i] + ': ' + str(dados[felinoSelecionado][i]))
            print(len(dados[0]), '- Voltar ao menu')
            print('-' * 52)

            #Pede para o usuário digitar a informação que deseja alterar e verifica se é válida
            while True:
                informacaoAMudar = input('Digite uma opção: ')
                if informacaoAMudar == '' or not informacaoAMudar.isnumeric() or int(informacaoAMudar) < 0 or int(informacaoAMudar) > len(dados[0]):
                    print('Opção inválida, tente novamente')
                    continue
                else:
                    informacaoAMudar = int(informacaoAMudar)
                    break
            
            #Se o usuário decidir voltar ao menu, sai do loop
            if informacaoAMudar == len(dados[0]):
                break
            
            #Pede para o usuário digitar a nova informação e verifica se está correta
            felinoCadastrado = []
            if informacaoAMudar == 5 or informacaoAMudar == 6 or informacaoAMudar == 7 or informacaoAMudar == 9 or informacaoAMudar == 10:
                verificaInput(dados[0][informacaoAMudar] + ' (S/N): ', 'bool')
            elif informacaoAMudar == 2:
                verificaInput(dados[0][informacaoAMudar] + ': ', 'int')
            elif informacaoAMudar == 8 or informacaoAMudar == 11 or informacaoAMudar == 14 or informacaoAMudar == 15 or informacaoAMudar == 16:
                verificaInput(dados[0][informacaoAMudar] + ' (DD/MM/AAAA): ', 'date')
            else:
                verificaInput(dados[0][informacaoAMudar] + ': ')

            dados[felinoSelecionado][informacaoAMudar] = felinoCadastrado[0]
            print('Informação alterada com sucesso!')
            
    elif opcaoSelecionadaMenu == 3:

        #Consultar informações sobre felino
        print('-' * 12 + '    FELINOS CADASTRADOS    ' + '-' * 13)

        if len(dados) == 1:
            print('Nenhum felino cadastrado')
            print('-' * 52)
            input('Pressione enter para continuar...')
            continue

        for i in range(1, len(dados)):                          #Mostra os nomes dos felinos, ignorando o cabeçalho
            print(str(i) + ' - ' + dados[i][0])
        print('-' * 52)

        #Pede para o usuário digitar o número do felino que deseja consultar e verifica se é válido
        while True:
            felinoSelecionado = input('Digite o número do felino desejado: ')
            if felinoSelecionado == '' or not felinoSelecionado.isnumeric() or int(felinoSelecionado) < 1 or int(felinoSelecionado) >= len(dados):
                print('Opção inválida, tente novamente')
                continue
            else:
                felinoSelecionado = int(felinoSelecionado)
                break

        #Mostra as informações do felino selecionado
        print('-' * 16 + '    INFORMAÇÕES    ' + '-' * 17)
        for i in range(len(dados[0])):
            print(dados[0][i] + ': ' + str(dados[felinoSelecionado][i]))
        print('-' * 52)

        #Aguarda o usuário pressionar enter para retornar ao menu
        input('Pressione enter para continuar...')

    elif opcaoSelecionadaMenu == 4:

        #Inicializa as variáveis que guardarão as estatísticas
        machosFemeas = [0, 0]
        adotadosNaoAdotados = [0, 0]
        negativosParaFIVFeLV = 0
        negativosFIV = 0
        negativosFeLV = 0
        positivosFIVFeLV = 0

        #Varre a lista de dados e conta a quantidade de felinos que correspondem a cada categoria
        for i in range(1, len(dados)):
            if dados[i][1] == 'M':
                machosFemeas[0] += 1
            elif dados[i][1] == 'F':
                machosFemeas[1] += 1
            if dados[i][9] == 'Sim':
                adotadosNaoAdotados[0] += 1
            elif dados[i][9] == 'Não':
                adotadosNaoAdotados[1] += 1
                
            if dados[i][6] == 'Não' and dados[i][7] == 'Não':
                negativosParaFIVFeLV += 1
            elif dados[i][6] == 'Não':
                negativosFIV += 1
            elif dados[i][7] == 'Não':
                negativosFeLV += 1
            else:
                positivosFIVFeLV += 1

        #Imprime as estatísticas gerais
        print('-' * 16 + '    ESTATÍSTICAS    ' + '-' * 16)
        if len(dados) == 1:
            print('Nenhum felino cadastrado')
            print('-' * 52)
            input('Pressione enter para continuar...')
            continue

        
        print('Porcentagem de machos:', round(machosFemeas[0] / (machosFemeas[0] + machosFemeas[1]) * 100, 2), '%')
        print('Porcentagem de fêmeas:', round(machosFemeas[1] / (machosFemeas[0] + machosFemeas[1]) * 100, 2), '%')
        print('Porcentagem de adotados:', round(adotadosNaoAdotados[0] / (adotadosNaoAdotados[0] + adotadosNaoAdotados[1]) * 100, 2), '%')
        print('Porcentagem de não adotados:', round(adotadosNaoAdotados[1] / (adotadosNaoAdotados[0] + adotadosNaoAdotados[1]) * 100, 2), '%')
        #Apresentar porcentagem de testados negativos para FIV e FeLV, apenas FIV, apenas FeLV e positivos para ambos
        print('Porcentagem de testados negativos para FIV e FeLV:', round(negativosParaFIVFeLV / (len(dados) - 1) * 100, 2), '%')
        print('Porcentagem de testados negativos para FIV:', round(negativosFIV / (len(dados) - 1) * 100, 2), '%')
        print('Porcentagem de testados negativos para FeLV:', round(negativosFeLV / (len(dados) - 1) * 100, 2), '%')
        print('Porcentagem de testados positivos para FIV e FeLV:', round(positivosFIVFeLV / (len(dados) - 1) * 100, 2), '%')

        print('-' * 52)

        #Aguarda o usuário pressionar enter para retornar ao menu
        input('Pressione enter para continuar...')

    elif opcaoSelecionadaMenu == 5:

        #Filtragem de dados
        print('-' * 13 + '    FILTRAGEM DE DADOS    ' + '-' * 13)
        print('1 - Filtrar por período de resgate')
        print('2 - Filtrar por período de adoção')
        print('-' * 52)

        #Pede para o usuário digitar a opção desejada e verifica se é válida
        while True:
            filtragemSelecionada = input('Digite a opção desejada: ')
            if filtragemSelecionada == '' or not filtragemSelecionada.isnumeric() or int(filtragemSelecionada) < 1 or int(filtragemSelecionada) > 2:
                print('Opção inválida, tente novamente')
                continue
            else:
                filtragemSelecionada = int(filtragemSelecionada)
                break
        
        #Pede para o usuário digitar o período desejado e verifica se é válido
        dataInicial = input('Digite o ano de início: ')
        while len(dataInicial) != 4 or not dataInicial.isnumeric():
            print('Ano inválido, tente novamente')
            dataInicial = input('Digite ano de início: ')
        dataFinal = input('Digite ano final: ')
        while len(dataFinal) != 4 or not dataFinal.isnumeric():
            print('Ano inválido, tente novamente')
            dataFinal = input('Digite ano final: ')

        #Converte as datas para inteiros
        dataInicial = int(dataInicial)
        dataFinal = int(dataFinal)

        #Cria uma lista para guardar os felinos que correspondem aos critérios de filtragem
        felinosCorrespondentes = []
        if filtragemSelecionada == 1:
            for i in range(1, len(dados)):
                if dados[i][8] != '-' and int(dados[i][8].split('/')[2]) >= dataInicial and int(dados[i][8].split('/')[2]) <= dataFinal:
                    felinosCorrespondentes.append(dados[i][0])
        else:
            for i in range(1, len(dados)):
                if dados[i][11] != '-' and int(dados[i][11].split('/')[2]) >= dataInicial and int(dados[i][11].split('/')[2]) <= dataFinal:
                    felinosCorrespondentes.append(dados[i][0])

        print('-' * 52)

        #Imprime os felinos que correspondem aos critérios de filtragem
        if len(felinosCorrespondentes) == 0:
            print('Nenhum felino corresponde aos critérios de filtragem')
        else:
            if filtragemSelecionada == 1:
                print('Felinos resgatados entre', dataInicial, 'e', dataFinal)
            else:
                print('Felinos adotados entre', dataInicial, 'e', dataFinal)
            for i in range(len(felinosCorrespondentes)):
                print(felinosCorrespondentes[i])
        
        print('-' * 52)

        #Aguarda o usuário pressionar enter para retornar ao menu
        input('Pressione enter para continuar...')
                    
    elif opcaoSelecionadaMenu == 6:
        #Salvar mudanças no arquivo
        salvarMudancas()
    elif opcaoSelecionadaMenu == 7:
        #Sair e salvar
        salvarMudancas()
        print('Saindo do programa...')
        break
