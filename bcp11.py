#CURRENCY NOTES
amt=int(input("Enter the amount  to be withdrawn:"))
amt=amt-100
count1=amt//2000
amt=amt-(count1*2000)
count2=amt//500
amt=amt-(count2*500)
count3=amt//100
total_count=count1+count2+count3+1
print("The total number of minimum currency notes is = ",total_count)