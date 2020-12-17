import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # Escolha de alguma palavra na lista de forma aletatória
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letras das palavras
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Palpites do usuário
    lives = 6

    # Pegando as letras dos usuário
    while len(word_letters) > 0 and lives > 0:
        print('Você ainda possui: ', lives, 'vidas. Você já utilizou as seguintes letras: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Qual a palavra? : ', ' '.join(word_list))

        user_letter = input('Adivinha a letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # Perde vida se errar uma letra
                print('\nSua letra,', user_letter, 'Não está na palavra')

        elif user_letter in used_letters:
            print('\nVocê já utilizou a letra, por favor, tente outra.')

        else:
            print('\nEssa letra não é válida. Por favor, tente outra')

    if lives == 0:
        print('Você morreu. A palavra certa é: ', word)
    else:
        print('Sim! Você acertou!', word, '!!')


if __name__ == '__main__':
    hangman()
