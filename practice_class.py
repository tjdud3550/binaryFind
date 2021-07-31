class Unit:
    def __init__(self):
        print("unit생성자")
class Flyable:
    def __init__(self):
        print("flyable 생성자.")

class Flyableunit(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()