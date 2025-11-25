import random

def iniciar_jogo():
    print("bem vindo ao jogo de adivinhação!")
numero_secreto = random.randint(1, 100)

tentativas = 0

while True:
    entrada = input("digite seu número: ")
    chute = int(entrada)
    tentativas = tentativas + 1

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif chute > numero_secreto:
        print("Seu palpite foi alto. Tente um número menor.")
    else:
        print("Seu palpite foi baixo. Tente um número maior.")

iniciar_jogo()