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

if __name__ == "__main__":
    main()