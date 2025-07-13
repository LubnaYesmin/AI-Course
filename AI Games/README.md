# ♟️ Chess Game: Human vs AI using Alpha-Beta Pruning

This is a GUI-based chess game where you (the human player) play as **White** and the **AI (Black)** plays using the **Alpha-Beta Pruning algorithm**. The game uses the `python-chess` library to handle chess logic and `pygame` for the graphical interface.

---

## 🛠️ How to Run the Game

### Step 1: Clone or Download the Project
```bash
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



