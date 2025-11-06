# Created on iPad.
meters = int(input("would you like to know meters in feet just write the meter here."))
feet = meters * 3.28084
print(meters,"meter is",feet,"feet")

money = int(input("how much money do you make"))
if money in range (0, 2001):
    print("0% tax")
elif money in range (2000,4001 ):
	print("15% tax")
elif money in range(4000, 7001):
	print("20% tax")
elif money in range(7000, 10001):
    print("25% tax")
elif money in range(10000, 14001):
	print("30% tax")
else:
    print("35% tax")