import random
from typing import Iterable, List

from Gams.hangman_oop.game_status import GameStatus
from Gams.hangman_oop.invalid_operation_exception import InvalidOperationException
import hungman_p

class Game:
    def __init__(self, count_step: int = 6):
        if count_step < 5 or count_step > 8:
            raise ValueError('it should be between 5 and 8.')
        self.__count_step = count_step
        self.__step_count = 0
        self.__typed_letters = []
        self.__guessed_chars = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ''
        self.__hung_man_index = 0

    def word_generator(self) -> str:
        filename = 'data/WordsStockRus.txt'

        words = []
        with open(filename, encoding='UTF-8') as file:
            for i in file:
                words.append(i.strip('\n'))

        rand_index = random.randint(0, len(words) - 1)
        self.__word = words[rand_index]
        self.__guessed_chars = [False for _ in self.__word]
        self.__game_status = GameStatus.IN_PROGRESS
        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:
        if self.__step_count == self.__count_step:
            raise InvalidOperationException(f'Maximum steeps are {self.__count_step}')
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(f'Current game status {self.game_status}')

        open_any = False
        result: List[str] = []

        for i in range(len(self.word)):
            cur_letter = self.word[i]
            if cur_letter == letter:
                self.__guessed_chars[i] = True
                open_any = True

            if self.__guessed_chars[i]:
                result.append(cur_letter)
            else:
                result.append('_')

        if not open_any:
            self.__count_step -= 1
            print(hungman_p.hangman_pics[self.__hung_man_index])
            self.__hung_man_index += 1

        self.__typed_letters.append(letter)

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.__step_count == self.__count_step:
            self.__game_status = GameStatus.LOST
        return result

    def __is_winning(self):
        for cur in self.__guessed_chars:
            if not cur:
                return False
        return True

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def count_step(self) -> int:
        return self.__count_step

    @property
    def step_count(self) -> int:
        return self.__step_count

    @property
    def guessed_chars(self) -> Iterable[str]:
        return sorted(self.__guessed_chars)

    @property
    def remaining_letter(self) -> int:
        return self.__count_step - self.__step_count

    @property
    def typed_letters(self) -> Iterable[str]:
        return self.__typed_letters
