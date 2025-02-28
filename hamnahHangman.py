words = ("objective", "bias", "evidence", "pineapple", "curiousity", "perspective", "marginalized", "potential", "opinion", "information", "justice",
         "networking", "communication", "relationships", "background", "authentic", "indigenous", "resilience", "scolarship")
import random
hangman_avatar = {0:("   ",
                     "   ",
                     "   "),
                  1:(" o ",
                     "   ",
                     "   "),
                  2:(" o ",
                     " | ",
                     "   "),
                  3:(" o ",
                     "/| ",
                     "   "),
                  4:(" o ",
                     "/|\\",
                     "   "),
                  5:(" o ",
                     "/|\\",
                     "/  "),
                  6:(" o ",
                     "/|\\",
                     "/ \\")}
def display_avatar(wrong_guesses):
    for line in hangman_avatar[wrong_guesses]:
        print(line)

    
def displayHint(hint):
    print (" ".join(hint))
def displayAns(answer):
    print (" ".join(answer))
def mainBody():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    lettersGuessed =[]
    running = True

    while running:
        display_avatar(wrong_guesses)
        displayHint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input, write one letter please")
            continue

        if guess in lettersGuessed:
            print(f"{guess} is already guessed")

        lettersGuessed.append(guess)


        
        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses +=1

        if "_" not in hint:
            display_avatar(wrong_guesses)
            displayAns(answer)
            print("You win!!")
            running = False
        elif wrong_guesses >= len(hangman_avatar) -1:
            display_avatar(wrong_guesses)
            displayAns(answer)
            print("you lose MUAHAHAHAH!!")
            running = False
            


                  

