salary=int(input("Enter the salary."))
yos=int(input("Enter the years of service."))
if(yos>10):
    print("bonus is 10%.")
    print((0.1*salary)+ salary)
elif((yos>=6) and (yos<=10)):
    print("bonus is 8%.")
    print((0.08*salary)+ salary)
elif(yos<6):
    print("bonus is 5%.")
    print((0.05*salary)+ salary)