
import json

from tamagotchi.tamagotchi import Tamagotchi


def save_game(game, filename):
    data = {
        "selected_pet": game.selected_pet,
        "alive_time": game.alive_time,
        "pets": []
    }

    for pet in game.pets:
        pet_data = {
            "name": pet.name,
            "hunger": pet.hunger,
            "health": pet.health,
            "boredom": pet.boredom,
            "exhaustion": pet.exhaustion,
            "is_alive": pet.is_alive
        }

        data["pets"].append(pet_data)

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Game saved to {filename}.")

    except (OSError, TypeError, ValueError) as error:
        print(f"Error saving game: {error}")


def load_game(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid game data format.")

        if not all(
            key in data
            for key in ("selected_pet", "alive_time", "pets")
        ):
            raise ValueError("Missing game data.")

        if not isinstance(data["pets"], list) or len(data["pets"]) != 3:
            raise ValueError("Invalid number of pets in game data.")

        pets = []

        for pet_data in data["pets"]:

            required_keys = (
                "name",
                "hunger",
                "health",
                "boredom",
                "exhaustion",
                "is_alive"
            )

            if not isinstance(pet_data, dict):
                raise ValueError("Invalid pet data.")

            if not all(key in pet_data for key in required_keys):
                raise ValueError("Missing pet information.")

            pet = Tamagotchi(pet_data["name"])

            pet.hunger = pet_data["hunger"]
            pet.health = pet_data["health"]
            pet.boredom = pet_data["boredom"]
            pet.exhaustion = pet_data["exhaustion"]
            pet.is_alive = pet_data["is_alive"]

            for attribute in (
                pet.hunger,
                pet.health,
                pet.boredom,
                pet.exhaustion
            ):
                if type(attribute) is not int or not 0 <= attribute <= 100:
                    raise ValueError("Invalid pet attribute value.")

            if type(pet.is_alive) is not bool:
                raise ValueError("Invalid pet alive status.")

            pets.append(pet)

        selected_pet = data["selected_pet"]
        alive_time = data["alive_time"]

        if type(selected_pet) is not int or not 0 <= selected_pet < len(pets):
            raise ValueError("Invalid selected pet index.")

        if type(alive_time) is not int or alive_time < 0:
            raise ValueError("Invalid alive time value.")

        game_data = {
            "selected_pet": selected_pet,
            "alive_time": alive_time,
            "pets": pets
        }

        print(f"Game loaded from {filename}.")
        return game_data

    except FileNotFoundError:
        print("Save file not found.")
        return None

    except json.JSONDecodeError:
        print("Save file contains invalid JSON.")
        return None

    except (ValueError, KeyError, TypeError) as error:
        print(f"Invalid save file: {error}")
        return None

    except OSError as error:
        print(f"Error loading game: {error}")
        return None
