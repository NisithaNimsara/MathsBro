# MathsBro

MathsBro is a Python console-based single-player game that helps players practice and improve basic arithmetic skills through short, focused rounds. It generates randomized arithmetic questions across four modes (Demo, Easy, Medium, Hard). Difficulty, operand ranges, and operations adapt by mode. The game gives immediate feedback, tracks progress during a session, and supports multiple rounds.

## Features

- Four play modes:
  - Demo — quick showcase of game flow and question types
  - Easy — beginner-friendly operands and operations
  - Medium — intermediate challenge with larger numbers and mixed operations
  - Hard — highest difficulty with larger ranges and faster pace
- Random arithmetic questions (addition, subtraction, multiplication; division behavior depends on mode/implementation)
- Immediate feedback after each answer
- Session stats: correct / incorrect counts and accuracy percentage
- Multiple rounds per session; configurable question counts

## Requirements

- Python 3.8 or newer
- No external libraries (uses only Python standard library)

## Quick start

1. Clone the repository
   ```bash
   git clone https://github.com/NisithaNimsara/MathsBro.git
   ```

2. Change into the project directory
   ```bash
   cd MathsBro
   ```

3. Run the launcher or a mode directly
   - Run launcher (if mathbro.py is the main menu/launcher):
     ```bash
     python mathbro.py
     ```
   - Run a specific mode:
     ```bash
     python demo.py
     python easy.py
     python medium.py
     python hard.py
     ```

(Use python3 instead of python if your environment requires it.)

## How to play

- Launch the game or a specific mode file.
- You will be presented with a sequence of arithmetic questions.
- Type your numeric answer and press Enter.
- The game reports whether the answer was correct and updates session stats.
- At the end of the round, a summary is shown showing total, correct, incorrect, and accuracy.

Example session excerpt:
> Question 1: 7 + 5 = ?
> 12
> Correct!
> Question 2: 9 × 4 = ?
> 36
> Correct!
> ---
> Round summary: 2/2 correct — 100%

## Repository files

- `mathbro.py` — core game logic and launcher
- `demo.py` — demo mode script
- `easy.py` — easy mode script
- `medium.py` — medium mode script
- `hard.py` — hard mode script
- `spec.pdf` — project specification
- `DOC 334 ICW 20240281.pdf` — additional documentation

## Configuration & Customization

Open the mode scripts or `mathbro.py` to change:
- Number of questions per round
- Operand ranges per mode
- Which operations are used
- Any time limits or scoring adjustments (if supported)

Suggested improvements:
- Add division support with integer-only results or fraction handling
- Add configurable timers per question or round
- Persist high scores to JSON or SQLite
- Add unit tests for question generation and scoring logic
- Create a GUI or web interface reusing `mathbro.py` logic

## Contributing

Contributions welcome. Suggested workflow:

1. Fork the repository
2. Create a branch: `git checkout -b feat/my-feature`
3. Implement and test changes
4. Commit and push, then open a pull request with a clear description and testing steps

Please add tests and update README/specs for any behaviour changes.

## Troubleshooting

- If input isn't being accepted, ensure the terminal supports stdin and you're running with Python 3.
- For encoding issues, run Python with UTF-8 or set the terminal encoding appropriately.
