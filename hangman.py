import csv
import random

def hangman():
    """

    :return:
    """
    level = 1
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|"]
    guess_words = get_guess_word_from_file()

    print("Welcome to Hangman")
    while level <= 3:
        wrong_guesses = 0
        guess_word = get_word(level, guess_words)
        print("\n")
        print(f'Level: {level}')

        remaining_letters = list(guess_word)
        letter_board = ["__"] * len(guess_word)
        win = False

        while wrong_guesses < len(stages)-1:
            guess = input("Guess a letter: ")
            if guess in remaining_letters:
                character_index = remaining_letters.index(guess)
                letter_board[character_index] = guess
                remaining_letters[character_index] = '$'
            else:
                wrong_guesses += 1
            print((' '.join(letter_board)))
            print('\n'.join(stages[0: wrong_guesses + 1]))
            if '__' not in letter_board:
                print(f'You win level {level}! The word was:')
                print(' '.join(letter_board))
                win = True
                break

        if win == True and level == 3:
            print('Congratulations! You win all the levels!')
            break
        elif win == True and level < 3:
            level += 1
            win = False
        else:
            # print('\n'.join(stages[0: wrong_guesses]))
            print('You lose! The words was {}'.format(guess_word))
            break

def get_guess_word_from_file():
    words = []
    with open("GuessWords.csv", "r") as file_read:
        read_words = csv.reader(file_read, delimiter=",")
        for row in read_words:
            words.append(row)

    return words

def get_word(level, words):
    row_words = words[level - 1]
    word = row_words[random.randint(0, len(row_words))]

    return word

hangman()


