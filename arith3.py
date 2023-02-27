num=int(input("Enter your total amount"))
if(num>=1000):
    print("discount offered of 5%")
    print(0.05*num)
    print(num-(0.05*num))
else:
    print("No discount.")