#Write a python script to check whether a given year is a leap year or not.
print (" Enter a leap year : ")
year=int(input())
if (year%400==0) or ( (year%100)!=0 and year%4==0 ):
    print(" Given year is leap year. ")
else :
    print(" Given year is not leap year. ")
print()