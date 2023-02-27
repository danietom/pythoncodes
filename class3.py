class Temperature:
    def __init__(self,celcius,farenheit):
        self.celcius=celcius#
        self.farenheit=farenheit
    def show(self):
        print(self.celcius," degrees celcius is equivalent to:",(self.celcius*(9/5))+32,"degrees farenheit")
        print(self.farenheit," degrees farenheit is equivalent to:",((self.farenheit-32)*5)/9,"degrees celcius")
stud= Temperature(20,20)
stud.show()