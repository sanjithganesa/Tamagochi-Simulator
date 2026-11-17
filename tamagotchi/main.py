
from tamagotchi.game import Game
from tamagotchi.storage import save_game, load_game


SAVE_FILE = "save.json"


def display_menu():

    print("\n================================")
    print("       TAMAGOTCHI SIMULATOR")
    print("================================")
    print("1. Select a Tamagotchi")
    print("2. Feed")
    print("3. Play")
    print("4. Sleep")
    print("5. Heal")
    print("6. Display pet status")
    print("7. Display game statistics")
    print("8. Save game")
    print("9. Load game")
    print("0. Quit")
    print("================================")


def select_pet_menu(game):

    print("\nAvailable Tamagotchis:")

    for index, pet in enumerate(game.pets, start=1):
        status = "Alive" if pet.is_alive else "Dead"
        print(f"{index}. {pet.name} ({status})")

    try:
        choice = int(input("\nSelect a pet (1-3): "))

        if choice < 1 or choice > len(game.pets):
            print("Invalid pet selection.")
            return

        game.select_pet(choice - 1)

    except ValueError:
        print("Please enter a valid number.")


def handle_action(game, action):

    game.perform_action(action)


def save_current_game(game):

    save_game(game, SAVE_FILE)


def restore_game(game):

    try:
        loaded_data = load_game(SAVE_FILE)

        if loaded_data is None:
            return game

        game.pets = loaded_data["pets"]
        game.selected_pet = loaded_data["selected_pet"]
        game.alive_time = loaded_data["alive_time"]

        print("Game state restored successfully!")

        return game

    except (ValueError, KeyError, TypeError) as error:
        print(f"Unable to restore game: {error}")
        return game


def main():

    game = Game()

    print("\nWelcome to Tamagotchi Simulator!")

    while True:

        display_menu()

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                select_pet_menu(game)

            elif choice == "2":
                handle_action(game, "feed")

            elif choice == "3":
                handle_action(game, "play")

            elif choice == "4":
                handle_action(game, "sleep")

            elif choice == "5":
                handle_action(game, "heal")

            elif choice == "6":
                pet = game.get_selected_pet()
                pet.display_status()

            elif choice == "7":
                game.display_statistics()

            elif choice == "8":
                save_current_game(game)

            elif choice == "9":
                game = restore_game(game)

            elif choice == "0":
                print("\nThanks for playing Tamagotchi Simulator!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select an option from 0 to 9.")

        except KeyboardInterrupt:
            print("\n\nGame interrupted. Goodbye!")
            break

        except Exception as error:
            print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
