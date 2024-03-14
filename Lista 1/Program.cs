//------  Exercício 1  ------
//Console.WriteLine("Hello World"); ---> C#
//print ('Hello World')  ---> Python
//println!("Hello World"); ---> Rust

//------  Exercício 2  ------
//Solicitar o nome do usuário
Console.WriteLine("Digite seu nome: ");
string? nome = Console.ReadLine();
//Escrever mensagem de boas vindas na tela
Console.WriteLine("Olá, " + nome + "!");

//------  Exercício 3  ------
//Escreve a pergunta na tela
Console.WriteLine("Qual é o verdadeiro nome do super-herói Batman?");
//Define as opções de resposta
string[] options = ["a) Bruce Wayne", "b) Clark Kent", "c) Peter Parker", "d) Tony Stark", "e) Steve Rogers"];
//Armazena a resposta correta
string respostaCorreta = "a";
//Escreve as opções na tela
for(int i = 0; i < options.Length; i++) {
    Console.WriteLine(options[i]);
}
//Captura a resposta do usuário
Console.WriteLine("Escolha sua resposta: ");
string resposta = Console.ReadLine()!.ToLower();
if(resposta == respostaCorreta) {
    Console.WriteLine("Parabéns! Você acertou :)");
}
Console.WriteLine("Você respondeu alternativa " + resposta + ". A alternativa correta é a alternativa " + respostaCorreta);

//------  Exercício 4  ------
//Usando um array com as opções de alternativas e um loop for para escrever as alternativas no console, como feito acima