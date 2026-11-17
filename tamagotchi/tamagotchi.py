
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.health = 100
        self.boredom = 40
        self.exhaustion = 35
        self.is_alive = True

    def feed(self):
        if not self.is_alive:
            print(f"{self.name} is no longer alive and cannot be fed.")
            return

        self.hunger = max(0, self.hunger - 20)
        print(f"{self.name} has been fed. Hunger is now {self.hunger}.")

    def play(self):
        if not self.is_alive:
            print(f"{self.name} is no longer alive and cannot play.")
            return

        self.boredom = max(0, self.boredom - 15)
        self.hunger = min(100, self.hunger + 5)
        self.exhaustion = min(100, self.exhaustion + 10)

        print(f"{self.name} played. Boredom is now {self.boredom}.")

    def sleep(self):
        if not self.is_alive:
            print(f"{self.name} is no longer alive and cannot sleep.")
            return

        self.exhaustion = max(0, self.exhaustion - 20)
        self.hunger = min(100, self.hunger + 10)

        print(f"{self.name} slept. Exhaustion is now {self.exhaustion}.")

    def heal(self):
        if not self.is_alive:
            print(f"{self.name} is no longer alive and cannot be healed.")
            return

        self.health = min(100, self.health + 20)
        print(f"{self.name} has been healed. Health is now {self.health}.")

    def display_status(self):
        print("\n========== PET STATUS ==========")
        print(f"Name       : {self.name}")
        print(f"Hunger     : {self.hunger}")
        print(f"Health     : {self.health}")
        print(f"Boredom    : {self.boredom}")
        print(f"Exhaustion : {self.exhaustion}")
        print(f"Alive      : {'Yes' if self.is_alive else 'No'}")
        print("================================")
