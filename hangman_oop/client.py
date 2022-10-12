from Gams.hangman_oop.game_status import GameStatus
from Gams.hangman_oop.viselica import Game
import hungman_p

def char_list(chars):
    return ''.join(chars)


game = Game()

word = game.word_generator()

letter_count = len(word)

print(f'word consists of {letter_count} letters')
print(f'Try to guess')
# Game run loop
while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Enter a letter ')
    if len(letter) > 1:
        print('You can insert only one letter')
    elif letter in game.typed_letters:
        print('You have typed this letter')
    else:
        state = game.guess_letter(letter)
        print(char_list(state))

    print(f'Count of tries  {game.remaining_letter}')
    print(f'you have typed {char_list(game.typed_letters)}')

if game.game_status == GameStatus.LOST:
    print(hungman_p.hangman_pics[-1])
    print('Looser you have looose ')
    print(f'The word wos {game.word}')

elif game.game_status == GameStatus.WON:
    print('you have won ')
