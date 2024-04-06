# ~~ Program for Taking two inputs from user and taking the sum of the number. ~~
# You can use int for taking only integer number (Whole numbers -24,5,0,53,564 etc) in input.
# Or use float for floating point number (-45.5535, 0.0, 1.0, 4.663, 64.746 etc.) in input.
# I have used eval for taking both float and int numbers in input.



First_Number = eval(input("Enter the first number: "))

print("You have entered first number:",First_Number)

Second_Number = eval(input("Enter the second number: "))

print("You have entered second number:",Second_Number)


Sum_of_Numbers = First_Number + Second_Number

print("\n",First_Number,"+",Second_Number,"=",Sum_of_Numbers)
print("Sum of",First_Number,"and",Second_Number,"is",Sum_of_Numbers)
