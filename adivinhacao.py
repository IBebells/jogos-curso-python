import random

def jogar():
    print('----------------------------')
    print('Welcome Jogo da Adivinhação!')
    print('----------------------------')

    print("1-Fácil 2-Médio 3-Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        quant_tentativas = 25
    elif (nivel == 2):
        quant_tentativas = 10
    else:
        quant_tentativas = 5

    pontos = 1000
    numero_secreto = random.randrange(1,101)
    rodada = 1

    while(rodada <= quant_tentativas):

        print("Essa é a sua tentiva {} de {}".format(rodada, quant_tentativas))
        chute = int(input("Digite o seu palpite entre 1 a 100: "))
        print("Você digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos! Parabéns ^^".format(pontos))
            break

        elif(rodada ==  quant_tentativas):
            pontos_perdidos = abs(numero_secreto - chute)
            print("Que pena! Você errou! O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            break

        else:
            if (maior):
                print("Que pena! Você errou! Tente um número menor.")
            elif (menor):
                print("Que pena! Você errou! Tente um número maior.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()