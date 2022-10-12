import random

hangman_pics = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
    |
    |
    |
   ===''', '''
+---+
  0 |
    |
    |
   ===''', '''
+---+
  0 |
  | |
    |
   ===''', '''
+---+
  0 |
 /| |
    |
   ===''', '''
+---+
  0 |
 /|\|
    |
   ===''', '''
+---+
  0 |
 /|\|
 /  |
   ===''', '''
+---+
  0 |
 /|\|
 / \|
   ===''']
words = ['абажур', 'аббат', 'аббатство', 'аббревиатура', 'абвер', 'абзац', 'абиогенез', 'абитуриент',
         'аблактировка', 'аболиционизм', 'аболиционист', 'абонемент', 'абонент', 'абордаж',
         'абориген', 'аборт', 'абразив', 'абракадабра', 'абрек']


def get_random_word(wordlist) -> str:
    word_index = random.randint(0, len(words) - 1)
    return words[word_index]


# Displays hangman_oop , guessed letters and incorrect letters
def display_bord(missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()

    print('Incorrect letters.', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)

    for n in range(len(secret_word)):
        if secret_word[n] in correct_letters:
            blanks = blanks[:n] + secret_word[n] + blanks[n + 1:]
    print('Guessed letters')
    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed) -> str:
    while True:
        print('enter a char')
        guess_chr = input()
        if len(guess_chr) != 1:
            print('please enter a char')
        elif guess_chr in already_guessed:
            print('You have already tipped this char')
        elif guess_chr not in 'абвгдеёзжийклмнопрстуфхцчшщъыьэюя':
            print('Please enter a char')
        else:
            return guess_chr


def play_again() -> bool:
    print('do you wont play again')
    return input().lower().startswith('y')


print('HANGMAN')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_status = False

# Game loop
while True:
    display_bord(missed_letters, correct_letters, secret_word)
    guess = get_guess(missed_letters+correct_letters)

    if guess in secret_word:
        correct_letters += guess

        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f'yes secret word is {secret_word} you have won ')
            game_status = True
    else:
        missed_letters += guess

        if len(missed_letters) == len(hangman_pics) - 1:
            display_bord(missed_letters, correct_letters, secret_word)
            game_status = True

        if game_status:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_status = False
                secret_word = get_random_word(words)
            else:
                break
