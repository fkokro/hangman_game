from english_words import get_english_words_set
import random
import warnings
warnings.filterwarnings("ignore")

# Retrieve a set of English words from web2 URL: https://svnweb.freebsd.org/base/head/share/dict/web2?view=markup&pathrev=326913
web2wordrset = get_english_words_set(['web2'])

def get_word():
    word = random.choice(list(web2wordrset))
    return word.upper()

def display_hangman(tries):
    stages =[
                """
                _____
                |     |
                |     O
                |  \\-*-/
                |     |
                |    /\\
            ____|
                """,

                """
                     _____
                    |     |
                    |     O
                    |   \\-*-/
                    |     |
                    |    / 
               _____|
                """,

                """
                     _____
                    |     |
                    |     O
                    |   \\-*-/
                    |     |
                    |     
               _____|
                """,

                """
                     _____
                    |     |
                    |     O
                    |   \\-*
                    |     
                    |    
               _____|
                """,

                """
                     _____
                    |     |
                    |     O
                    |   
                    |     
                    |    
                ____|
                """,

                """
                    ______
                    |     |
                    |     
                    |   
                    |    
                    |    
                ____|
                """
            ]
    
    return stages[tries]
      
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed that letter.", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True            
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, " is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word!", word)
    else:
        print("Sorry, you ran out of guesses. The word was", word, ".")
def main():
    word  = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word
        play(word)
        

if __name__ == "__main__":
    main() 

