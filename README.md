# Tamagotchi Simulator

A simple command-line Tamagotchi Simulator built using Python. The game allows you to take care of virtual pets by feeding them, playing with them, making them sleep, and healing them.

## About the Project

The simulator has three pets: Brick, Morty, and Coco. Each pet has its own hunger, health, boredom, and exhaustion levels.

The goal is to keep your pets healthy by managing their needs. As the game progresses, their needs change, and random events can affect their condition.

## Features

- Select and switch between three pets.
- Feed pets to reduce hunger.
- Play with pets to reduce boredom.
- Let pets sleep to reduce exhaustion.
- Heal pets to restore health.
- Automatic updates to pet attributes after each action.
- Random events that affect pet conditions.
- Pet death when health reaches zero.
- View individual pet status and game statistics.
- Save and load game progress using JSON.

## Technologies Used

- Python 3
- Object-Oriented Programming
- JSON
- Random and Time modules

The project uses Python's built-in libraries, so no external packages are required.

## Project Structure

```text
Tamagotchi_simulator/
│
├── tamagotchi/
│   ├── __init__.py
│   ├── main.py
│   ├── game.py
│   ├── storage.py
│   └── tamagotchi.py
│
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Execution

Clone the repository:

```bash
git clone https://github.com/sanjithganesa/Tamagochi-Simulator.git
```

Navigate to the project directory:

```bash
cd Tamagochi-Simulator
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Run the application from the project root:

```bash
python -m tamagotchi.main
```

## How to Play

Once the application starts, a menu will appear with options to select a pet, perform actions, view its status, check game statistics, save progress, or load a previous game.

Choose an option by entering its corresponding number in the terminal.

## Saving Progress

The game uses JSON to save pet attributes and the current game state in a `save.json` file. You can load this file later to continue your previous session.

## Future Improvements

- Add a graphical interface using Tkinter.
- Introduce more pets and activities.
- Add additional random events.
- Improve game statistics and progression.

## Author

Sanjith Ganesa Pandiayn

MSc Artificial Intelligence Systems