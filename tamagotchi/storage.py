from tamagotchi.tamagotchi import Tamagotchi
import json

def save_game(game,filename):
    data = {
        "selected_pet": game.selected_pet,
        "alive_time": game.alive_time,
        "pets": []
    }

    for pet in game.pets :
        pet_data = {
            "name": pet.name,
            "hunger": pet.hunger,
            "health": pet.health,
            "boredom": pet.boredom,
            "exhaustion": pet.exhaustion,
            "is_alive": pet.is_alive
        }
        data["pets"].append(pet_data)
