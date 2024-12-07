# codigo para jogo da forca

import random
from os import system, name


def limpa_tela():
    # windows
    if name == "nt":
        _ = system("cls")

    # mac ou linux
    else:
        _ = system("clear")


# funçao
def game():

    limpa_tela()

    print("Bem ao Jogo da Forca")
    print("Adivinhe uma palavra")

    # lista de palavras
    palavras = ["banana", "uva", "abacate", "morango", "laranja"]

    # escolha da palavra randomicamente
    palavra = random.choice(palavras)
    letras_descobertas = ["_" for letra in palavra]

    # numero de chances
    chances = 6

    # lista de letras erradas
    letras_erradas = []

    # loop quanto numero de chances for maior do zero
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # tentativa
        tentativa = input("\nDigite uma letra:").lower()

        # condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # condicional
        if "_" not in letras_descobertas:
            print("Parabéns, você venceu! A palavra era: ", palavra)
            break

    if "_" in letras_descobertas:
        print("Você perdeu! A palavra era: ", palavra)


# bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. O projeto foi concluído")
