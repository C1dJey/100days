# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
    
# calculate_love_score("Kanye West", "Kim Kardashian")

######CIPHER
# ---> chatGPT version
# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             shift_base = 65 if char.isupper() else 97
#             result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
#         else:
#             result += char
#     return result

def encrypt(text_base,shift_base):
    cipher = ""
    for l in text_base:
        if l not in alphabet:
            cipher += l
        else:
            shift = alphabet.index(l.lower())+shift_base
            shift %= len(alphabet)
            cipher +=  alphabet[shift]
    print(f"result is: {cipher}")
    
def decrypt(text_base,shift_base):
    cipher = ""
    
    for l in text_base:
        if l not in alphabet:
            cipher += l
        else:
            shift = alphabet.index(l.lower())-shift_base
            shift %= len(alphabet)
            cipher +=  alphabet[shift]
    print(f"this is result: {cipher}"
          )
def ceaser(direction, text, shift):
    if direction.lower() == "encode":
        encrypt(text_base=text, shift_base=shift)
    elif direction.lower() == "decode":
        decrypt(text_base=text, shift_base=shift)
    else:
        print("anything options choosed")
        
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   
again = True
while again:
    direction = input("decode or encode: ")
    text = input("what is your text: ")
    shift = int(input("type of shift number: "))
    ceaser(direction, text, shift)
    dnv = input("Again ?")
    
    if dnv.lower() == "no":
        again = False
        print("see you later")
