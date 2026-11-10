
import random
import time

from tamagotchi.tamagotchi import Tamagotchi


class Game:
    def __init__(self):
        self.pets = [
            Tamagotchi("Brick"),
            Tamagotchi("Morty"),
            Tamagotchi("Coco")
        ]

        self.selected_pet = 0
        self.alive_time = 0

    def loading_animation(self):
        print("Processing", end="", flush=True)

        for i in range(3):
            time.sleep(random.uniform(0.5, 1.5))
            print(".", end="", flush=True)

        print(" Done!")

    def select_pet(self, index):
        if index < 0 or index >= len(self.pets):
            print("Invalid pet selection.")
            return

        self.selected_pet = index
        print(f"Selected pet: {self.pets[index].name}")

    def get_selected_pet(self):
        return self.pets[self.selected_pet]

    def perform_action(self, action):
        pet = self.get_selected_pet()

        if not pet.is_alive:
            print(f"{pet.name} is no longer alive.")
            return

        if action == "feed":
            pet.feed()

        elif action == "play":
            pet.play()

        elif action == "sleep":
            pet.sleep()

        elif action == "heal":
            pet.heal()

        else:
            print("Invalid action. Choose feed, play, sleep, or heal.")
            return

        self.loading_animation()
        self.update_pets()
        self.random_event()

    def update_pets(self):
        for pet in self.pets:

            if not pet.is_alive:
                continue

            # Natural increase in needs
            pet.hunger = min(100, pet.hunger + 5)
            pet.boredom = min(100, pet.boredom + 3)
            pet.exhaustion = min(100, pet.exhaustion + 2)

            # Health deterioration when needs become critical
            if pet.hunger >= 80:
                pet.health = max(0, pet.health - 5)

            if pet.boredom >= 90:
                pet.health = max(0, pet.health - 5)

            if pet.exhaustion >= 90:
                pet.health = max(0, pet.health - 5)

            # Death condition
            if pet.health <= 0:
                pet.is_alive = False
                print(f"{pet.name} has died due to neglect!")

    def random_event(self):
        living_pets = [
            pet for pet in self.pets if pet.is_alive
        ]

        if not living_pets:
            print("All pets are dead. Game over.")
            print(f"Survived time: {self.alive_time} seconds.")
            return

        # 50% chance of a random event
        if random.random() < 0.5:

            pet = random.choice(living_pets)

            event = random.choice([
                "starvation",
                "illness",
                "boredom",
                "exhaustion"
            ])

            if event == "starvation":
                pet.hunger = min(100, pet.hunger + 20)
                print(f"Random Event: {pet.name} became hungry!")

            elif event == "illness":
                pet.health = max(0, pet.health - 20)
                print(f"Random Event: {pet.name} became ill!")

            elif event == "boredom":
                pet.boredom = min(100, pet.boredom + 15)
                print(f"Random Event: {pet.name} became bored!")

            elif event == "exhaustion":
                pet.exhaustion = min(100, pet.exhaustion + 10)
                print(f"Random Event: {pet.name} became exhausted!")

            if pet.health <= 0:
                pet.is_alive = False
                print(f"{pet.name} has died due to {event}.")

    def display_statistics(self):
        living_pets = [
            pet for pet in self.pets if pet.is_alive
        ]

        dead_pets = [
            pet for pet in self.pets if not pet.is_alive
        ]

        print("\n========== GAME STATISTICS ==========")

        print(f"Total pets : {len(self.pets)}")
        print(f"Living pets: {len(living_pets)}")
        print(f"Dead pets  : {len(dead_pets)}")
        print(f"Alive time : {self.alive_time} seconds")

        if living_pets:
            average_health = sum(
                pet.health for pet in living_pets
            ) / len(living_pets)

            average_hunger = sum(
                pet.hunger for pet in living_pets
            ) / len(living_pets)

            average_boredom = sum(
                pet.boredom for pet in living_pets
            ) / len(living_pets)

            average_exhaustion = sum(
                pet.exhaustion for pet in living_pets
            ) / len(living_pets)

            print(f"Average health     : {average_health:.2f}")
            print(f"Average hunger     : {average_hunger:.2f}")
            print(f"Average boredom    : {average_boredom:.2f}")
            print(f"Average exhaustion : {average_exhaustion:.2f}")

        else:
            print("No living pets remaining.")

        print("=====================================")

        for pet in self.pets:
            pet.display_status()
