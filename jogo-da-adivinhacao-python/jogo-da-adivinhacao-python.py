# Definição lógica do jogo da adivinhação

numero_secreto = 7

# Capturando a entrada do usuário

palpite = int(input("Digite seu palpite: "))
print(f"Você digitou: {palpite}")

# Comparando e estruturando a decisão

if palpite > numero_secreto:
    print("Você errou! O seu palpite foi maior que o número secreto.")
elif palpite < numero_secreto:
    print("Você errou! O seu palpite foi menor que o número secreto.")
else:
    print("Parabéns! Você acertou o número secreto.")