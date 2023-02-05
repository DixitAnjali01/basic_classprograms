#PROGRAM TO CALCULATE THE SIMPLE INTEREST 
amt=int(input("Enter the principal amount:"))
rate=int(input("Enter rate:"))
time=int(input("Enter the time(in years):"))
interest=(amt*rate*time)/100
print("The amount of simple interest is = ",interest)