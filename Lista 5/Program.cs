// C# - Lista 5

//------  Exercício 1  ------
Console.WriteLine("\n------  Exercício 1  ------");
void Cumprimentar(string nome) {
    Console.WriteLine($"Olá, {nome}!");
}
Cumprimentar("Mundo");


//------  Exercício 2  ------
Console.WriteLine("\n------  Exercício 2  ------");
void Tabuada(int numero) {
    for(int i = 1; i <= 10; i++) {
        Console.WriteLine($"{numero} x {i} = {numero * i}");
    }
}
Tabuada(5);

//------  Exercício 3  ------
Console.WriteLine("\n------  Exercício 3  ------");
void MediaUnisinos(float GA, int GB) {
    float media = (GA + (2 * GB)) / 3;
    if (media >= 6) {
        Console.WriteLine($"Aprovado! Média: {media}");
    } else {
        Console.WriteLine($"Reprovado! Qual Grau deseja substituir? \na) Grau A \nb) Grau B");
        string grau = Console.ReadLine()!;
        if (grau == "a") {
            Console.WriteLine("Digite a nota do Grau C:");
            float GC = float.Parse(Console.ReadLine()!);
            media = (GC + (2 * GB)) / 3;
        } else {
            Console.WriteLine("Digite a nota do Grau C:");
            float GC = float.Parse(Console.ReadLine()!);
            media = (GA + (2 * GC)) / 3;
        }
        if (media >= 6) {
            Console.WriteLine($"Aprovado! Média: {media}");
        } else {
            Console.WriteLine($"Reprovado! Média: {media}");
        }
    }
}
MediaUnisinos(5, 5);

//------  Exercício 4  ------
Console.WriteLine("\n------  Exercício 4  ------");
void Sorteio(int min, int max) {
    Random random = new Random();
    int sorteado = random.Next(min, max);
    Console.WriteLine($"Número sorteado: {sorteado}");
}
Sorteio(0, 100);


//------  Exercício 5  ------
Console.WriteLine("\n------  Exercício 5  ------");
float Somar(float n1, float n2) {
    return n1 + n2;
}
float Subtrair(float n1, float n2) {
    return n1 - n2;
}
float Multiplicar(float n1, float n2) {
    return n1 * n2;
}
float Dividir(float n1, float n2) {
    return n1 / n2;
}
void Calculadora(int opecao, float n1, float n2) {
    switch (opecao) {
        case 1:
            Console.WriteLine("A soma é " + Somar(n1, n2));
            break;
        case 2:
            Console.WriteLine("A subtração é " +Subtrair(n1, n2));
            break;
        case 3:
            Console.WriteLine("A multiplicação é " + Multiplicar(n1, n2));
            break;
        case 4:
            if(n2 == 0) {
                Console.WriteLine("Não é possível dividir por zero");
            } else {
                Console.WriteLine("A divisão é " +Dividir(n1, n2));
            }
            break;
        default:
            Console.WriteLine("Opção inválida");
            break;
    }
}

while(true) {
    Console.WriteLine("Digite a operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão");
    int opcao = int.Parse(Console.ReadLine()!);
    Console.WriteLine("Digite o primeiro número:");
    float num1 = float.Parse(Console.ReadLine()!);
    Console.WriteLine("Digite o segundo número:");
    float num2 = float.Parse(Console.ReadLine()!);
    Calculadora(opcao, num1, num2);
    Console.WriteLine("Deseja realizar outra operação? \n1 - Sim \n2 - Não");
    int continuar = int.Parse(Console.ReadLine()!);
    if(continuar == 2) {
        break;
    }
}


//------  Exercício 6  ------
Console.WriteLine("\n------  Exercício 6  ------");
void LootBox() {
    int itensComuns = 0;
    int itensRaros = 0;
    int itensLendarios = 0;
    while(true) {
        Console.WriteLine("Digite a opção desejada: \n1 - Abrir uma Caixa \n2 - Consultar Itens \n3 - Sair");
        int opcao = int.Parse(Console.ReadLine()!);
        int sorteio = new Random().Next(1, 101);
        if(opcao == 1) {
            if(sorteio == 1) {
                itensLendarios++;
                Console.WriteLine("Parabéns, você obteve um item lendário!");
            } else if(sorteio <= 19) {
                itensRaros++;
                Console.WriteLine("Você obteve um item raro!");
            } else {
                itensComuns++;
                Console.WriteLine("Você obteve um item comum.");
            }
        } else if(opcao == 2) {
            Console.WriteLine($"Itens comuns: {itensComuns} \nItens raros: {itensRaros} \nItens lendários: {itensLendarios}");
        } else if(opcao == 3) {
            break;
        }
    }
}
LootBox();
