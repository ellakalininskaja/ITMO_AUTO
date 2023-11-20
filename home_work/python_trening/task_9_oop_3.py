class Soda:
    ing = None
    width = 'ghg'

    def __init__(self, ing=None, width='1111'):
        self.ing = ing
        self.width = width

    def show_my_drink(self):
        if self.ing:
            print(f"Газировка и {self.ing}")
        else:
            print("Обычная гозировка")


drink1 = Soda()
print(drink1.width)
drink2 = Soda('Малина', 'тест')
drink1.show_my_drink()
drink2.show_my_drink()
print(drink2.width)
