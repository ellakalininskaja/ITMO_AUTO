from home_work.python_trening.task_9_inheritance import Mammal


class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5

print(B().y)
b = B()
print(b.y)


class Cat(Mammal):
    species = "Canis lupus"

    def __init__(self, name):
        super().__init__(name)


cat = Cat('Муся')
print(cat.name)