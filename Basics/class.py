class Animal:
    def __init__(self,habitat,diet):
        self.habitat=habitat
        self.diet=diet

    def speak(self):
        print(f"i live in the {self.habitat} and eat {self.diet}")


animal_1=Animal('sea','plant')
animal_1.speak()


class Lion(Animal):
    def __init__(self,title,pride_size,habitat,meat):
        super().__init__(habitat,meat)
        self.title=title
        self.pride_size=pride_size

    def roar(self):
        print(f"i am the {self.title} of my pride of {self.pride_size} lions")



scar=Lion('outcast',15,'savanna','meat')
scar.roar()
scar.speak()