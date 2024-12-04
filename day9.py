# dictionaries
#practice
def students_grade():
    student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
    student_grades ={}
    
    for i in student_scores:
        if student_scores[i] <= 70:
            student_grades[i] = "Fail"
        elif  student_scores[i] >70 and  student_scores[i] < 80:
            student_grades[i] = "Acceptable"
        elif  student_scores[i] >80 and  student_scores[i] < 90:
            student_grades[i] = "Exceeds Expectations"
        else:
            student_grades[i] = "Outstanding"

        
## Project
def winner(list_dict):
    key_win = ""
    win = 0
    for i in list_dict:
        if  list_dict[i]> win:
            key_win = i
            win =  list_dict[i]
    print(f"Winner is {key_win} with a bid of ${list_dict[key_win]} ")
    
def bid_secret():
    print("Welcome to the secret auction program")
    list_dict = {}
    more = True
    while more:        
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        list_dict[name] = bid
        again = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
        
        if again != "yes":
            more = False
        else:
            print("\n" *20)
    
    ##make for me
    winner(list_dict)
    ##another 
    print(f"Winner is {max(list_dict, key=list_dict.get)} with a bid of ${list_dict[max(list_dict, key=list_dict.get)]} ")

bid_secret()