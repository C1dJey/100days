print ("Welcome to the tip calculator.")
bill = float(input("What was the total bill??\n$"))
# print(type(bill))
tip = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
total = (bill * (tip/100)) + bill
people =int(input("How many people to split the bill?\n"))
bill_people = total / people
result = round(bill_people, 2)
print(f"Each person should pay: $ {result}" )
