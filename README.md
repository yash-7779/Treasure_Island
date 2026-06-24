# 🏝️ Treasure Island Game

A simple text-based adventure game written in Python where the player must make the right choices to find a hidden treasure.

## 📖 Description

Welcome to **Treasure Island**! Your goal is to navigate through a series of choices and find the hidden treasure. Choose wisely—one wrong move can end your adventure.

## 🎮 How to Play

1. Start the game.
2. Choose between the **Left** or **Right** path.
3. If you choose the correct path, you'll discover an abandoned castle.
4. Decide whether to enter the castle or turn back.
5. Find the treasure or face a game over!

## 🚀 Running the Game

Make sure Python is installed on your system.

```bash
python treasure_island.py
```

## 📋 Example Gameplay

```text
Welcome to the treasure Island!

The road you were walking on now diverges into two turns...
Which path do you want to go? 'Left' or 'Right'
> left

You found an Abandoned Castle.
Would you like to go into the castle or turn back?
Type 'castle' or 'turn back'
> castle

Congrats! you found the Treasure.
```

## 🗺️ Game Flow

```text
Start
 │
 ├── Right
 │    └── Monster attacks → Game Over
 │
 └── Left
      │
      ├── Castle
      │    └── Find Treasure 🎉
      │
      └── Turn Back
           └── Lost forever → Game Over
```

## 📂 Project Structure

```text
treasure_island.py
README.md
```

## 🛠️ Technologies Used

* Python 3

## 🎯 Learning Objectives

This project helps beginners practice:

* User input handling
* Conditional statements (`if`, `elif`, `else`)
* String manipulation with `.lower()`
* Basic game logic
* Console-based interaction

## 📜 License

This project is free to use for learning and educational purposes.
