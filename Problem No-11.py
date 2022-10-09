# Write a python script to take the month value in numeric format and display the number of days in it.
print(" Enter month number : ")
month=int(input())
if month in (1,3,5,7,8,10,12):
    print(" No of days in this month are : 31 days.")
elif month in (4,6,9,11) :
    print(" No of days in this month are : 30 days.")
elif month==2:
    print("Number of days in this month are : 28 days or 29 days.")
else:
    print("Invalid month number.")
print()
