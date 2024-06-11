#include <iostream>
#include <ctime>
#include <vector>
#include <locale.h>

void Exercicio1();
void Exercicio2();
void Exercicio3();

int main() {
    srand((unsigned) time(0));
    setlocale(LC_ALL, "Portuguese");

    std::cout << "Lista 6 - Estrutura de Dados\n\n";

    std::cout << "Exercício 1\n";
    Exercicio1();

    std::cout << "\nExercício 2\n";
    Exercicio2();

    std::cout << "\nExercício 3\n";
    Exercicio3();

    return 0;
}

void Exercicio1() {
    //Inicializa o vetor com tamanho 10
    int VetorAleatorio[10];

    //Variável para guardaro número de vezes que 50 aparece no vetor
    int Contador50 = 0;

    //Gera números aleatórios entre 10 e 90 e armazena no vetor
    for (int i = 0; i < 10; i++) {
        VetorAleatorio[i] = rand() % 81 + 10;
        if (VetorAleatorio[i] == 50) {
            Contador50++;
        }
    }

    //Imprime o vetor (A)
    std::cout << "Vetor: ";
    for (int i = 0; i < 10; i++) {
        std::cout << VetorAleatorio[i];
        if (i < 9) {
            std::cout << ", ";
        } else {
            std::cout << "\n";
        }
    }

    //Verifica se 50 aparece no vetor (B)
    if (Contador50 > 0) {
        std::cout << "\nO número 50 aparece no vetor.\n";
    } else {
        std::cout << "\nO número 50 não aparece no vetor.\n";
    }

    //Imprime o número de vezes que 50 aparece no vetor (C)
    std::cout << "O número 50 aparece " << Contador50 << " vezes no vetor.\n";

    //Calcular e imprimir a média dos valores (D)
    int Soma = 0;
    //Incicializar a variavel de produtório para ser utilizada depois
    int Produtorio = 1;
    for (int i = 0; i < 10; i++) {
        Soma += VetorAleatorio[i];
        Produtorio *= VetorAleatorio[i];
    }
    std::cout << "\nA média dos valores é: " << Soma / 10 << "\n";

    //Encontrar e imprimir o maior e menor valor (E)
    int Maior = 0;
    int Menor = 100;
    for(int i = 0; i < 10; i++) {
        if(VetorAleatorio[i] > Maior) {
            Maior = VetorAleatorio[i];
        }
        if(VetorAleatorio[i] < Menor) {
            Menor = VetorAleatorio[i];
        }
    }
    std::cout << "\nO maior valor é: " << Maior << "\n";
    std::cout << "O menor valor é: " << Menor << "\n";

    //Imprimir o somatório e o produtório dos valores (F)
    std::cout << "\nO somatório dos valores é: " << Soma << "\n";
    std::cout << "O produtório dos valores é: " << Produtorio << "\n";

    //Imrpimir o vetor em ordem inversa e copiar para outro vetor (G, H)
    int VetorInverso[10];
    std::cout << "\nVetor em ordem inversa: ";
    for(int i = 9; i >= 0; i--) {
        VetorInverso[i] = VetorAleatorio[i];
        std::cout << VetorAleatorio[i];
        if(i > 0) {
            std::cout << ", ";
        } else {
            std::cout << "\n";
        }
    }

    //Criar vetores para armazenar os valores pares e ímpares
    std::vector< int > vPares;
    std::vector< int > vImpares;

    for(int i = 0; i < 10; i++) {
        if(VetorAleatorio[i] % 2 == 0) {
            vPares.push_back(VetorAleatorio[i]);
        } else {
            vImpares.push_back(VetorAleatorio[i]);
        }
    }

    //Imprimir os vetores de pares e ímpares
    std::cout << "\nVetor de pares: ";
    for(int i = 0; i < vPares.size(); i++) {
        if(vPares[i] != 0) {
            std::cout << vPares[i];
            if(i < vPares.size() - 1) {
                std::cout << ", ";
            } else {
                std::cout << "\n";
            }
        }
    }

    std::cout << "\nVetor de ímpares: ";
    for(int i = 0; i < vImpares.size(); i++) {
        if(vImpares[i] != 0) {
            std::cout << vImpares[i];
            if(i < vImpares.size() - 1) {
                std::cout << ", ";
            } else {
                std::cout << "\n";
            }
        }
    }
}

void Exercicio2() {
    //Lê 5 inteiros e armazena em um vetor
    int Vetor[5];
    for(int i = 0; i < 5; i++) {
        std::cout << "Digite o " << i + 1 << "º número: ";
        std::cin >> Vetor[i];
        Vetor[i] = Vetor[i] * i;
    }

    //Imprime o vetor
    std::cout << "Vetor: ";
    for(int i = 0; i < 5; i++) {
        std::cout << Vetor[i];
        if(i < 4) {
            std::cout << ", ";
        } else {
            std::cout << "\n";
        }
    }
}

void Exercicio3() {
    //Lê o número de sorteios desejados
    int NumeroDeSorteios = 0;
    std::cout << "Digite o número de sorteios: ";
    std::cin >> NumeroDeSorteios;

    //Cria um vetor para armazenar o número de vezes que cada número foi sorteado
    int VetorVezesNumeroSorteado[6] = {0};
    for(int i = 0; i < NumeroDeSorteios; i++) {
        int NumeroSorteado = rand() % 6 + 1;
        VetorVezesNumeroSorteado[NumeroSorteado - 1]++;
    }

    //Imprime o número de vezes que cada número foi sorteado
    for(int i = 0; i < 6; i++) {
        std::cout << "O número " << i + 1 << " foi sorteado " << VetorVezesNumeroSorteado[i] << " vezes.\n";
    }
}