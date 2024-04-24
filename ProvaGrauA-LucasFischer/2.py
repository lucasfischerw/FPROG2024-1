def divisivelPorN(dividendo, divisor):
    # Escreve mensagem de erro caso o divisor seja 0
    if divisor == 0:
        print("Não é possível dividir por 0")
        return False

    # Verifica se o resto da divisão do número por 2 é 0
    if dividendo % divisor == 0:
        return True
    else:
        #Retorna falso caso o número não seja divisível
        return False
