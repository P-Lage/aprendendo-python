import random
import time

def main():
    # Definição da lógica do jogo
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    inicio = time.time()

    print("Bem-vindo ao jogo da adivinhação!")
    print("O objetivo do jogo é adivinhar o número secreto que está entre 1 e 100.")

    # Laço de repetição contendo o jogo
    while True:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Palpite inválido! Digite apenas números inteiros.")
            continue

        tentativas += 1
        print(f"Seu palpite foi: {palpite}")

        if palpite > numero_secreto:
            print("Você errou! O número secreto é menor.")
        elif palpite < numero_secreto:
            print("Você errou! O número secreto é maior.")
        else:
            print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    main()