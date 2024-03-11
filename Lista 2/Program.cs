//Exercício 1
Console.WriteLine("Digite o tempo em minutos: ");
float minutos = float.Parse(Console.ReadLine()!.Replace(".", ","));
int segundos = (int) (minutos * 60);
Console.WriteLine("O tempo convertido em segundos é " + segundos + "s");

//Exercício 2
Console.WriteLine("Digite a cotação atual do dólar:");
float cotacao = float.Parse(Console.ReadLine()!.Replace(".", ","));
Console.WriteLine("Digite quantos dólares você deseja obter:");
float dolares = float.Parse(Console.ReadLine()!.Replace(".", ","));
double reais = dolares * cotacao;
Console.WriteLine("Você precisará desembolsar " + reais + " reais");

//Exercício 3
Console.WriteLine("Digite o peso do prato em kg: ");
float peso = float.Parse(Console.ReadLine()!.Replace(".", ","));
double preco = 40 * peso;
Console.WriteLine("O preço do seu prato é de " + preco + " reais");

//Exercício 4
Console.WriteLine("Digite a sua nota do Grau A:");
float grau_A = float.Parse(Console.ReadLine()!.Replace(".", ","));
Console.WriteLine("Digite a sua nota do Grau B:");
float grau_B = float.Parse(Console.ReadLine()!.Replace(".", ","));
float mediaFinal = (grau_A + (2 * grau_B))/3;
Console.WriteLine("Sua média final é de: " + mediaFinal);

//Exercício 5
Console.WriteLine("Digite o preço do litro da gasolina:");
float precoLitro =  float.Parse(Console.ReadLine()!.Replace(".", ","));
Console.WriteLine("Digite quanto dinheiro você tem disponível:");
float valorDisponivel = float.Parse(Console.ReadLine()!.Replace(".", ","));
float litros = valorDisponivel/precoLitro;
Console.WriteLine("Você pode abastecer " + litros + " litros");

//Exercício 6
Console.WriteLine("Informe o número de celulares vendidos: ");
int celularesVendidos = Int32.Parse(Console.ReadLine()!);
Console.WriteLine("Informe o número de tablets vendidos: ");
int tabletsVendidos = Int32.Parse(Console.ReadLine()!);
int valorTotal = (celularesVendidos * 1000) + (tabletsVendidos * 1500);
Console.WriteLine("Total arrecadado no dia foi de " + valorTotal + " reais");

//Exercício 7
Console.WriteLine("Informe o número de passarinhos:");
int passarinhos = Int32.Parse(Console.ReadLine()!);
int gramas = 30 * passarinhos;
Console.WriteLine("Você precisa de " + gramas + " gramas de ração");

//Exercício 8
Console.WriteLine("Digite a temperatura em Fahrenheit:");
float temperatura = float.Parse(Console.ReadLine()!.Replace(".", ","));
float temperaturaConvertida = (temperatura - 32) * (5.0f/9.0f);
Console.WriteLine("A temperatura é de " + temperaturaConvertida + " graus celsius");

//Exercício 9
Console.WriteLine("Digite o valor total da compra:");
float precoCompra = float.Parse(Console.ReadLine()!.Replace(".", ",")) * 0.85f;
Console.WriteLine("O valor com desconto é " + precoCompra + " reais");

//Exercício 10
Console.WriteLine("Digite a quantidade de camisetas compradas:");
int camisetas = Int32.Parse(Console.ReadLine()!);
Console.WriteLine("Digite a quantidade de calças compradas:");
int calcas = Int32.Parse(Console.ReadLine()!);
Console.WriteLine("Digite a quantidade de cintos comprados:");
int cintos = Int32.Parse(Console.ReadLine()!);
double precoTotal = (camisetas * 25) + (calcas * 100) + (cintos * 40);
double desconto = precoTotal * 0.1;
double precoFinal = precoTotal - desconto;
Console.WriteLine("O valor do desconto é " + desconto + " reais");
Console.WriteLine("O valor total da compra é " + precoFinal + " reais");
