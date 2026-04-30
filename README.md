# Typing Speed Test Project

## 📌 Project Description
This project is a terminal-based typing speed test application built in Python. It allows users to practice typing by displaying random text passages and measuring their performance in real time.

The program calculates:
- Words Per Minute (WPM) based on typing speed
- Accuracy percentage by comparing typed input to the original passage
- It also stores results in a leaderboard so users can track their progress over time

The leaderboard is saved locally using a JSON file, allowing scores to persist between runs.

---

## ⚙️ Features
- Random typing passages for practice
- Real-time timing of typing speed
- WPM calculation using standard 5-character word method
- Character-by-character accuracy checking
- Persistent leaderboard stored in `leaderboard.json`
- Leaderboard ranked by a combined WPM × accuracy score so fast but inaccurate scores don't unfairly dominate
- Input validation that re-prompts on unexpected answers (e.g. extra spaces, wrong letters)
- Option to replay multiple rounds

---

## 📦 Requirements
This project uses only built-in Python libraries, so no external installations are required.

Built-in modules used:
- time
- random
- json
- os

Make sure you have:
- Python 3.x installed

You can check your Python version with:
```
python --version
```

---

## 🚀 How to Run the Project

1. Download or clone the project files onto your computer.
2. Open a terminal (Command Prompt, Terminal, or VS Code terminal).
3. Navigate to the folder containing the Python file.
4. Run the program using:

```
python typing_test.py
```

---

## 🧠 How to Use

1. The program will prompt you to press Enter to start.
2. A random passage will appear on screen.
3. Type the passage as quickly and accurately as possible and press Enter.
4. After finishing, your results will be displayed:
   - Time taken
   - WPM (Words Per Minute)
   - Accuracy percentage
5. You can optionally enter your name to save your score.
6. Choose whether to view the leaderboard or play again.
   - If you type something other than y/n, the program will re-prompt you.

---

## 🏆 Leaderboard
- Scores are saved automatically in `leaderboard.json`
- Displays the top 10 highest scores
- Sorted by a **combined WPM × accuracy score**
  - Example: 100 WPM at 50% accuracy scores 50, while 70 WPM at 95% accuracy scores 66.5 and ranks higher
  - This ensures the leaderboard rewards both speed and accuracy, not just speed

---

## 📁 File Structure
```
project-folder/
│
├── typingtest.py
├── leaderboard.json (created automatically after first score)
└── README.md
```

---

## ❗ Special Setup Notes
- No external packages or API keys are required
- No additional setup is needed
- The leaderboard file (`leaderboard.json`) will be created automatically when the first score is saved

---

## 🤖 External Contributors & AI Usage

### Generative AI — Claude (Anthropic)
We used Claude as an AI assistant during the final polish stage of this project. Here is a detailed description of how we used it and what it contributed:

We used Claude to help clean up our code comments for the final submission. Our original comments explained almost every line, including ones that were self-explanatory. We asked Claude to trim them down so only important or non-obvious lines were commented, following the project rubric's guidance. Claude did not change any logic — it only removed redundant comments and kept the ones that explained the *why* behind tricky lines (e.g. why we divide by `len(target)`, why we multiply WPM by accuracy for ranking).

**What we wrote:**
All original program logic, structure, and design were written by us. Claude's contributions were limited to the three bug fixes and comment cleanup described above, all of which we reviewed and understood.

---

## 👨‍💻 Summary
This project demonstrates Python fundamentals including functions, loops, file I/O with JSON, and basic performance measurement logic. It is designed as a simple but effective typing practice tool with persistent scoring across sessions.
