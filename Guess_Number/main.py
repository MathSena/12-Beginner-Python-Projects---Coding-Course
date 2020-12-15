import random

# Joguinho para você tentar adivinhar um número randômico.
def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number: #Enquanto o palpite for diferente do sorteado...
        guess = int(input(f"Escolha um número entre 1 e {x}: ")) #Palpite do usuáriio
        if guess < random_number: #Se o número for abaixo.
            print("Número é maior...Tente novamente!")
        elif guess > random_number: #Se o número for acima
            print("Número é menor...Tente novamente!")

    print(f'Parabéns! Você acertou! O número é {random_number}')

guess(10)

#Palpite do computador
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c': #Enquanto o computador não acertar
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'O número {guess} é o maior(H), menor(L) ou o certo(C)?').lower()

        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f'Parabéns! O computador acertou! O número é {guess}')

computer_guess(10)