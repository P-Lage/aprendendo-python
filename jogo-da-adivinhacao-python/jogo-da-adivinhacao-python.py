# Modularização do jogo da adivinhação

def main():
    # Definição da lógica do jogo
    numero_secreto = 7
    tentativas = 0

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