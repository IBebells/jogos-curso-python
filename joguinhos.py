import forquinha
import adivinhacao

print("********************************************")
print("*******Escolha o que você quer jogar!*******")
print("********************************************")

print("1-Forca 2-Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Iniciando forca")
    forquinha.jogar()
elif (jogo == 2):
    print("Iniciando adivinhação")
    adivinhacao.jogar()