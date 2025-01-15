print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
pay_per_person = (bill + tip_amount) / people

print(f"Each person should pay {round(pay_per_person, 2)}")