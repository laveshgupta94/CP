# Print all factors/divisors of agiven +ve number
num=int(input("Enter the num: "))
i=1
while(i<=num):
   if(num%i==0):
     print(i)
   i=i+1
