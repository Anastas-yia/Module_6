# добавила проверку того, что объект, передаваемый в параметр food содержит атрибут 'edible'
# поэтому в выводе в консоль есть дополнительная строка: "Волк не может съесть Слон"
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True # живой
        self.fed = False # накормленный

    def eat(self, food):
        if hasattr(food, 'edible'):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{self.name} не может съесть {food.name}')


class Plant:
    edible = False # съедобность
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True # переопределяется при наследовании


a1 = Predator('Волк')
a2 = Mammal('Слон')
p1 = Flower('Тюльпан')
p2 = Fruit('Банан')


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
a1.eat(a2)
print(a1.alive)
print(a2.fed)
