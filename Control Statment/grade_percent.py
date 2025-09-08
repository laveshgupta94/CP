#15. Accept the percentage from the user and display the grade according to the following 
# Below 25 – D 
# 25 to 45 – C 
# 45 to 65 – B 
# 65 to 85 – A 
# Above 85 – A+ 

P=int(input("Enter your percentage: "))
if(P<=25):
    print("Grade is D",P)
if(25<P<=45):
    print("Grade is C",P)
if(45<P<=65):
    print("Grade is B",P)
if(65<P<=85):
    print("Grade is A",P)
if (85<P<=100):
    print("Grade is A+",P)
