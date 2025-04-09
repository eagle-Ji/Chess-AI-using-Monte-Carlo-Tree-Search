# Chess AI using Monte Carlo Tree Search (MCTS)

This repository contains an implementation of a chess-playing AI using Monte Carlo Tree Search (MCTS) for action selection and Stockfish as an opponent for benchmarking. The agent simulates chess games and evaluates performance using centipawn scores and win/loss/tie counts.

## Overview
- **AI Agent**: Uses MCTS to explore possible moves.
- **Opponent**: Stockfish engine.
- **Environment**: `gym-chess`, with board and move encodings.
- **Evaluation**: Centipawn scores, win/loss/tie statistics.

## Key Features
- Self-play and evaluation mode
- Custom MCTS implementation with UCB1
- Interoperability with Stockfish for stronger opponent evaluation

## Installation
```bash
pip install gym gym-chess python-chess numpy
```

## Stockfish Setup
- Download Stockfish from [https://stockfishchess.org/download/](https://stockfishchess.org/download/)
- Set correct path to the Stockfish executable:
```python
engine = chess.engine.SimpleEngine.popen_uci("path/to/stockfish")
```

## Monte Carlo Tree Search (MCTS)

### Algorithm Steps
1. **Selection**: Traverse the tree using UCB1 until a leaf node.
2. **Expansion**: Add child nodes representing possible legal moves.
3. **Simulation**: Play out a random playout until a terminal state.
4. **Backpropagation**: Update node statistics based on the simulation outcome.

### Upper Confidence Bound (UCB1)
\[
UCB(s,a) = Q(s,a) + C \cdot \sqrt{\frac{\ln N(s)}{N(s,a)}}
\]
Where:
- \( Q(s,a) \): Estimated value of action \( a \) from state \( s \)
- \( N(s) \): Number of visits to state \( s \)
- \( N(s,a) \): Number of times action \( a \) was taken from state \( s \)
- \( C \): Exploration constant (typically \( \approx \sqrt{2} \) or tuned empirically)

### Reward Function
```python
def give_reward(result):
    if result == "1/2-1/2":
        return 0.5
    elif result == "0-1":
        return -1
    elif result == "1-0":
        return 1.0
```

## Evaluation Metrics
- **Centipawn Score** (from Stockfish)
- **Game Outcome**: Win (1), Loss (-1), Tie (0.5)
- **Game Length**: Number of moves
- **FEN Tracking**: Each state saved in Forsyth-Edwards Notation

## How to Use
1. Load the chess environment
2. Initialize the board and MCTS root node
3. Play moves using:
   - MCTS for agent (White)
   - Stockfish for opponent (Black)
4. Track evaluations, results, and FENs

## Sample Output
```
Board state:
. . . q k b n r
. . . . . p p p
p . . . . . . .
. . . . . . . .
. . . . . P . .
. . . . . . . .
P P P P . . P P
R N B Q K B N R

Game result: 1-0
Centipawn eval: +113
```

## Limitations
- MCTS is not learning across games
- No neural network guidance
- Simple random rollout policy

## Future Work
- Integrate a neural network for value and policy estimation (like AlphaZero)
- Add experience replay / Q-table persistence
- Improve reward shaping and playout heuristics

## License
MIT License

## Author
Suleman Sahib

Feel free to fork or contribute improvements!

