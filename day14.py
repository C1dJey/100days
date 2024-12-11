# Higher lower game
import random as r
def main(score):
    in_game = True
    choose = "first"
    while in_game:
        
        if len(dict_all) > 0:
            print(f"Score is : {score}")   
            if choose ==  "first":
                c1 = r.choice(list(dict_all))
                dict_all.pop(c1)
            c2 = r.choice(list(dict_all))
            dict_all.pop(c2)
            choose = input(f"Who is mor stronger ? type 'A' for {c1}, or 'B' for {c2} ").lower()
            if choose == "a":
                choose = c1
            else:
                choose = c2
            
            a = dict_choices[c1]
            b = dict_choices[c2]
            if a > b:
                if choose == c1:
                    score += 1
                else:
                    print("You lose")
                    in_game = False   
                    break
            elif b > a:
                if choose == c2:
                    score += 1
                else:
                    print("You lose")
                    in_game = False   
                    break
            c1 = choose
        else:
            print (f"You win, score {score}")
            break

dict_all= {"Naruto": 10, "Goku": 100, "Midorya": 5}
dict_choices = {"Naruto": 10, "Goku": 100, "Midorya": 5}
score = 0 
main(score)