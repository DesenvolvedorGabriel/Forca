import random

def jogar():

    imprime_mensagem_abertura()

    frutas = ["banana", "abacate", "cereja", "framboesa", "melancia", "pessego", "laranja"]
    carros = ["onix", "sandero", "prisma", "opala", "tiguan", "gol", "golf"]
    paises = ["brasil", "alemanha", "canada", "china", "colombia", "espanha", "portugal"]

    opcao_valida = False

    while (not opcao_valida):

        tema = int(input("(1) Frutas (2) Carros (3) Paises \nQual tema você deseja escolher?: "))

        if (tema == 1):

            numero_aleatorio = random.randrange(0, len(frutas))
            palavra_secreta = frutas[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        elif (tema == 2):

            numero_aleatorio = random.randrange(0, len(carros))
            palavra_secreta = carros[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        elif (tema == 3):

            numero_aleatorio = random.randrange(0, len(paises))
            palavra_secreta = paises[numero_aleatorio].upper()
            letras_acertadas = ["_" for letra in palavra_secreta]
            opcao_valida = True

        else:

            print("Opção Inválida! Escolha entre as opções disponíveis.")
            opcao_valida = False

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("A palavra tem ", len(letras_acertadas), "Letras")

    while(not acertou and not enforcou):
        chute = input("\nQual a letra?: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):

            index = 0

            for letra in palavra_secreta:

                if (chute == letra):
                    letras_acertadas[index] = letra

                index += 1

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        mensagem_ganhou()
    else:
        mensagem_perdeu(palavra_secreta)

def imprime_mensagem_abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

def mensagem_ganhou():
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
def mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))

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
if(__name__ == "__main__"):
    jogar()
