# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
def life_in_week(age):
    result = 0
    for a in range(int(age)):
        result += 54
    print(f"You have {result} weeks left.")


life_in_week(2)