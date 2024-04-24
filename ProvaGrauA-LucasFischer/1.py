def divisivelPor2(numero):
    # Verifica se o resto da divisão do número por 2 é 0
    if numero % 2 == 0:
        # Retorna verdadeiro caso o resto seja 0, ou seja, o número é divisível por 2
        return True
    else:
        # Retorna falso caso o número não seja divisível por 2
        return False
