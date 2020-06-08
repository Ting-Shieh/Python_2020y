class car:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed
    def run(self):
        print("run")

class Electorcar(car):
    def __init__(self, vol=0, brand="", speed=0):
        super().__init__(brand,speed)
        self.vol = vol


