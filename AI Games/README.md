# ♟️ Chess Game: Human vs AI using Alpha-Beta Pruning

This is a GUI-based chess game where you (the human player) play as **White** and the **AI (Black)** plays using the **Alpha-Beta Pruning algorithm**. The game uses the `python-chess` library to handle chess logic and `pygame` for the graphical interface.

---

## 🛠️ How to Run the Game

### Step 1: Clone or Download the Project
bash
git clone https://github.com/your-username/ai-chess-game.git
cd ai-chess-game

### Step 2: Install Required Libraries
Make sure Python is installed. Then run:
pip install pygame
pip install chess

### Step 3: Run the Game
python chess_game.py

## 🎮 How to Play

You are White, and you move first.
Click once on a white piece to select it, and click again on a valid square to move.
After your move, the AI will automatically calculate and make its move.
To exit the game, close the window.

## 🧠 Algorithm Used

This game uses the Alpha-Beta Pruning algorithm, a classical AI method used in adversarial games to reduce the search space of the Minimax algorithm.
The AI:
Searches to a depth of 3
Evaluates based on a material-count heuristic
Makes decisions by minimizing the opponent’s best options

## 📚 Libraries & Frameworks Used

pygame – for GUI window and drawing
python-chess – for board logic, legal moves, etc.
sys – for closing the game
Standard Python (3.6+)

![chess](https://github.com/user-attachments/assets/228fac98-3c22-4518-bb63-c538660ead6b)

# 🎮 Tic-Tac-Toe Game – Human vs AI using Minimax Algorithm

This is a terminal-based **Tic-Tac-Toe game** where you (the human) play as `X`, and the **AI opponent (O)** plays using the **Minimax algorithm** to make optimal moves.

---

## 🛠️ How to Run the Game

### Step 1: Make sure Python is installed  
Recommended version: **Python 3.6+**

### Step 2: Save the code  
Save the game code in a Python file, e.g. `tic_tac_toe.py`

### Step 3: Run the file in terminal or any Python environment  
bash
python tic_tac_toe.py

## 📚 Software / Libraries Required
No external libraries required

Uses only Python standard library (math)

✅ This game runs in the terminal/console — no need for GUI or installations.

## 🎮 How to Play the Game
You will play as X

The AI will play as O

On your turn, you will be asked to input:

Row number: 0, 1, or 2

Column number: 0, 1, or 2

The board will update after every move.

After your move, the AI will automatically calculate its best move using the Minimax algorithm

The game ends when:

Either player wins

The board is full (draw)

## 🧠 Algorithm Used
🔁 Minimax Algorithm
This game uses the Minimax algorithm, a recursive decision-making strategy used in two-player turn-based games.

The AI explores all possible moves using recursion.

It tries to maximize its score and minimize the opponent's.

Base case:

+1 if AI wins (O)

-1 if Human wins (X)

0 if it's a draw

⚙️ Decision Rules:
AI (O) is the maximizer

Human (X) is the minimizer

AI picks the move that leads to the best guaranteed outcome


Screenshot 2025-07-13 234049.png

# 🎮 Connect 4 Game – Human vs AI (Minimax with Alpha-Beta Pruning)

This is a **console-based Connect 4 game** where a human plays against an AI. The AI uses the **Minimax algorithm with Alpha-Beta Pruning** to make smart decisions. The game is played on a 6x7 board, and the first to align four of their pieces (horizontally, vertically, or diagonally) wins.

---

## ✅ How to Run the Game

### Step 1: Make sure Python is installed
Recommended version: **Python 3.6+**

### Step 2: Save the code
Save the Python code in a file named:

bash
connect4.py

### Step 3: Run the file in terminal or IDE
python connect4.py

## 📦 Libraries Used
✅ Only uses built-in Python libraries:

math

random

No external libraries are needed.

## 🎮 How to Play
You play as Player (1) and go first or second (randomized).

The AI is Player 2 (2).

On your turn:

Input a column number between 0 and 6

If the move is valid, your piece will be placed at the lowest available row in that column

The board will display after every move.

The game ends when:

A player connects 4 pieces (horizontal, vertical, or diagonal)

The board is full (draw)

## 🧠 AI Algorithm: Minimax + Alpha-Beta Pruning
🔁 Minimax
The AI simulates all possible future moves to a fixed depth (default: 4)

It evaluates outcomes using a heuristic scoring function:

+100 for 4-in-a-row

+10 for 3-in-a-row

+5 for 2-in-a-row

-8 if the opponent is about to win

## 🔍 Alpha-Beta Pruning
Optimizes Minimax by pruning branches that won't affect the outcome

Reduces unnecessary computation and improves speed

## ⚡ Depth Control
You can adjust the difficulty by changing:
DEPTH = 4

## 📸 Game Example Output
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 2, 0, 0, 0, 0, 0]
Your move:
Enter column (0-6): _
## 🙌 Acknowledgements
Developed as part of the AI Lab Course

Topic: Adversarial Search – Minimax Algorithm with Alpha-Beta Pruning








