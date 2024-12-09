# Black Jack
import random as r

def get_score(hand):
    score = 0
    for i in hand:
        score += i
    return score

def check_win(hand):
    score = get_score(hand)
    if score == 21:
        return True
    else:
        return False
    
def add_remove(deck_cards, your_cards, choice):
    your_cards.append(choice)
    deck_cards.remove(choice)

def check_bust(your_cards,computer_cards):
    score = get_score(your_cards)
    if score > 21:
        # print(f"Your hand: {your_cards}, current score: {get_score(your_cards)}")
        print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")
        print(f"Busted You Lose")
        return True 
    
def first_round(your_cards,computer_cards, deck_cards):
    choice = r.choice(deck_cards)
    add_remove(deck_cards, your_cards, choice)
    
    choice = r.choice(deck_cards)
    add_remove(deck_cards, your_cards, choice)
    
    choice = r.choice(deck_cards)
    add_remove(deck_cards, computer_cards, choice)
    
    choice = r.choice(deck_cards)
    add_remove(deck_cards, computer_cards, choice)

def computer_game(computer_cards, deck_cards):
    continue_computer = True
    while continue_computer:
        if get_score(computer_cards) < 17:
            choice = r.choice(deck_cards)
            add_remove(deck_cards, computer_cards, choice)
        else:
            continue_computer = False
    print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")

def winner(your_cards,computer_cards):
    your = get_score(your_cards)
    computer = get_score(computer_cards)
    
    if your > computer and your <= 21:
        print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")
        print("You Win")
    elif computer > your and computer <= 21:
        print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")
        print("You Lose")
    elif computer > 21 and your < 21:
        print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")
        print("You Win")
    elif your> 21 and computer < 21:
        print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")
        print("Busted You Lose")  
    elif your == computer:
        print(f"Computer card: {computer_cards} score: {get_score(computer_cards)}")
        print("Draw")
    else:
        print(f"sei la your {your} computer {computer} ")
        
def main():
    deck_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    continue_game = True
    your_cards = []
    computer_cards = []
    
    #first round
    first_round(your_cards,computer_cards, deck_cards)
    
    print(f"deck: {deck_cards}")
    print(f"Your hand: {your_cards}, current score: {get_score(your_cards)}")
    print(f"Computer first card: {computer_cards[0]}")
    while continue_game:
        if not check_win(your_cards):
            other_card = input("do you want other card ? 'y' or 'n'")
            if other_card == "y":
                choice = r.choice(deck_cards)
                add_remove(deck_cards, your_cards, choice)
                print(f"Your hand: {your_cards}, current score: {get_score(your_cards)}")
                if check_bust(your_cards, computer_cards):
                    break
                check_win(your_cards)
            else:
                #Computer processa hand
                computer_game(computer_cards, deck_cards)
                
                # show all hands
                print(f"Your hand: {your_cards}, current score: {get_score(your_cards)}")
                winner(your_cards,computer_cards)
                # verify winner (compar both hand and get te winner or draW)
                
                continue_game = False
        else:
            computer_game(computer_cards, deck_cards)
            if not check_win(computer_cards):
                print("You Win")
                break
            else:
                print("Draw")
                break

first_check = input("do you want to play a Black Jack, type 'y' or 'n': ")
if first_check == "y":
    main()
