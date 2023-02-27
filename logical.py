citizen=input("Enter your citzenship:").lower()
age=int(input("Enter your age:"))
if((citizen=="kenyan")and(age>=18)):
    print("Eligible to vote.")
else:
    print("Not eligible")