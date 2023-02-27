class Temperature:
    def __init__(self,celcius,farenheit):
        self.celcius=celcius
        self.farenheit=farenheit
    def convert_celcius(self):
        return ((self.celcius*(9/5))+32)
    def convert_farenheit(self):
        return (((self.farenheit-32)*5)/9)
stud= Temperature(20,20)
print(stud.convert_celcius())
print(stud.convert_farenheit())