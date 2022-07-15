from temperature import Temperature


class Calorie:

    def __init__(self, weight, height, temperature, age):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result

# if __name__ == "__main__":
#    temperature = Temperature(country="brazil", city="curitiba").get()
#    calorie = Calorie(temperature=temperature, weight=80, height=181, age=21)
#    print(calorie.calculate())
