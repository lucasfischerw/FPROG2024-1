//------  Exercício 1A  ------
Console.WriteLine("\n------  Exercício 1A  ------");
for(int i = 0; i < 100; i++) {
    Console.Write(i + 1);
    if(i != 99) {
        Console.Write(", ");
    }
}

//------  Exercício 1B  ------
Console.WriteLine("\n------  Exercício 1B  ------");
for(int i = 20; i <= 50; i++) {
    if(i % 2 == 0) {
        Console.Write(i);
        if(i != 50) {
            Console.Write(", ");
        }
    }
}

//------  Exercício 1C  ------
Console.WriteLine("\n------  Exercício 1C  ------");
for(int i = 70; i >= 25; i--) {
    Console.Write(i);
    if(i != 25) {
        Console.Write(", ");
    }
}


//------  Exercício 1D  ------
Console.WriteLine("\n------  Exercício 1D  ------");
for(int i = 95; i >= 25; i --) {
    if(i % 2 != 0) {
        Console.Write(i);
        if(i != 25) {
            Console.Write(", ");
        }
    }
}

//------  Exercício 1E  ------
Console.WriteLine("\n------  Exercício 1E  ------");
float soma = 0;
for(int i = 0; i < 15; i++) {
    Console.WriteLine("Digite um número: ");
    soma += int.Parse(Console.ReadLine()!);
}
Console.WriteLine("A soma dos números é: " + soma);
Console.WriteLine("A média dos números é: " + soma / 15);


//------  Exercício 1F  ------
Console.WriteLine("\n------  Exercício 1F  ------");
int impares = 0;
int pares = 0;
for(int i = 0; i < 10; i++) {
    Console.WriteLine("Digite um número: ");
    if(int.Parse(Console.ReadLine()!) % 2 == 0) {
        pares++;
    } else {
        impares++;
    }
}
Console.WriteLine("Quantidade de números pares: " + pares);
Console.WriteLine("Quantidade de números ímpares: " + impares);

//------  Exercício 1G  ------
Console.WriteLine("\n------  Exercício 1G  ------");
int positivos = 0;
int negativos = 0;
int nulos = 0;
for(int i = 0; i < 20; i++) {
    int sorteioNumero = new Random().Next(-10, 10);
    if(sorteioNumero == 0) {
        Console.WriteLine("NULO: " + sorteioNumero);
        nulos++;
    } else if(sorteioNumero < 0) {
        Console.WriteLine("NEGATIVO: " + sorteioNumero);
        negativos++;
    } else {
        Console.WriteLine("POSITIVO: " + sorteioNumero);
        positivos++;
    }
}
Console.WriteLine("Quantidade de números positivos: " + positivos);
Console.WriteLine("Quantidade de números negativos: " + negativos);
Console.WriteLine("Quantidade de números nulos: " + nulos);

//------  Exercício 1H  ------
Console.WriteLine("\n------  Exercício 1H  ------");
Console.WriteLine("Digite o número de números a serem lidos: ");
int numerosALer = int.Parse(Console.ReadLine()!);
int somaFinal = 0;
for(int i = 0; i < numerosALer; i++) {
    Console.WriteLine("Digite um número: ");
    somaFinal += int.Parse(Console.ReadLine()!);
}
Console.WriteLine("A soma dos números é: " + somaFinal);


//------  Exercício 2  ------
Console.WriteLine("\n------  Exercício 2  ------");
int sorteio = new Random().Next(-10, 10);
int tentativas = 3;

for(int i = 0; i < tentativas; i++) {
    Console.WriteLine("Digite um número: ");
    int numeroTentativa = int.Parse(Console.ReadLine()!);
    if(numeroTentativa == sorteio) {
        Console.WriteLine("Parabéns, você acertou!");
        break;
    } else {
        if(numeroTentativa > sorteio) {
            Console.WriteLine("O número sorteado é menor.");
        } else {
            Console.WriteLine("O número sorteado é maior.");
        }
    }
    tentativas--;
}
if(tentativas == 0) {
    Console.WriteLine("Você perdeu! O número sorteado era: " + sorteio);
}


//------  Exercício 3  ------
Console.WriteLine("\n------  Exercício 3  ------");
Console.WriteLine("Digite um número: ");
int numero = int.Parse(Console.ReadLine()!);
for(int i = 0; i <= 10; i++) {
    Console.WriteLine(numero + " x " + i + " = " + numero * i);
}


//------  Exercício 4  ------
Console.WriteLine("\n------  Exercício 4  ------");
Console.WriteLine("Entre com o valor do divisor: ");
int divisor = int.Parse(Console.ReadLine()!);
Console.WriteLine("Entre com o início do intervalo: ");
int inicio = int.Parse(Console.ReadLine()!);
Console.WriteLine("Entre com o fim do intervalo: ");
int fim = int.Parse(Console.ReadLine()!);
Console.WriteLine("Numeros divisíveis por " + divisor + " no intervalo de " + inicio + " a " + fim + ":");
for(int i = inicio; i <= fim; i++) {
    if(i % divisor == 0) {
        Console.WriteLine(i);
    }
}


//------  Exercício 5  ------
Console.WriteLine("\n------  Exercício 5  ------");
Console.WriteLine("Digite o número de alunos: ");
int alunos = int.Parse(Console.ReadLine()!);
float mediaTotal = 0;
for(int i = 0; i < alunos; i++) {
    Console.WriteLine($"Digite a nota do Grau A do aluno {i+1}:");
    float grauA = float.Parse(Console.ReadLine()!);
    Console.WriteLine($"Digite a nota do Grau B do aluno {i+1}:");
    float grauB = float.Parse(Console.ReadLine()!);

    float media = (grauA + (2 * grauB)) / 3;
    if (media >= 6) {
        Console.WriteLine($"Aprovado! Média: {media}");
    } else {
        Console.WriteLine($"Reprovado! Qual Grau deseja substituir? \na) Grau A \nb) Grau B");
        string grau = Console.ReadLine()!;
        if (grau == "a") {
            Console.WriteLine($"Digite a nota do Grau C do aluno {i+1}:");
            grauA = float.Parse(Console.ReadLine()!);
        } else {
            Console.WriteLine($"Digite a nota do Grau C do aluno {i+1}:");
            grauB = float.Parse(Console.ReadLine()!);
        }
        media = (grauA + (2 * grauB)) / 3;
        if (media >= 6) {
            Console.WriteLine($"Aprovado! Média: {media}");
        } else {
            Console.WriteLine($"Reprovado! Média: {media}");
        }
    }
    mediaTotal += media;
}
Console.WriteLine("A média da turma é: " + mediaTotal / alunos);


//------  Exercício 6  ------
Console.WriteLine("\n------  Exercício 6  ------");
int menor = 100;
int maior = 0;
int mediaNumeros = 0;
for(int i = 0; i < 5; i++) {
    int numeroSorteado = new Random().Next(0, 100);
    if(numeroSorteado < menor) {
        menor = numeroSorteado;
    }
    if(numeroSorteado > maior) {
        maior = numeroSorteado;
    }
    mediaNumeros += numeroSorteado;
}
Console.WriteLine("O menor número sorteado foi: " + menor);
Console.WriteLine("O maior número sorteado foi: " + maior);
Console.WriteLine("A média dos números sorteados foi: " + mediaNumeros / 5);


//------  Exercício 7  ------
Console.WriteLine("\n------  Exercício 7  ------");
string[] nomes = new string[5];
for(int i = 0; i < 5; i++) {
    Console.WriteLine("Digite um nome: ");
    nomes[i] = Console.ReadLine()!;
}
nomes = nomes.OrderBy(x => x).ToArray();
Console.WriteLine("Primneiro nome: " + nomes[0]);


//------  Exercício 8  ------
Console.WriteLine("\n------  Exercício 8  ------");
while(true) {
    Console.WriteLine("Digite um número: ");
    int numeroEscolhido = int.Parse(Console.ReadLine()!);
    int fatorial = numeroEscolhido;
    for(int i = numeroEscolhido - 1; i > 0; i--) {
        fatorial *= i;
    }
    Console.WriteLine("O fatorial de " + numeroEscolhido + " é: " + fatorial);
    Console.WriteLine("Deseja calcular o fatorial de outro número? (s/n)");
    if(Console.ReadLine()! == "n") {
        break;
    }
}

//------  Exercício 9  ------
Console.WriteLine("\n------  Exercício 9  ------");
Console.WriteLine("Digite um número: ");
int numeroEscolhidoCaracteres = int.Parse(Console.ReadLine()!);
Console.WriteLine("Digite um caractere: ");
string caractereEscolhido = Console.ReadLine()!;

for(int i = 0; i < numeroEscolhidoCaracteres; i++) {
    for(int j = 0; j <= i; j++) {
        Console.Write(caractereEscolhido);
    }
    Console.WriteLine();
}