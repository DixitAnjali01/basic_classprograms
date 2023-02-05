#COMPOUND INTEREST
amt=int(input("Enter the principal amount:"))
rate=int(input("Enter rate:"))
time=int(input("Enter the time(in years):"))
CI=amt*((1+rate)**time)
print("The amount of simple interest is = ",CI)