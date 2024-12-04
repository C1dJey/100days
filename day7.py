## hangman
import random as r

def contains_letter (letter, word):
    # woeds = str(palavra).count()
    for word_letter in word:
        if word_letter == letter:
            return True
    return False

def create_empty_word(word):
    empty_word =""
    for letter in str(word):
        empty_word += "_"
    return empty_word

def replace_empty (letter, word, empty):
    new_empty =""
    
    for a in word:
        coun = str(word).index(a)
        if a == letter:
            new_empty += letter
        else:
            new_empty += empty[coun]
            
    return new_empty
    
list_hang =[
'''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=========''',  
    '''  
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''',
   
    ''' 
 +---+
 |   |
 0   |
/|\  |
     |
     |
=========''',
    '''
 +---+
 |   |
 0   |
/|   |
     |
     |
=========''',
 '''
 +---+
 |   |
 0   |
 |   |
     |
     |
=========''',
    ''' 
 +---+
 |   |
 0   | 
     |
     |
     |
=========''',
''' 
+---+
|   |
    |
    |
    |
    |
=========
''',
    
]
list_of_words = ["matheus","julie","aysha", "gustavo"]
lives = 6
win = False
word_random = r.choice(list_of_words)
empty_word = create_empty_word(word_random)
# print(word_random)
print(empty_word)
# empty_word = replace_empty("a", word_random,empty_word)
while lives > 0:
    if "_"  in empty_word:
        print(f"=====have {lives}/6 Lives=====")
        letter = input("Choose your letter: ").lower()
        if contains_letter(letter, word_random):
            empty_word = replace_empty(letter,word_random,empty_word)
            print(empty_word)
        else:
            print("Dont contain this letter")
            lives -= 1
        print(list_hang[lives])
    else:
        print("You win!")
        win = True
        break
if not win:
    print("=========You LOSE===========")