import random

posJogador1 = 0
posJogador2 = 0

nroJogadores = 0
jogadorDaVez = 1

jogadoresMortos = False

filhosJogador1 = 0
filhosJogador2 = 0

jogador1Casado = False
jogador2Casado = False

jogador1Divorciado = False
jogador2Divorciado = False

jogador1Famoso = False
jogador2Famoso = False

dinheiroJogador1 = 0
dinheiroJogador2 = 0

proximaVezPerdida = False

def Roleta():
    #Função que sorteia um número de 1 a 6
    return random.randint(1, 6)
    
def Dado(nJogador):
    #Função que simula o lançamento de um dado
    global posJogador1, posJogador2, proximaVezPerdida
    if Roleta() == 1:
        #Se o número sorteado for 1, o jogador avança 1 casa
        print("Avançou 1 casa!")
        if nJogador == 1:
            posJogador1 += 1
        else:
            posJogador2 += 1
    elif Roleta() == 3:
        #Se o número sorteado for 3, o jogador volta 1 casa
        print("Voltou 1 casa")
        if nJogador == 1:
            posJogador1 -= 1
        else:
            posJogador2 -= 1
    elif Roleta() == 6 and nroJogadores == 2:
        #Se o número sorteado for 6, o jogador perde a vez
        print("Perdeu a vez.")
        proximaVezPerdida = True
    else:
        #Se o número sorteado for 2, 4 ou 5, o jogador não avança nem volta
        print("Não avançou nem voltou.")

    
def Morrer(nJogador):
    #Função que simula a morte de um jogador e exibe informações sobre o jogador
    if nroJogadores == 2:
        if nJogador == 1:
            print("Jogador 1 morreu. Jogador 2 ganhou.")
            print("Número de filhos do Jogador 1: ", filhosJogador1)
            if jogador1Casado:
                print("Jogador 1 era casado.")
            else:
                print("Jogador 1 não era casado.")
            if jogador1Divorciado:
                print("Jogador 1 era divorciado.")
            else:
                print("Jogador 1 não era divorciado.")
            if jogador1Famoso:
                print("Jogador 1 era famoso.")
            else:
                print("Jogador 1 não era famoso.")
            print("Dinheiro do Jogador 1: ", dinheiroJogador1, "reais.")
        else:
            print("Jogador 2 morreu. Jogador 1 ganhou.")
            print("Número de filhos do Jogador 2: ", filhosJogador2)
            if jogador2Casado:
                print("Jogador 2 era casado.")
            else:
                print("Jogador 2 não era casado.")
            if jogador2Divorciado:
                print("Jogador 2 era divorciado.")
            else:
                print("Jogador 2 não era divorciado.")
            if jogador2Famoso:
                print("Jogador 2 era famoso.")
            else:
                print("Jogador 2 não era famoso.")
            print("Dinheiro do Jogador 2: ", dinheiroJogador2, "reais.")
    else:
        print("Jogador 1 morreu. Você perdeu.")
        print("Número de filhos do Jogador 1: ", filhosJogador1)
        if jogador1Casado:
            print("Jogador 1 era casado.")
        else:
            print("Jogador 1 não era casado.")
        if jogador1Divorciado:
            print("Jogador 1 era divorciado.")
        else:
            print("Jogador 1 não era divorciado.")
        if jogador1Famoso:
            print("Jogador 1 era famoso.")
        else:
            print("Jogador 1 não era famoso.")
        print("Dinheiro do Jogador 1: ", dinheiroJogador1, "reais.")

    global jogadoresMortos
    jogadoresMortos = True

def Primo(numero):
    #Função que verifica se um número é primo
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
        
    return True

def Primos(numeroFinal):
    #Função que exibe os números primos até um número final
    print("Numeros Primos até", numeroFinal, ":")
    for i in range(1, numeroFinal):
        if Primo(i):
            print(str(i) + ", ", end="")

    print("")

def Somatorio(ini, fim):
    #Função que calcula o somatório de um intervalo
    soma = 0
    for i in range(ini, fim+1):
        soma += i
    return soma

def Fibonacci(n):
    #Função que calcula o n-ésimo número da sequência de Fibonacci
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
def AreaCirculo(raio):
    #Função que calcula a área de um círculo
    return 3.14 * raio**2

def Fatorial(n):
    #Função que calcula o fatorial de um número
    if n == 0:
        return 1
    else:
        return n * Fatorial(n-1)
    
def Div25(n):
    #Função que verifica se um número é divisível por 2 e 5 ao mesmo tempo
    if n > 0 and n % 2 == 0 and n % 5 == 0:
        return True
    else:
        return False

def DesafioMatematico(nJogador):
    #Função que simula um desafio matemático
    print("Desafio Matemático")
    numeroSorteado = Roleta()
    if numeroSorteado == 1:
        #Exibir números primos até 100
        Primos(100)
    elif numeroSorteado == 2:
        #Exibir o somatório de 1 a 10
        print("O somatório é: ", Somatorio(1, 10))
    elif numeroSorteado == 3:
        #Exibir o 10º número da sequência de Fibonacci
        print("O fibonacci é: ", Fibonacci(10))
    elif numeroSorteado == 4:
        #Exibir a área de um círculo de raio 2.5
        print("A área do círculo é: ", AreaCirculo(2.5))
    elif numeroSorteado == 5:
        #Exibir o fatorial de 5
        print("O fatorial é: ", Fatorial(5))
    elif numeroSorteado == 6:
        #Exibir os primeiros 5 números divisíveis por 2 e 5
        numerosDivisiveis = 0
        numeroAtual = 0
        while numerosDivisiveis < 5:
            if Div25(numeroAtual):
                print("Número divisível por 2 e 5: ", numeroAtual)
                numerosDivisiveis += 1
            numeroAtual += 1

def Formatura(nJogador):
    #Função que simula a formatura de um jogador, sorteando um curso
    print("Parabéns! Você se formou!")
    numeroSorteado = Roleta()
    if numeroSorteado == 1:
        print("Seu curso foi de Engenharia.")
    elif numeroSorteado == 2:
        print("Seu curso foi de Medicina.")
    elif numeroSorteado == 3:
        print("Seu curso foi de Direito.")
    elif numeroSorteado == 4:
        print("Seu curso foi de Administração.")
    elif numeroSorteado == 5:
        print("Seu curso foi de Ciência da Computação.")
    elif numeroSorteado == 6:
        print("Seu curso foi de ADS :)")

def TerFilhos(nJogador):
    #Função que simula o nascimento de um filho, com 1/6 de chance de serem gêmeos
    global filhosJogador1, filhosJogador2
    print("Parabéns! Você teve um filho!")
    numeroSorteado = Roleta()
    if numeroSorteado == 5:
        print("E são gêmeos!")
        if nJogador == 1:
            filhosJogador1 += 2
        else:
            filhosJogador2 += 2
    else:
        if nJogador == 1:
            filhosJogador1 += 1
        else:
            filhosJogador2 += 1

def Casar(nJogador):
    #Função que simula o casamento de um jogador e altera seu status
    global jogador1Casado, jogador2Casado
    print("Parabéns! Você casou!")
    if nJogador == 1:
        jogador1Casado = True
    else:
        jogador2Casado = True

def FicarFamoso(nJogador):
    #Função que simula a fama de um jogador e altera seu status
    global jogador1Famoso, jogador2Famoso
    print("Parabéns! Você ficou famoso!")
    if nJogador == 1:
        jogador1Famoso = True
    else:
        jogador2Famoso = True

def Divorciar(nJogador):
    #Função que simula o divórcio de um jogador e altera seu status
    global jogador1Divorciado, jogador2Divorciado, jogador1Casado, jogador2Casado
    if nJogador == 1 and jogador1Casado:
        jogador1Casado = False
        jogador1Divorciado = True
        print("Você se divorciou.")
    elif nJogador == 2 and jogador2Casado:
        jogador2Casado = False
        jogador2Divorciado = True
        print("Você se divorciou.")
    else:
        print("Você não pode se divorciar, pois não é casado.")

def Loteria(nJogador):
    #Função que simula a vitória na loteria e altera o dinheiro do jogador
    #O valor ganho depende do número sorteado
    global dinheiroJogador1, dinheiroJogador2
    print("Parabéns! Você ganhou na loteria!")
    numeroSorteado = Roleta()
    if numeroSorteado == 1:
        print("Você ganhou 2.5 reais!")
        if nJogador == 1:
            dinheiroJogador1 += 2.5
        else:
            dinheiroJogador2 += 2.5
    elif numeroSorteado == 2:
        print("Você ganhou 5000 reais!")
        if nJogador == 1:
            dinheiroJogador1 += 5000
        else:
            dinheiroJogador2 += 5000
    elif numeroSorteado == 3:
        print("Você ganhou 50000 reais!")
        if nJogador == 1:
            dinheiroJogador1 += 50000
        else:
            dinheiroJogador2 += 50000
    elif numeroSorteado == 4:
        print("Você ganhou 500000 reais!")
        if nJogador == 1:
            dinheiroJogador1 += 500000
        else:
            dinheiroJogador2 += 500000
    elif numeroSorteado == 5:
        print("Você ganhou 5000000 reais!")
        if nJogador == 1:
            dinheiroJogador1 += 5000000
        else:
            dinheiroJogador2 += 5000000
    elif numeroSorteado == 6:
        print("Você ganhou 100000000 reais!")
        if nJogador == 1:
            dinheiroJogador1 += 100000000
        else:
            dinheiroJogador2 += 100000000

def NovoAmor(nJogador):
    #Função que simula o encontro de um novo amor e altera o status do jogador
    #O jogador deve estar divorciado ou solteiro para encontrar um novo amor
    global jogador1Divorciado, jogador2Divorciado, jogador1Casado, jogador2Casado
    if nJogador == 1 and jogador1Divorciado and not jogador1Casado:
        print("Parabéns! Você encontrou um novo amor!")
        jogador1Divorciado = False
        jogador1Casado = True
    elif nJogador == 2 and jogador2Divorciado and not jogador2Casado:
        print("Parabéns! Você encontrou um novo amor!")
        jogador2Divorciado = False
        jogador2Casado = True
    else:
        print("Você não pode encontrar um novo amor")

def Resetar(nJogador):
    #Função que reseta as informações do jogador e o coloca de volta no início
    global posJogador1, posJogador2, filhosJogador1, filhosJogador2, jogador1Casado, jogador2Casado, jogador1Divorciado, jogador2Divorciado, jogador1Famoso, jogador2Famoso, dinheiroJogador1, dinheiroJogador2
    if nJogador == 1:
        posJogador1 = 0
        filhosJogador1 = 0
        jogador1Casado = False
        jogador1Divorciado = False
        jogador1Famoso = False
        dinheiroJogador1 = 0
    else:
        posJogador2 = 0
        filhosJogador2 = 0
        jogador2Casado = False
        jogador2Divorciado = False
        jogador2Famoso = False
        dinheiroJogador2 = 0
    print("Você voltou ao Início!")

def ExecutarAcaoCasa(nJogador, posicao):
    #Função que executa a ação da casa em que o jogador caiu
    if posicao == 1 or posicao == 3 or posicao == 10 or posicao == 17:
        #Rodar o dado
        print("Caiu no dado!")
        Dado(nJogador)

    elif posicao == 2 or posicao == 8 or posicao == 18:
        #Morrer
        print("Caiu na casa de morte!")
        Morrer(nJogador)
    
    elif posicao == 4 or posicao == 11 or posicao == 19:
        #Desafio Matemático
        print("Caiu na casa de desafio matemático!")
        DesafioMatematico(nJogador)
    elif posicao == 5:
        #Formatura
        print("Caiu na casa de formatura!")
        Formatura(nJogador)

    elif posicao == 6 or posicao == 9 or posicao == 13:
        #Ter Filhos
        print("Caiu na casa de ter filhos!")
        TerFilhos(nJogador)
    
    elif posicao == 7:
        #Casar
        print("Caiu na casa de casamento!")
        Casar(nJogador)

    elif posicao == 15:
        #Ficar Famoso
        print("Caiu na casa de ficar famoso!")
        FicarFamoso(nJogador)

    elif posicao == 12:
        #Divorciar
        print("Caiu na casa de divórcio!")
        Divorciar(nJogador)

    elif posicao == 14:
        #Loteria
        print("Caiu na casa da loteria!")
        Loteria(nJogador)

    elif posicao == 16:
        #Novo Amor
        print("Caiu na casa de novo amor!")
        NovoAmor(nJogador)

    elif posicao == 20:
        #Resetar
        print("Caiu na casa de resetar!")
        Resetar(nJogador)

def DesenhaTabuleiro():
    #Função que desenha o tabuleiro com a posição dos jogadores
    print(" " * 12, end="")
    print("-" * 69, end="")
    print("")
    if posJogador1 == 0:
        print("Jogador 1   |    X   ", end="")
    else:
        print("Jogador 1   | INÍCIO ", end="")
    for i in range(1, 21):
        if posJogador1 == i:
            if i <= 9:
                print("|X", end="")
            else:
                print("|X ", end="")
        else:
            print("|" + str(i), end="")

    print("| FINAL |")

    print(" " * 12, end="")
    print("-" * 69, end="")
    print("")
    #Se houverem dois jogadores, desenhar o tabuleiro do jogador 2
    if nroJogadores == 2:
        if posJogador2 == 0:
            print("Jogador 2   |    X   ", end="")
        else:
            print("Jogador 2   | INÍCIO ", end="")
        for i in range(1, 21):
            if posJogador2 == i:
                if i <= 9:
                    print("|X", end="")
                else:
                    print("|X ", end="")
            else:
                print("|" + str(i), end="")

        print("| FINAL |")
        print(" " * 12, end="")
        print("-" * 69)


while True:
    #Loop para pedir o número de jogadores, até inserir um número válido
    nroJogadores = input("Digite o número de jogadores: ")
    if not nroJogadores.isdigit() or nroJogadores == "":
        print("Número de jogadores inválido. Digite Novamente.")
    else:
        nroJogadores = int(nroJogadores)
        if nroJogadores < 1 or nroJogadores > 2:
            print("Número de jogadores inválido. Digite Novamente.")
        else:
            break

while not jogadoresMortos:
    #Loop principal do jogo
    if proximaVezPerdida:
        #Reseta a variável que indica se a próxima vez será perdida
        proximaVezPerdida = False

    #Imprime qual jogador é o da vez
    if jogadorDaVez == 1:
        print("Jogador 1, é a sua vez.")
    else:
        print("Jogador 2, é a sua vez.")

    #Espera o jogador pressionar Enter para jogar o dado
    input("Pressione Enter para jogar o dado.")
    numeroSorteado = Roleta()

    if jogadorDaVez == 1:
        #Move o jogador 1
        posJogador1 += numeroSorteado
        print("Numero Sorteado:", numeroSorteado)
        if posJogador1 > 20:
            #Se o jogador ultrapassar a casa final, ele é colocado na casa final e ganha
            posJogador1 = 20
            print("PARABÉNS! VOCÊ CHEGOU AO FINAL!")
            print("Jogador 1 ganhou!")
            break
        #Desenha o tabuleiro e executa a ação da casa
        DesenhaTabuleiro()
        ExecutarAcaoCasa(1, posJogador1)
    else:
        #Move o jogador 2
        posJogador2 += numeroSorteado
        print("Numero Sorteado:", numeroSorteado)
        if posJogador2 > 20:
            #Se o jogador ultrapassar a casa final, ele é colocado na casa final e ganha
            posJogador2 = 20
            print("PARABÉNS! VOCÊ CHEGOU AO FINAL!")
            print("Jogador 2 ganhou!")
            break
        #Desenha o tabuleiro e executa a ação da casa
        DesenhaTabuleiro()
        ExecutarAcaoCasa(2, posJogador2)

    #Altera o jogador da vez
    if nroJogadores == 2:
        #Se houverem dois jogadores, alterna entre eles, exceto se a próxima vez for perdida
        if jogadorDaVez == 1 and not proximaVezPerdida:
            jogadorDaVez = 2
        elif jogadorDaVez == 2 and not proximaVezPerdida:
            jogadorDaVez = 1