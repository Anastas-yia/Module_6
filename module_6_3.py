import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz):
        self.new_x = dx * self.speed
        self._cords[0] = self.new_x
        self.new_y = dy * self.speed
        self._cords[1] = self.new_y
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.new_z = dz * self.speed
            self._cords[2] = self.new_z

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        self.random_number = random.randint(1, 4)
        print(f'Here are(is) {self.random_number} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dive_z = int(dz / 2 * self.speed)
        self._cords[2] = self._cords[2] - abs(self.dive_z)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

print(Duckbill.mro())

