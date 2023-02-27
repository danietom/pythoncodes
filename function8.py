def principle(princ):
    print("principle is: ",princ)
principle(princ=int(input("Enter the principle:")))
def time_years(time):
      print("time is: ",time)
time_years(time=int(input("Enter the time in years:")))
def rate_pa(rate):
    print("rate is: ",rate)
rate_pa(rate=int(input("Enter the rate in percentage:")))
def total_amount(amount):
    amount=(princ*(1+(rate/100))**time)
    print("The total amount is:",amount)
total_amount()