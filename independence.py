class Person:
    def __init__(self, name, country, gender, state):
        self.name = name
        self.country = country
        self.gender = gender
        self.state = state

    def introduce(self):
        if self.gender.lower() == "male":
            title = "Mr"

        elif self.gender.lower() == "female":
            title = "Mrs"

        else:
            title = ""
        nigeria_age = 2026 - 1960

        print(
            f"Hello {title} {self.name}, your state of origin is {self.state} and you are {self.country}. Congratulations on your country's {nigeria_age}th independence")

    def foreigner(self):
        print(f"Hello {self.name}, you're a citizen of {self.country}, Welcome to Gomycode.")

    def citizen(self):
        if self.country.strip().lower() == "nigeria":
            self.introduce()
        else:
            self.foreigner()


name = input("Enter your name: ")
country = input("Enter your country: ")
gender = input("Enter your gender: ")
state = input("Enter your state of origin: ")

person1 = Person(name, country, gender, state)

person1.citizen()