class Mammal:
    name = "Млекопитающие"

    def __init__(self, name):
        self.name = name


class Dog(Mammal):
    species = "Canis lupus"

    def __init__(self, name):
        super().__init__(name)


class Cat(Mammal):
    species = "Canis lupus"

    def __init__(self, name):
        super().__init__(name)


# dog = Dog('Шарик')
# print(dog.name)
# cat = Cat('Муся')
# print(cat.name)
