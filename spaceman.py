import random

# a list that contains the letters that qere correctly guessed
correct_letter_guessed = []

letters_guessed = []

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    correct_word = set(letters_guessed).intersection(secret_word)

    # for letter in secret_word:
    if len(correct_word) == len(secret_word):
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.
        For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessing_word = []

    for letter in secret_word:
        if letter in letters_guessed: #and letter in secret_word:
        # if letter in letters_guessed.intersection(secret_word):
            guessing_word.append(letter)
        else:
            guessing_word.append("_")

    reveal =  " ".join(guessing_word)
    print("The word is: " + reveal)



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    # if guess in secret_word:
    #     # if the guess is correct, add it to correct_letter_guessed and print statement
    #     letters_guessed.append(guess)
    #     print("Yes! You correctly guessed a letter." + '\n')
    #     return True
    # elif guess in letters_guessed:
    #     print('\n' + "Try again. You already used that letter." + '\n')
    if guess in letters_guessed:
        print('\n' + "Try again. You already used that letter." + '\n')
    elif guess in secret_word:
        letters_guessed.append(guess)
        print("Yes! You correctly guessed a letter." + '\n')
    else:
        # if guess is incorrect, add the letter to letters_guessed and print statement
        letters_guessed.append(guess)
        print("Sorry, but that is not a correct guess." + '\n')
        return False






def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    welcome_user = input("Hello! What is your name? ")

    print('\n' + welcome_user + ", welcome to Spaceman. This is a word guessing game.")
    print("There is a mystery word and the objective is to guess the word before you run out of guesses.")
    print("You have 7 guesses. You are allowed to guess only one letter at a time.")
    print("------------------------------------------------------------------------")


    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    count = 0
    while True:
        guessed_letter = input('\n' "Choosen letter is: " )

        # print(guessed_letter)
        if len(guessed_letter) > 1:
            print("Sorry, you violated the rules. Choose only ONE letter.") # make words in color red?
        else:
            print("Guessed letters: " + guessed_letter + '\n')

            #TODO: Check if the guessed letter is in the secret or not and give the player feedback
            is_guess_in_word(guessed_letter, secret_word)
            print(letters_guessed)

            #TODO: show the guessed word so far
            get_guessed_word(secret_word, letters_guessed)

            #TODO: check if the game has been won or lost

            isguessed = is_word_guessed(secret_word, letters_guessed)

            incorrect = set(letters_guessed).difference(secret_word)

            if isguessed == True:
                print("Congrats! You just won the game!")
            elif len(incorrect) == 6:
                print('\n' + "One more guess left!" + '\n')
                print("Number of incorrect guesses: " + str(len(incorrect)))
                print("----------------------------")
            elif len(incorrect) > 6:
                print('\n' + "GAME OVER!" + '\n')
                return False
            else:
                # count = count + 1
                print("Number of incorrect guesses: " + str(len(incorrect)))
                print("----------------------------")






#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
