#FINDING NUMBER OF TILES WHEN BOTH RECTANGULAR AREA AND DIMENSION OF TILE IS GIVEN
l1=int(input("Enter length of the rectangular floor:"))
b1=int(input("Enter breadth of the rectangular floor:"))
l2=int(input("Enter length of the rectangular tile:"))
b2=int(input("Enter breadth of the rectangular tile:"))
count=(l1*b1)//(l2*b2)
print("The number of tiles is = ",count)