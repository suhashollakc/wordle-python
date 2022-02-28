from letter_state import LetterState
from math import remainder

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    VOIDED_LETTER ="*"

    def __init__(self, secret:str):
        self.secret: str = secret.upper()
        self.attempts = []
        

    def attempt(self, word: str):
        word.upper()
        self.attempts.append(word)

    def guess(self, word:str):
        word.upper()

        result = [LetterState(x) for x in word] #intiialise the result array with all GREY words
        #Make a copy of secret so we can cross out used letters
        remaining_secret = list(self.secret)

        #First check for green letters.
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.is_in_position = True
                remaining_secret[i] = self.VOIDED_LETTER
        
        #Now check for yellow letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]

            #Skip this letter if it is already in position
            if letter.is_in_position:
                continue
        #Else check if the letter is in the word and void that index
    
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:   
                    remaining_secret[j] = self.VOIDED_LETTER
                    letter.is_in_word = True
                    break

        return result

    
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved