
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("enter (A, B, C, or D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0
    
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("results")
    print("-------------------------")
    
    print("answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
        
    print("guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = ((correct_guesses/len(questions))*100)
    print("your score is: "+str(score)+"%")

def play_again():

    response = input("do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "yes":
        return True
    else:
        return False

questions = {
    "who created python?: ": "A",
    "what year was python created?: ": "B",
    "python is tributed to which comedy group?: ": "C",
    "is the eart round?: ": "A"
}

options = [["A. guido van rossum", "B. elon musk", "C. bill gates", "D. mark zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. lonely island", "B. smosh", "C. monty python", "D.snl"],
          ["A. true", "B. false", "C. sometimes", "D. what's earth?"]]

new_game()

while play_again():
    new_game()

print("ok :v")







