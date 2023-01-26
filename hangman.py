import random


list_words = ['python', 'java', 'swift', 'javascript'] # List of words
print(f"H A N G M A N")
print("")



play_cond = True # a condition so that the while loop keeps asking
win_count = 0
lose_count = 0

while play_cond:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    # if the choice is play then this starts the game
    if choice == "play":
        # this is so that the word get covered by hyphens
        hyphens = ""
        hyphens_num = 0
        word = random.choice(list_words) # to choose a random word from the list
        hyphens_num = len(word)
        hyphens = "-" * hyphens_num
        attempts = 8
        hyphens = list(hyphens) # so i can immute the list and reveal letters when needed
        word = list(word)

        letters_used = ""
        letter_used_not_in = ""
        flag = False

        while attempts != 0:

            print("".join(hyphens)) # this prints out the hyphens
            letter = input("Input a letter: ")
            # this while loop will make sure that the letter is following the correct input format
            while  not letter.isalpha() or len(letter) != 1 or not letter.islower():
                if len(letter) != 1:
                    print("Please, input a single letter.")
                elif not letter.isalpha() or not letter.islower() :
                    print("Please, enter a lowercase letter from the English alphabet.")
                print("")
                print("".join(hyphens))
                letter = input("Input a letter: ")


            if letter in word:
                if letter in letters_used:
                    print("You've already guessed this letter.")
                    print("")
                else:
                    for i in range(len(word)):
                        if letter == word[i]:
                            hyphens[i] = word[i]
                    letters_used = letter + letters_used
                    print("")
            else:
                if letter in letter_used_not_in:
                    print("You've already guessed this letter.")
                    print("")
                else:
                    print("That letter doesn't appear in the word.")
                    letter_used_not_in = letter + letter_used_not_in
                    attempts -= 1
                    print("")

            if hyphens == word:
                word = "".join(word)
                print(f"You guessed the word {word}!")
                print("You survived!")
                attempts = 0
                win_count += 1
                flag = False
            else:
                flag = True
        if flag:
            print("You lost!")
            lose_count += 1
    elif choice == "results":
        print(f"You won: {win_count} times.")
        print(f"You lost: {lose_count} times")
    elif choice == "exit":
        break










