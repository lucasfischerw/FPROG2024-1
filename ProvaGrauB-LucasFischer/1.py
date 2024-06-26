import random as rd

#Recebendo o array
array = input('Digite os números do array, separados por vírgula: ')

#Separando os elementos do array por vírgula
array = array.split(',')

#Transformando as strings em int
array = [int(i) for i in array]

print("Array digitado: ", array)

#Sorteando dois números entre 0 e index final do array, por n vezes (tamanho do array)
for i in range(len(array)):
    index = rd.randint(0, len(array)-1)
    index2 = rd.randint(0, len(array)-1)

    #Garantir que os dois index sorteados são diferentes
    while index2 == index:
        index2 = rd.randint(0, len(array)-1)

    print(str(i + 1) + ". Trocando elemento na ", index + 1, " posição com o elemento na ", index2 + 1, " posição")

    #Trocar os valores dos dois index sorteados
    valorOrginal = array[index]
    array[index] = array[index2]
    array[index2] = valorOrginal

print("Array resultante: ", array)