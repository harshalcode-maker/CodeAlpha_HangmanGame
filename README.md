# CodeAlpha_HangmanGame
# 🎮 Hangman Game Using Python

## 📌 Project Overview

The **Hangman Game** is a simple text-based word-guessing game developed using Python. In this game, the computer randomly selects a word from a predefined list, and the player must guess the word one letter at a time.

The player gets a maximum of **6 incorrect guesses** to identify the secret word. The game also includes a hint feature that reveals a randomly selected hidden letter.

## 🎯 Project Objectives

- Develop a simple word-guessing game using Python.
- Understand random word selection.
- Practice loops and conditional statements.
- Work with strings and lists.
- Implement a random letter hint system.
- Handle invalid and repeated user inputs.

## ✨ Features

- Random selection of words from a list of 5 predefined words.
- Letter-by-letter word guessing.
- Maximum 6 incorrect attempts.
- Random letter hint system.
- Input validation.
- Detection of repeated guesses.
- Win and lose conditions.
- Console-based interface.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Module:** Random
- **Concepts:** Lists, Strings, While Loop, For Loop, If-Else Statements, Conditional Logic, User Input.

## 📚 Predefined Words

The game contains the following five words:

1. Python
2. Computer
3. Program
4. Developer
5. Keyboard

The computer randomly selects one word whenever the game starts.

## 💡 Hint System

The player can type `hint` instead of a letter to reveal a randomly selected hidden letter.

**Example:**


Secret Word: PYTHON

Before Hint:
_ _ _ _ _ _

After Hint:
P _ _ _ _ _


The revealed letter is automatically added to the guessed letters. Using a hint does not increase the incorrect guess count.

## 📂 Project Structure


CodeAplha_HangmanGame/
│
├── hangman.py
└── README.md


## ⚙️ Requirements

- Python 3.x
- Visual Studio Code (recommended)
- No external libraries required.

The `random` module is included in Python's standard library.

## 🚀 How to Run the Project

**Step 1:** Clone the repository or download the project files.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Open the terminal.

**Step 4:** Run the following command:

```bash
python hangman.py
```

**Step 5:** Start guessing letters or type `hint` to reveal a letter.

## 🖥️ Sample Output

```text
================================
       WELCOME TO HANGMAN
================================
Guess the word one letter at a time!
You have 6 incorrect guesses allowed.
Type 'hint' to reveal a random letter.

Word: _ _ _ _ _ _

Enter a letter or type 'hint': p
Correct guess!

Word: p _ _ _ _ _

Enter a letter or type 'hint': hint
Hint! The letter revealed is: y

Word: p y _ _ _ _
```

## 📖 Key Python Concepts

| Concept | Description |
|---|---|
| Random Module | Selects a random word |
| Lists | Stores guessed letters and words |
| Strings | Stores and displays the secret word |
| While Loop | Repeats the game until it ends |
| For Loop | Displays guessed and hidden letters |
| If-Else | Checks correct and incorrect guesses |
| Input | Accepts player guesses |
| Conditional Logic | Checks winning and losing conditions |

## 🎓 Learning Outcomes

By completing this project, I learned how to:

- Use Python's random module.
- Implement loops and conditional statements.
- Work with lists and strings.
- Accept and validate user input.
- Build a simple interactive console-based game.
- Implement a random letter hint feature.

⭐ If you find this project useful, feel free to star the repository!
