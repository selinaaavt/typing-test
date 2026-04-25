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

1. The program will display a menu and prompt you to start.
2. Press Enter to begin the typing test.
3. A random passage will appear on screen.
4. Type the passage as quickly and accurately as possible.
5. After finishing, your results will be displayed:
   - Time taken
   - WPM (Words Per Minute)
   - Accuracy percentage
6. You can optionally enter your name to save your score.
7. Choose whether to view the leaderboard or play again.

---

## 🏆 Leaderboard
- Scores are saved automatically in `leaderboard.json`
- Displays the top 10 highest scores
- Sorted by:
  1. Highest WPM
  2. Highest accuracy (if WPM is tied)

---

## 📁 File Structure
```
project-folder/
│
├── typing_test.py
├── leaderboard.json (created automatically after first score)
└── README.md
```

---

## ❗ Special Setup Notes
- No external packages or API keys are required
- No additional setup is needed
- The leaderboard file (`leaderboard.json`) will be created automatically when the first score is saved

---

## 👨‍💻 Summary
This project demonstrates Python fundamentals including functions, loops, file handling, and basic performance measurement logic. It is designed as a simple but effective typing practice tool.