sub1=abs(int(input("Enter the marks of the first subject:")))
if ((sub1<0) and (sub1>101)):
    print("A negative number.")
sub2=abs(int(input("Enter the marks of the second subject:")))
sub3=abs(int(input("Enter the marks of the third subject:")))
avg=((sub1+sub2+sub3)/3)
print(avg)
if((avg<=100) and (avg>=70)):
    print("Grade A")
elif((avg<=69) and (avg>=60)):
    print("Grade B")
elif((avg<=59) and (avg>=50)):
    print("Grade C")
elif((avg<=49) and (avg>=40)):
    print("Grade D")
elif((avg<=39) and (avg>=0)):
    print("FAIL")
else:
    print("INVALID INPUT.")