# 🤖 Artificial Intelligence Course – Search & Game Algorithms

This section of the AI course explores **search algorithms** and **game-playing strategies**, focusing on both **uninformed** and **informed** methods as well as heuristic techniques like **hill climbing**, and adversarial search via **Min-Max and Alpha-Beta Pruning**.

---

## 📚  Search Algorithms

### 🔍 Uninformed Search Techniques

#### 1. Breadth-First Search (BFS)
- **Working:** Explores all nodes at one depth before going deeper.
- **Application:** Shortest path in unweighted graphs, puzzle solvers.
- **Time Complexity:** O(b^d)
- **Space Complexity:** O(b^d)

#### 2. Depth-First Search (DFS)
- **Working:** Explores a path as deep as possible before backtracking.
- **Application:** Maze traversal, topological sorting.
- **Time Complexity:** O(b^m)
- **Space Complexity:** O(bm)

#### 3. Iterative Deepening Search (IDS)
- **Working:** Combines DFS and BFS by gradually increasing depth.
- **Application:** Game trees (like chess), complete & optimal.
- **Time/Space Complexity:** O(b^d), O(bd)

#### 4. Bidirectional Search
- **Working:** Searches from both start and goal nodes.
- **Application:** Pathfinding where the goal state is known.
- **Time/Space Complexity:** O(b^(d/2))

#### 5. Depth-Limited Search
- **Working:** DFS with a predefined depth limit.
- **Application:** Avoids infinite loop in DFS on cyclic graphs.
- **Time/Space Complexity:** O(b^l), where l = limit

---

### 🧠 Informed (Heuristic) Search

#### 6. Best-First Search
- **Working:** Uses heuristic to prioritize nodes with lower cost.
- **Application:** Route finding, robotics.
- **Time Complexity:** O(b^m)
- **Space Complexity:** O(b^m)

#### 7. A* Search
- **Working:** Uses `f(n) = g(n) + h(n)` (cost + heuristic)  
- **Application:** GPS systems, games, AI pathfinding.
- **Time Complexity:** Exponential in worst case
- **Space Complexity:** Exponential

#### 8. AO* Algorithm
- **Working:** AND-OR graph traversal for decision trees with conditions.
- **Application:** Planning, decision support systems.
- **Time/Space Complexity:** Depends on graph structure (exponential in worst)

---

## 📚 Local Search

### 🔼 Hill Climbing
- **Working:** Moves in direction of increasing value (gradient-based).
- **Application:** Optimization problems, robotic movement.
- **Limitation:** Gets stuck in local maxima.
- **Time/Space Complexity:** O(n)

### 🔽 Beam Search
- **Working:** Explores only the top-k best nodes at each level.
- **Application:** NLP (speech recognition), game AI.
- **Time/Space Complexity:** O(km), where `k` is beam width and `m` is depth

---

## 📚 Game Playing Algorithms

### ♟️ Min-Max Algorithm
- **Working:** Two-player decision-making tree where one minimizes the opponent's score while maximizing their own.
- **Application:** Chess, Tic-Tac-Toe, Checkers
- **Time Complexity:** O(b^d)
- **Space Complexity:** O(bd)

### ✂️ Alpha-Beta Pruning
- **Working:** Prunes branches that won’t affect final decision in Min-Max.
- **Application:** Efficient adversarial games
- **Time Complexity:** O(b^(d/2)) – much faster than Min-Max
- **Space Complexity:** O(bd)



