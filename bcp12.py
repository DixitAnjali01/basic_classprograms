#PROGRAM TO FIND THE TYPE OF TRIANGLE
s1=int(input("Enter first side:"))
s2=int(input("Enter second side:"))
s3=int(input("Enter third side:"))
print(((s1>s2+s3)&(s2>s1+s3)&(s3>s1+s2))*('Invalid'))
print(((s1!=s2)|(s2!=s3)|(s1!=s3))*('Scalene'))
print(((s1==s2)|(s2==s3)|(s3==s1))*('Isoceles'))
print(((s1**2==s2**2+s3**2)|(s2**2==s1**2+s3**2)|(s3**2==s2**2+s1**2))*('Rght angle'))

