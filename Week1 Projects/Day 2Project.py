print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
split=int(input("How many people to split the bill?"))
pay=(bill+((tip/100)*bill))/7
print(round(pay, 2))


