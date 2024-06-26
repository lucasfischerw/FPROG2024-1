import random as rd

def gerarToupeiras():
    # Iniciar a matriz com todos os elementos como '-'
    matriz = [['-' for x in range(4)] for y in range(4)]

    # Sortear 4 toupeiras
    for i in range(4):
        indexY = rd.randint(0, 3)
        indexX = rd.randint(0, 3)

        # Sortear números até achar uma posição vazia
        while matriz[indexY][indexX] == 'T':
            indexY = rd.randint(0, 3)
            indexX = rd.randint(0, 3)

        # Colocar a toupeira na matriz
        matriz[indexY][indexX] = 'T'

    # Retornar a matriz
    return matriz 

#Imprimir a matriz resultante
def imprimirMatriz(matriz):
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end="     ")
        print("\n")

# Gerar 3 matrizes
for i in range(3):
    matriz = gerarToupeiras()
    print("      Matriz ", i + 1)
    print("____________________\n")
    imprimirMatriz(matriz)
    print("\n")