##random
import random as r
def define_choice(c):
    if c == 0:
        print(c)
    elif c == 1:
        print(c)
    else:
        print(c)    

choices = ['''
           Rock
           ''',
           '''
           Paper
           ''',
           '''
           Scissors
           '''
           ]

choice_ind = int(input("what do yo choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\nYou choice is: "))
if choice_ind >= 0 and  choice_ind<= 2:
    choice = choices[choice_ind]
    computer = choices[r.randint(0,2)]
    define_choice(choice)

    print("\nComputer chose: ")
    define_choice(choice)

    print()
    if choices.index(choice) == 0 and choices.index(computer) == 0:
        print("Draw")
    elif choices.index(choice) == 0 and choices.index(computer) == 1:
        print("You lose")
    elif choices.index(choice) == 0 and choices.index(computer) == 2:
        print("You Win!") 
    elif choices.index(choice) == 1 and choices.index(computer) == 1:
        print("Draw")
    elif choices.index(choice) == 1 and choices.index(computer) == 2:
        print("You lose")
    elif choices.index(choice) == 1 and choices.index(computer) == 0:
        print("You Win!")    
    elif choices.index(choice) == 2 and choices.index(computer) == 2:
        print("Draw")
    elif choices.index(choice) ==2 and choices.index(computer) == 0:
        print("You lose")
    elif choices.index(choice) ==2 and choices.index(computer) == 1:
        print("You Win!")
        
else:
    print("You Typed an invalid")
    
