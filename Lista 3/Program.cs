using System;
using System.Globalization;
CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;


//------  Exercício 1  ------
Console.WriteLine("\n------  Exercício 1  ------");
Console.WriteLine("Digite o dividendo:");
float dividendo = float.Parse(Console.ReadLine()!);
Console.WriteLine("Digite o divisor:");
float divisor = float.Parse(Console.ReadLine()!);

if (divisor == 0) {
    Console.WriteLine("Erro! Divisão por zero não é permitida.");
} else {
    Console.WriteLine($"O resultado da divisão é: {dividendo / divisor}");
}

//------  Exercício 2  ------
Console.WriteLine("\n------  Exercício 2  ------");
Console.WriteLine("Digite o número A:");
float a = float.Parse(Console.ReadLine()!);
Console.WriteLine("Digite o número B:");
float b = float.Parse(Console.ReadLine()!);
Console.WriteLine("Digite o número C:");
float c = float.Parse(Console.ReadLine()!);

if (a + b < a + c) {
    Console.WriteLine("A + B é menor que A + C");
} else {
    Console.WriteLine("A + B é maior que A + C");
}

//------  Exercício 3  ------
Console.WriteLine("\n------  Exercício 3  ------");
Console.WriteLine("Digite um número:");
float numero = float.Parse(Console.ReadLine()!);

if (numero < 0) {
    Console.WriteLine($"O número é negativo. Seu tripo é {numero * 3}");
} else {
    Console.WriteLine($"O número é positivo. Seu dobro é {numero * 2}");
}

//------  Exercício 4  ------
Console.WriteLine("\n------  Exercício 4  ------");
Console.WriteLine("Digite um número inteiro:");
int inteiro = int.Parse(Console.ReadLine()!);

if (inteiro % 3 == 0) {
    Console.WriteLine("O número é divisível por 3 :)");
} else {
    Console.WriteLine("O número não é divisível por 3 :(");
}

//------  Exercício 5  ------
Console.WriteLine("\n------  Exercício 5  ------");
Console.WriteLine("Digite um número qualquer:");
float qualquer = float.Parse(Console.ReadLine()!);

if(qualquer % 2 == 0) {
    Console.WriteLine("O número é par.");
} else {
    Console.WriteLine("O número é ímpar.");
}

//------  Exercício 6  ------
Console.WriteLine("\n------  Exercício 6  ------");
Console.WriteLine("Escolha a sua aposta: \n   1 - Par \n   2 - Ímpar");
int aposta = int.Parse(Console.ReadLine()!);
Console.WriteLine("Digite um número de 0 a 5:");
int numeroAposta = int.Parse(Console.ReadLine()!);
Random rnd = new Random();
int sorteio   = rnd.Next(0, 5);

if (numeroAposta < 0 || numeroAposta > 5) {
    Console.WriteLine("Erro! O número da aposta deve ser de 0 a 5.");
} else {
    Console.WriteLine($"O número sorteado foi: {sorteio}");
    Console.WriteLine($"O resultado da soma é: {sorteio + numeroAposta}");
    if ((sorteio + numeroAposta) % 2 == 0) {
        if (aposta == 1) {
            Console.WriteLine("Você ganhou! O resultado é par.");
        } else {
            Console.WriteLine("Você perdeu! O resultado é par.");
        }
    } else if (aposta == 2) {
        Console.WriteLine("Você ganhou! O resultado é ímpar.");
    } else {
        Console.WriteLine("Você perdeu! O resultado é ímpar.");
    }
}

//------  Exercício 7  ------
Console.WriteLine("\n------  Exercício 7  ------");
Console.WriteLine("Digite o seu salário:");
float salario = float.Parse(Console.ReadLine()!);
if (salario * 0.11f > 318.20f) {
    Console.WriteLine("O desconto do salário é de R$ 318,20.");
} else {
    Console.WriteLine($"O desconto do salário é de R$ {salario * 0.11f}");
}

//------  Exercício 8  ------
Console.WriteLine("\n------  Exercício 8  ------");
Console.WriteLine("Digite o valor do produto:");
float valorProduto = float.Parse(Console.ReadLine()!);

if(valorProduto < 20) {
    Console.WriteLine($"O valor de venda é R$ {valorProduto * 1.45f}");
} else if(valorProduto >= 20 && valorProduto <= 50) {
    Console.WriteLine($"O valor do produto é R$ {valorProduto * 1.35f}");
} else {
    Console.WriteLine($"O valor do produto é R$ {valorProduto * 1.25f}");
}

//------  Exercício 9  ------
Console.WriteLine("\n------  Exercício 9  ------");
Console.WriteLine("Digite a cotação do dólar:");
float cotacaoDolar = float.Parse(Console.ReadLine()!);
Console.WriteLine("Digite a cotação do euro:");
float cotacaoEuro = float.Parse(Console.ReadLine()!);

Console.WriteLine("1) Converter de Real para Euro \n2) Converter de Real para Dólar \n3) Converter de Euro para Dólar\n4) Converter de Euro para Real\n5) Converter de Dólar para Euro\n6) Converter de Dólar para Real");
int opcao = int.Parse(Console.ReadLine()!);
Console.WriteLine("Digite o valor a ser convertido:");
float valor = float.Parse(Console.ReadLine()!);

if(opcao == 1) {
    Console.WriteLine($"O valor convertido é € {valor/cotacaoEuro}");
} else if(opcao == 2) {
    Console.WriteLine($"O valor convertido é $ {valor/cotacaoDolar}");
} else if(opcao == 3) {
    Console.WriteLine($"O valor convertido é $ {valor * (cotacaoEuro/cotacaoDolar)}");
} else if(opcao == 4) {
    Console.WriteLine($"O valor convertido é € {valor * cotacaoEuro}");
} else if(opcao == 5) {
    Console.WriteLine($"O valor convertido é € {valor * (cotacaoDolar/cotacaoEuro)}");
} else {
    Console.WriteLine($"O valor convertido é R$ {valor * cotacaoDolar}");
}

//------  Exercício 10  ------
Console.WriteLine("\n------  Exercício 10  ------");
Console.WriteLine("Digite o número de faces do dado:");
int faces = int.Parse(Console.ReadLine()!);
int sorteioDado = rnd.Next(1, faces + 1);
Console.WriteLine($"O número sorteado foi: {sorteioDado}");

//------  Exercício 11  ------
Console.WriteLine("\n------  Exercício 11  ------");
Console.WriteLine("Digite o valor em reais:");
float valorReais = float.Parse(Console.ReadLine()!);
int[] notas = [100, 50, 20, 10, 5, 1];
int[] quantidadeNotas = [0, 0, 0, 0, 0, 0];

for (int i = 0; i < notas.Length; i++) {
    quantidadeNotas[i] = (int) (valorReais / notas[i]);
    if(quantidadeNotas[i] > 0) {
        Console.WriteLine($"{quantidadeNotas[i]} nota(s) de R$ {notas[i]}");
    }
    valorReais = valorReais % notas[i];
}

//------  Exercício 12  ------
Console.WriteLine("\n------  Exercício 12  ------");
Console.WriteLine("Digite a idade do nadador:");
int idade = int.Parse(Console.ReadLine()!);

if(idade < 5) {
    Console.WriteLine("Categoria Inválida.");
} else if(idade >= 5 && idade <= 7) {
    Console.WriteLine("Categoria Infantil A.");
} else if(idade >= 8 && idade <= 10) {
    Console.WriteLine("Categoria Infantil B.");
} else if(idade >= 11 && idade <= 13) {
    Console.WriteLine("Categoria Juvenil A.");
} else if(idade >= 14 && idade <= 17) {
    Console.WriteLine("Categoria Juvenil B.");
} else {
    Console.WriteLine("Categoria Adulto.");
}

//------  Exercício 13  ------
Console.WriteLine("\n------  Exercício 13  ------");
Console.WriteLine("Digite a nota do Grau A:");
float grauA = float.Parse(Console.ReadLine()!);
Console.WriteLine("Digite a nota do Grau B:");
float grauB = float.Parse(Console.ReadLine()!);

float media = (grauA + (2 * grauB)) / 3;
if (media >= 6) {
    Console.WriteLine($"Aprovado! Média: {media}");
} else {
    Console.WriteLine($"Reprovado! Qual Grau deseja substituir? \na) Grau A \nb) Grau B");
    string grau = Console.ReadLine()!;
    if (grau == "a") {
        Console.WriteLine("Digite a nota do Grau C:");
        grauA = float.Parse(Console.ReadLine()!);
    } else {
        Console.WriteLine("Digite a nota do Grau C:");
        grauB = float.Parse(Console.ReadLine()!);
    }
    media = (grauA + (2 * grauB)) / 3;
    if (media >= 6) {
        Console.WriteLine($"Aprovado! Média: {media}");
    } else {
        Console.WriteLine($"Reprovado! Média: {media}");
    }
}

//------  Exercício 14  ------
Console.WriteLine("\n------  Exercício 14  ------");
Console.WriteLine("Você tem dependentes? \na) Sim \nb) Não");
string dependentes = Console.ReadLine()!;
if(dependentes == "a") {
    Console.WriteLine("Digite a idade do seu dependente:");
    int idadeDependente = int.Parse(Console.ReadLine()!);
    int custoDependente = 0;
    if(idadeDependente < 10) {
        custoDependente = 100;
    } else if(idadeDependente >= 10 && idadeDependente <= 30) {
        custoDependente = 220;
    } else if(idadeDependente > 30 && idadeDependente <= 60) {
        custoDependente = 395;
    } else {
        custoDependente = 480;
    }
    Console.WriteLine($"O custo total do seu plano é de R$ {300 + custoDependente},00");
    Console.WriteLine($"O custo do seu dependente é de R$ {custoDependente},00");
} else {
    Console.WriteLine("O custo do seu plano é de R$ 300,00");
}

//------  Exercício 15  ------
Console.WriteLine("\n------  Exercício 15  ------");
Console.WriteLine("Digite o valor do produto:");
float valorProdutoOriginal = float.Parse(Console.ReadLine()!);
Console.WriteLine("Escolha a forma de pagamento: \n   1 - À vista em dinheiro \n   2 - À vista no cartão de crédito \n   3 - Em duas vezes \n   4 - Em três vezes");
int formaPagamento = int.Parse(Console.ReadLine()!);
if(formaPagamento == 1) {
    Console.WriteLine($"O valor do produto é R$ {valorProdutoOriginal * 0.85f}");
} else if(formaPagamento == 2) {
    Console.WriteLine($"O valor do produto é R$ {valorProdutoOriginal * 0.9f}");
} else if(formaPagamento == 3) {
    Console.WriteLine($"O valor do produto é R$ {valorProdutoOriginal}");
} else {
    Console.WriteLine($"O valor do produto é R$ {valorProdutoOriginal * 1.1f}");
}

