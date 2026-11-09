import random
from tamagotchi.tamagotchi import Tamagotchi
import time

class Game :

    def __init__(self):
        self.pets = [
            Tamagotchi("Brick"),
            Tamagotchi("Morty"),
            Tamagotchi("Coco"),
        ]

        self.selected_pet = 0
        self.alive_time = 0
    
    #writing a method to show loading in progress
    def loading_animation(self):
        for i in range(3):
            time.sleep(random.uniform(0.5, 1.5))
            print(".",end="",flush=True)
        print("Done !")
    
    def select_pet(self,index):

        if index < 0 or index >= len(self.pets):
            print("Invalid pet selection")
            return
        self.select_peted_pet = index
        print(f"Selected pet: {self.pets[index].name}")

    def get_selected_pet(self):
        return self.pets[self.selected_pet]

    def perform_action(self,action):

        pet = self.get_selected_pet()
        if not pet.is_alive:
            print(f"{pet.name} is no longer alive. You cannot perform actions on it.")
            return
        if action == "feed":
            pet.feed()
            print(f"You fed {pet.name}.")
        elif action == "play":
            pet.play()
            print(f"You played with {pet.name}.")
        elif action == "sleep":
            pet.sleep()
            print(f"{pet.name} is sleeping.")
        elif action == "heal":
            pet.heal()
            print(f"You healed {pet.name}.")
        else:
            print("Invalid action. Please choose from 'feed', 'play', 'sleep', or 'heal'.")
            return
        self.loading_animation()
        self.update_pets()
        self.random_event()
        

    def update_pets(self):

        for pet in self.pets:
            if pet.is_alive:
                pet.hunger = min(100, pet.hunger + 5)
                pet.boredom = min(100, pet.boredom + 3)
                pet.exhaustion = min(100, pet.exhaustion + 2)

                if pet.hunger >= 100 or pet.health <= 0 or pet.boredom >= 100 or pet.exhaustion >= 100:
                    pet.is_alive = False
                    print(f"{pet.name} has died due to neglect.")

    def random_event(self):

        living_pets = [
            pet for pet in self.pets if pet.is_alive
        ]

        if not living_pets:
            print("All pets are dead. Game over.Survived time : ",self.alive_time," seconds.")
            return

        if random.random() < 0.5:

            pet=random.choice(living_pets)

            event = random.choice(["starvation", "illness", "boredom", "exhaustion"])

            if event == "starvation":
                pet.hunger = min(100, pet.hunger + 20)
                print(f"Random Event: {pet.name} is starving! Hunger increased to {pet.hunger}.")
            elif event == "illness":
                pet.health = max(0, pet.health - 20)
                print(f"Random Event: {pet.name} got sick! Health decreased to {pet.health}.")
            elif event == "boredom":
                pet.boredom = min(100, pet.boredom + 15)
                print(f"Random Event: {pet.name} is bored! Boredom increased to {pet.boredom}.")
            elif event == "exhaustion":
                pet.exhaustion = min(100, pet.exhaustion + 10)
                print(f"Random Event: {pet.name} is exhausted! Exhaustion increased to {pet.exhaustion}.")

            if pet.health <= 0 or pet.hunger >= 100 or pet.boredom >= 100 or pet.exhaustion >= 100:
                pet.is_alive = False
                print(f"{pet.name} has died due to {event}.")

    def display_statistics(self):
        print("\n<==== Game Statistics ===>")
        for pet in self.pets:
            print(f"Name: {pet.name}, Alive: {'Yes' if pet.is_alive else 'No'}, Hunger: {pet.hunger}, Health: {pet.health}, Boredom: {pet.boredom}, Exhaustion: {pet.exhaustion}")
        print("<==========================>\n")


    
    