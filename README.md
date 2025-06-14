# 🧠 Rock-Paper-Scissors AI (Python & Tkinter)

A fun Rock-Paper-Scissors game with a smart AI opponent and with a graphical user interface built using Python's `tkinter` module.

The bot tracks your previous moves and adapts its strategy based on your behavior.

---

## 🎮 Features

- 🧠 **Learning AI:** Predicts your next move based on your past choices  
- 🖱️ **Interactive GUI:** Play using buttons 
- 📊 **Live Score Tracking:** Real-time score updates after every round  
- 🪄 **Clean, minimalist design:** Focused on functionality and simplicity

---

## 🧠 How the AI Works

1. The bot keeps a record of your past moves (`rock`, `paper`, or `scissors`)
2. It finds the **most frequent move** you’ve made so far
3. Then it plays the move that **beats** your most frequent move

> Example: If you often choose `rock`, the bot will play `paper`.

---

## 📦 Technologies Used

- Python 3.x  
- `tkinter` (for GUI)  
- `collections.Counter` (to analyze user patterns)  
- No external dependencies

---
```bash
python ai_rps_gui.py
