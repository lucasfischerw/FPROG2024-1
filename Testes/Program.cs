int[] posHamsters = [0, 0];

void AtualizaPosicaoHamster(int sorteio, int hamster) {
    if(sorteio == 1) {
        posHamsters[hamster] += 1;
    } else if(sorteio == 2) {
        posHamsters[hamster] += 2;
    } else if(sorteio == 4 && posHamsters[hamster] > 0) {
        posHamsters[hamster] -= 1;
    } else if(sorteio == 5 && posHamsters[hamster] > 1) {
        posHamsters[hamster] -= 2;
    }
}

while (posHamsters[0] < 12 && posHamsters[1] < 12) {
    AtualizaPosicaoHamster(new Random().Next(1, 5), 0);
    AtualizaPosicaoHamster(new Random().Next(1, 5), 1);
    Console.WriteLine($"Posição do hamster 1: {new string('-', posHamsters[0])}");
    Console.WriteLine($"Posição do hamster 2: {new string('-', posHamsters[1])}");
    Console.WriteLine("-----------");
}

if (posHamsters[0] >= 12) {
    Console.WriteLine("O hamster 1 venceu!");
} else {
    Console.WriteLine("O hamster 2 venceu!");
}