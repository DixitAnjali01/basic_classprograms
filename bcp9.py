#PROGRAM TO FIND THE HYPOTENEUSE OF THE TRIANGLE WHEN BASE AND HEIGHT ARE BEING ENTERED
import math
b=int(input("Enter the base:"))
h=int(input("Enter the height:"))
hypo=math.sqrt((b**2)+(h**2))
print("The hypoteneuse of the triangle is =",hypo)