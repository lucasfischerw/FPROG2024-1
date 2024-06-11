#include <iostream>
#include <ctime>
#include <vector>
#include <locale.h>

void Exercicio1();
void Exercicio2(std::string palavra1, std::string palavra2);
void Exercicio3();
void Exercicio4();
void Exercicio5();
void Exercicio6();

int main() {
    srand((unsigned) time(0));
    setlocale(LC_ALL, "Portuguese");

    std::cout << "Exercício 1\n";
    Exercicio1();

    std::cout << "\nExercício 2\n";
    Exercicio2("asas", "casa");

    std::cout << "\nExercício 3\n";
    Exercicio3();

    std::cout << "\nExercício 4\n";
    Exercicio4();

    std::cout << "\nExercício 5\n";
    Exercicio5();

    std::cout << "\nExercício 6\n";
    Exercicio6();
}

void Exercicio1() {
    //Lê a frase digitada pelo usuário
    std::string frase;
    std::cout << "Digite uma frase: ";
    std::getline(std::cin, frase);

    //Conta a quantidade de letras na frase e de palavras
    int quantidadeLetras = 0;
    int quantidadePalavras = 1;
    for(int i = 0; i < frase.size(); i++) {
        if(isalpha(frase[i])) {
            quantidadeLetras++;
        }
        if(isspace(frase[i])) {
            quantidadePalavras++;
        }
    }

    //Imprime a quantidade de letras e palavras
    std::cout << "Quantidade de letras: " << quantidadeLetras << std::endl;
    std::cout << "Quantidade de palavras: " << quantidadePalavras << std::endl;
}

void Exercicio2(std::string palavra1, std::string palavra2) {
    //Verifica se as palavras são iguais
    if(palavra1 == palavra2) {
        std::cout << "As palavras são iguais" << std::endl;
    } else {
        //Se as palavras não são iguais, verifica qual vem antes na ordem alfabética
        if(palavra1 < palavra2) {
            std::cout << palavra1 << " vem antes de " << palavra2 << std::endl;
        } else {
            std::cout << palavra2 << " vem antes de " << palavra1 << std::endl;
        }
    }
}

void Exercicio3() {
    //Lê a frase digitada pelo usuário
    std::string frase;
    std::cout << "Digite uma frase: ";
    std::getline(std::cin, frase);

    //Trocar todos os R por L
    for(int i = 0; i < frase.size(); i++) {
        if(frase[i] == 'R') {
            frase[i] = 'L';
        } else if(frase[i] == 'r') {
            frase[i] = 'l';
        }
    }

    //Imprime a frase com os R trocados por L
    std::cout << frase << std::endl;
}

void Exercicio4() {
    //Lê a frase digitada pelo usuário
    std::string frase;
    std::cout << "Digite uma frase: ";
    std::getline(std::cin, frase);

    //Converte as letras minúsculas em maiúsculas
    for(int i = 0; i < frase.size(); i++) {
        if(islower(frase[i])) {
            frase[i] = toupper(frase[i]);
        }
    }

    //Imprime a frase com as letras minúsculas convertidas em maiúsculas
    std::cout << frase << std::endl;
}

void Exercicio5() {
    //Lê a frase digitada pelo usuário
    std::string frase;
    std::cout << "Digite uma frase: ";
    std::getline(std::cin, frase);

    //Verifica se a frase contem pelo menos uma letra maiúscula, um número e um caractere especial

    bool temMaiuscula = false;
    bool temNumero = false;
    bool temCaractereEspecial = false;

    for(int i = 0; i < frase.size(); i++) {
        if(isupper(frase[i])) {
            temMaiuscula = true;
        } else if(isdigit(frase[i])) {
            temNumero = true;
        } else if(frase[i] == '*' || frase[i] == '!' || frase[i] == '$' || frase[i] == '#') {
            temCaractereEspecial = true;
        }
    }

    if(temMaiuscula && temNumero && temCaractereEspecial) {
        std::cout << "A frase é uma senha válida" << std::endl;
    } else {
        std::cout << "A frase não é uma senha válida" << std::endl;
    }
}

void Exercicio6() {
    //Lê a frase digitada pelo usuário
    std::string frase;
    std::cout << "Digite uma frase: ";
    std::getline(std::cin, frase);

    //Verifica se uma palavra é um palíndromo
    bool palindromo = true;
    for(int i = 0; i < frase.size(); i++) {
        if(tolower(frase[i]) != tolower(frase[frase.size() - i - 1])) {
            palindromo = false;
            break;
        }
    }

    //Imprime se a palavra é um palíndromo
    if(palindromo) {
        std::cout << "A frase é um palíndromo" << std::endl;
    } else {
        std::cout << "A frase não é um palíndromo" << std::endl;
    }
}