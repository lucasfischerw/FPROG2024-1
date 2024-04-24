# Definição da quantidade inicial de cada ingrediente
poDeFenix = 100
essenciaCelestial = 50
raizDeDragao = 45
orvalhoLunar = 30
floresSecas = 200
elixirAmargo = 20
lagrimaDeUnicornio = 15

# Função que verifica se o input entrado pelo usuário é válido
def validarInput(input, min, max):
    # Verifica se o input é diferente de vazio e se está entre o mínimo e o máximo permitido
    if input != "" and input >= min and input <= max:
        return True
    else:
        return False

# Função que exibe os ingredientes disponíveis
def mostrarIngredientesDisponiveis():
    # Alinha o texto no centro da tela
    print("-" * 49)
    print(" " * 12 + "Ingredientes Disponíveis")
    print("-" * 49)
    print("Pó de Fenix:          " + " " * 23 + str(poDeFenix) + "g")
    print("Essência Celestial:   " + " " * 23 + str(essenciaCelestial) + "ml")
    print("Raiz de Dragão:       " + " " * 23 + str(raizDeDragao) + "g")
    print("Orvalho Lunar:        " + " " * 23 + str(orvalhoLunar) + "ml")
    print("Flores Secas:         " + " " * 23 + str(floresSecas) + "g")
    print("Elixir Amargo:        " + " " * 23 + str(elixirAmargo) + "ml")
    print("Lágrima de Unicórnio: " + " " * 23 + str(lagrimaDeUnicornio) + "ml")


def criarPocao(qntPoFenix, qntEssenciaCelestial, qntRaizDragao, qntOrvalhoLunar, qntFloresSecas, qntElixirAmargo, qntLagrimaUnicornio):
    # Utiliza as variáveis globais
    global poDeFenix, essenciaCelestial, raizDeDragao, orvalhoLunar, floresSecas, elixirAmargo, lagrimaDeUnicornio

    # Define uma string para guardar os ingredientes faltantes
    ingredientesFaltantes = ""

    # Verifica se a quantidade de ingredientes é suficiente para criar a poção, para cada ingrediente
    # Se a quantidade de ingredientes for suficiente, subtrai a quantidade utilizada da quantidade disponível
    #  Se a quantidade de ingredientes for insuficiente, adiciona o ingrediente à string de ingredientes faltantes
    if poDeFenix - qntPoFenix < 0:
        ingredientesFaltantes += "\nPó de Fênix"
    else:
        poDeFenix -= qntPoFenix

    if essenciaCelestial - qntEssenciaCelestial < 0:
        ingredientesFaltantes += "\nEssência Celestial"
    else:
        essenciaCelestial -= qntEssenciaCelestial

    if raizDeDragao - qntRaizDragao < 0:
        ingredientesFaltantes += "\nRaiz de Dragão"
    else:
        raizDeDragao -= qntRaizDragao

    if orvalhoLunar - qntOrvalhoLunar < 0:
        ingredientesFaltantes += "\nOrvalho Lunar"
    else:
        orvalhoLunar -= qntOrvalhoLunar

    if floresSecas - qntFloresSecas < 0:
        ingredientesFaltantes += "\nFlores Secas"
    else:
        floresSecas -= qntFloresSecas

    if elixirAmargo - qntElixirAmargo < 0:
        ingredientesFaltantes += "\nElixir Amargo"
    else:
        elixirAmargo -= qntElixirAmargo

    if lagrimaDeUnicornio - qntLagrimaUnicornio < 0:
        ingredientesFaltantes += "\nLágrima de Unicórnio"
    else:
        lagrimaDeUnicornio -= qntLagrimaUnicornio
    
    # Se houver ingredientes faltantes, exibe a mensagem de erro e os ingredientes faltantes
    if ingredientesFaltantes != "":
        print("-" * 49)
        print(" " * 12 + "INGREDIENTES INSUFICIENTES!")
        print("-" * 49)
        print("Ingredientes Faltantes:" + ingredientesFaltantes)
        return
    
    # Se não houver ingredientes faltantes, exibe a mensagem de sucesso
    print("-" * 49)
    print(" " * 12 + "POÇÃO CRIADA COM SUCESSO!")


# Loop principal do Programa
while True:
    # Exibe o menu
    print("-" * 49)
    print("1- Preparar poção \n2- Consultar os ingredientes disponíveis \n3- Sair")
    print("-" * 49)

    # Solicita ao usuário uma opção
    opcao = int(input("Digite a opção desejada: "))

    # Verifica se a opção é válida
    if not validarInput(opcao, 1, 3):
        # Exibe mensagem de erro e solicita a opção novamente
        print("Opção inválida. Digite um número entre 1 e 3")

    # Se a opção for válida, executa a opção escolhida
    elif opcao == 1:
        print("-" * 49)
        print(" " * 15 + "Preparar nova Poção")
        print("-" * 49)

        # Define uma variável para guardar a poção escolhida e uma flag para verificar se a opção é válida
        opcaoValida = False
        pocao = 0

        # Loop para solicitar a poção desejada
        while not opcaoValida:
            print("1- Poção de Cura \n2- Poção Força da Floresta \n3- Poção Sabedoria da Riqueza \n4- Poção Sorte no Amor\n5- Poção Malvada")
            print("-" * 49)

            # Solicita ao usuário a poção desejada
            pocao = int(input("Digite a poção desejada: "))

            # Verifica se a poção é válida
            if not validarInput(pocao, 1, 5):
                print("Opção inválida. Digite um número entre 1 e 5")
            else:
                opcaoValida = True

        # Cria a poção escolhida, se a poção for válida
        # Cada poção utiliza uma quantidade específica de ingredientes, que é passada em ordem para a função criarPocao
        if pocao == 1:
            criarPocao(30, 20, 0, 0, 20, 0, 10)
        elif pocao == 2:
            criarPocao(0, 0, 30, 20, 30, 0, 0)
        elif pocao == 3:
            criarPocao(50, 30, 0, 0, 0, 0, 0)
        elif pocao == 4:
            criarPocao(0, 0, 0, 10, 50, 0, 5)
        elif pocao == 5:
            criarPocao(0, 0, 15, 0, 0, 10, 0)

    # Exibe os ingredientes disponíveis
    elif opcao == 2:
        mostrarIngredientesDisponiveis()

    # Sai do programa
    elif opcao == 3:
        break