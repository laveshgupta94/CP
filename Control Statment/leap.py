#9. WAP to check whether a year is a leap year or not. 
Year =int(input("Enter the Year"))
if(Year%400==0 and Year%4==0):
    print("leap")
else:
    print("no leap")