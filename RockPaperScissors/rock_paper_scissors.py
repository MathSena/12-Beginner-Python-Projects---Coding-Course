import random


def play():
    user = input('Pedra, Papel ou Tesoura: ')
    computer = random.choice(['Pedra', 'Papel', 'Tesoura'])

    if user == computer:
        return 'Empate'

    if is_win(user, computer):
        return 'Você venceu!'

    return 'Você perdeu!'



def is_win(player, opponent):
    #Retorna verdadeiro se o player vencer

    if(player == 'Pedra' and opponent=='Tesoura') or (player=='Tesoura' and opponent == 'Papel') or (player == 'Papel' and opponent == 'Pedra'):
        return True
        

print(play())