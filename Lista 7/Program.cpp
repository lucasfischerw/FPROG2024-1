#include <iostream>
#include <ctime>
#include <vector>
#include <locale.h>

void Exercicio1();
void Exercicio2();
void Exercicio3();
void Exercicio4();
void Exercicio5();
void Exercicio6();
void Exercicio7();

int main() {
    srand((unsigned) time(0));
    setlocale(LC_ALL, "Portuguese");

    std::cout << "Lista 7 - Estrutura de Dados Bidimensionais\n\n";

    std::cout << "Exercício 1\n";
    Exercicio1();

    std::cout << "\nExercício 2\n";
    Exercicio2();

    std::cout << "\nExercício 3\n";
    Exercicio3();

    std::cout << "\nExercício 4\n";
    Exercicio4();

    std::cout << "\nExercício 5\n";
    Exercicio5();

    std::cout << "\nExercício 6\n";
    Exercicio6();

    std::cout << "\nExercício 7\n";
    Exercicio7();

    return 0;

}

int matriz[3][5];

void Exercicio1() {
    //Inicializa os vetores unidiomensionais
    int vet1[5] = {1, 5, 9, 2, 5};
    int vet2[5] = {7, 4, 13, 21, 6};
    int vet3[5] = {8, -3, 5, 7, 12};

    //Inicializa a matriz bidimensional
    for(int i = 0; i < 5; i++) {
        matriz[0][i] = vet1[i];
        matriz[1][i] = vet2[i];
        matriz[2][i] = vet3[i];
    }

    //Imprime a matriz
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 5; j++) {
            std::cout << matriz[i][j] << "\t";
        }
        std::cout << std::endl;
    }
}

void Exercicio2() {
    //Mutiplicar todos os elementos da matriz por 7
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 5; j++) {
            matriz[i][j] *= 7;
        }
    }

    //Imprime a matriz
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 5; j++) {
            std::cout << matriz[i][j] << "\t";
        }
        std::cout << std::endl;
    }
}

void Exercicio3() {
    //Cria uma matriz 4x4
    int matriz[4][4];

    //Cria uma matriz identidade
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(i == j) {
                matriz[i][j] = 1;
            } else {
                matriz[i][j] = 0;
            }
        }
    }

    //Imprime a matriz identidade
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            std::cout << matriz[i][j] << "\t";
        }
        std::cout << std::endl;
    }
}

int matrizAleatoria[4][6];

void Exercicio4() {
    //Preenche a matriz com números aleatórios entre -10 e 10
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 6; j++) {
            matrizAleatoria[i][j] = rand() % 21 - 10;
        }
    }

    //Imprime a matriz
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 6; j++) {
            std::cout << matrizAleatoria[i][j] << "\t";
        }
        std::cout << std::endl;
    }

    //Faz a soma dos elementos da segunda linha
    int somaLinha2 = 0;
    for(int i = 0; i < 6; i++) {
        somaLinha2 += matrizAleatoria[1][i];
    }
    std::cout << "A soma dos elementos da segunda linha é: " << somaLinha2 << std::endl;

    //Faz a soma dos elementos da quinta coluna
    int somaColuna5 = 0;
    for(int i = 0; i < 4; i++) {
        somaColuna5 += matrizAleatoria[i][4];
    }
    std::cout << "A soma dos elementos da quinta coluna é: " << somaColuna5 << std::endl;

    //Faz a mutiplicação dos elementos da primeira linha pelos elementos da quarta linha
    int produtoLinhas = 0;
    for(int i = 0; i < 6; i++) {
        produtoLinhas += matrizAleatoria[0][i] * matrizAleatoria[3][i];
    }
    std::cout << "O produto dos elementos da primeira linha pelos elementos da quarta linha é: " << produtoLinhas << std::endl;

    //Faz a soma dos elementos das colunas com índice par
    int somaColunasPar = 0;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 6; j++) {
            if(j % 2 == 0) {
                somaColunasPar += matrizAleatoria[i][j];
            }
        }
    }
    std::cout << "A soma dos elementos das colunas com índice par é: " << somaColunasPar << std::endl;

    //Faz a soma dos elementos das linhas com índice ímpar
    int somaLinhasImpar = 0;
    for(int i = 0; i < 4; i++) {
        if(i % 2 != 0) {
            for(int j = 0; j < 6; j++) {
                somaLinhasImpar += matrizAleatoria[i][j];
            }
        }
    }
    std::cout << "A soma dos elementos das linhas com índice ímpar é: " << somaLinhasImpar << std::endl;
}

void Exercicio5() {
    //Encontra o maior e o menor valor da matriz gerada no exercício anterior
    int maior = 0;
    int menor = 200;

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 6; j++) {
            if(matrizAleatoria[i][j] > maior) {
                maior = matrizAleatoria[i][j];
            }
            if(matrizAleatoria[i][j] < menor) {
                menor = matrizAleatoria[i][j];
            }
        }
    }

    std::cout << "O maior valor da matriz é: " << maior << std::endl;
    std::cout << "O menor valor da matriz é: " << menor << std::endl;
}

void Exercicio6() {
    float matrizNotas[10][3];
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 2; j++) {
            //Gera uma nota aleatória entre 0 e 10 com duas casas decimais
            matrizNotas[i][j] = rand() % 1001 / 100.0;
        }
        matrizNotas[i][2] = (matrizNotas[i][0] + (2 * matrizNotas[i][1])) / 3;
    }

    //Imprime a matriz
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 3; j++) {
            std::cout << matrizNotas[i][j] << "\t";
        }
        std::cout << std::endl;
    }

    std::cout << std::endl;
    
    //Imprime a média de cada aluno
    for(int i = 0; i < 10; i++) {
        std::cout << "A média do aluno " << i + 1 << " é: " << matrizNotas[i][2] << std::endl;
    }
}

void Exercicio7() {
    int matriz[5][5];
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            //Gera um número aleatório entre -1000 e 1000
            matriz[i][j] = rand() % 2001 - 1000;
        }
    }

    std::cout << "Matriz original\n";

    //Imprime a matriz
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            std::cout << matriz[i][j] << "\t";
        }
        std::cout << std::endl;
    }

    //Troca o sinal dos elementos da matriz
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            matriz[i][j] *= -1;
        }
    }

    std::cout << "\nMatriz com sinal trocado\n";

    //Imprime a matriz
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            std::cout << matriz[i][j] << "\t";
        }
        std::cout << std::endl;
    }
}