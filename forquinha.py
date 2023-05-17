import random
 
def jogar():

    imprime_introducao()
    palavras = ler_palavras()
    palavra_secreta = seleciona_palavra(palavras)
    tracinhos = ["_" for letra in palavra_secreta]

    ganhou = False
    enforcado = False
    erros = 0

    print(tracinhos)

    while(not enforcado and not ganhou):
        letra_palpite = recebe_letra()

        if(letra_palpite in palavra_secreta):

            compara_letra(palavra_secreta, letra_palpite, tracinhos)
        
        else:
            erros += 1
            desenha_forca(erros)

        #ganha ou perde
        enforcado = erros == 7
        ganhou = "_" not in tracinhos #acertou a palavra

        print(tracinhos)

    if(ganhou):
        imprime_mensagem_vitoria(palavra_secreta)
    else:
        imprime_mensagem_derrota(palavra_secreta)
        
    print("Fim do jogo")

def imprime_introducao():
    print('----------------------------')
    print('---Welcome Jogo da Forca!---')
    print('----------------------------')


def ler_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    return palavras

def seleciona_palavra(palavras):
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta

def recebe_letra():
    letra_palpite = input("Digite uma letra ")
    letra_palpite = letra_palpite.strip().lower()
    return letra_palpite

def compara_letra(palavra_secreta, letra_palpite, tracinhos):
    index = 0
    for letra in palavra_secreta:

        if (letra_palpite == letra):
            tracinhos[index] = letra
        index += 1
    return tracinhos

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vitoria(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_derrota(palavra_secreta):
    print("Que pena, você perdeu e foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")

if(__name__ == "__main__"):
    jogar()