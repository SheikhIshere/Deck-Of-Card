# 🂡 Card Game — Trick-Taking Game

![GitHub repo size](https://img.shields.io/badge/repo-ready-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-yellow)

A polished, beginner-friendly Python trick-taking card game where **you** play against three AI opponents. Clean emoji-based card display, rule-enforced moves, and a lightweight CLI experience.

---

## 🔥 Highlights
- Beautiful emoji card UI in terminal 🎴  
- Rule-aware AI opponents (follow suit, choose smart plays) 🤖  
- Input validation with ✅ (valid) / ❌ (invalid) hints  
- Lightweight — no heavy dependencies, runs on Python 3.6+ ⚡  
- Easy to read, extend, and integrate into other projects 🧩

---

## 📋 Table of Contents
1. [Quick Start](#-quick-start)  
2. [Project Structure](#-project-structure)  
3. [How to Play](#-how-to-play)  
4. [Rules & Mechanics](#-rules--mechanics)  
5. [Configuration & Git Troubleshooting](#-configuration--git-troubleshooting)  
6. [Contributing](#-contributing)  
7. [Troubleshooting](#-troubleshooting)  
8. [License & Credits](#-license--credits)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher  
- Terminal that supports Unicode emojis (modern terminals like GNOME Terminal, Windows Terminal, iTerm2)

### Install & Run
```bash
# Clone the repo
git clone https://github.com/your-username/card-game.git
cd card-game

# Run the game
python main.py
# Or on some systems:
python3 main.py
```

---

## 📁 Project Structure

```
card-game/
├── main.py                 # 🎮 Game entry point & welcome screen
├── game_logic.py           # ⚙️ Core game mechanics & round management
├── deck_logic.py           # 🃏 Deck creation, shuffling, card dealing
├── player_logic.py         # 👥 Player classes (User + 3 Bots)
├── card_pair_to_emoji.py   # 🎨 Card tuple to emoji conversion
└── README.md              # 📖 This file
```

### File Descriptions
- **`main.py`**: Launches the game with welcome screen and clean UI
- **`game_logic.py`**: Handles round flow, winner determination, and game rules
- **`deck_logic.py`**: Manages 52-card deck, shuffling, and distribution
- **`player_logic.py`**: Defines Player, UserPlayer, and Bot classes with game logic
- **`card_pair_to_emoji.py`**: Converts (suit, rank) tuples to Unicode card emojis

---

## 🎮 How to Play

### Game Flow
1. **Setup**: 52 cards are shuffled and dealt to 4 players (13 cards each)
2. **First Round**: Random player starts; subsequent rounds led by previous winner
3. **Your Turn**: 
   - Cards displayed as emojis with validity indicators
   - ✅ = Legal move | ❌ = Invalid (must follow suit if possible)
   - Enter card number (0-12) to play
4. **Bot Turns**: AI plays automatically with 1-second delay for realism
5. **Round End**: Winner is determined, scores updated
6. **Game End**: Final results when all 13 rounds complete

### Example Turn
```
🔄 Round starting! Cards remaining: 13
==================================================

Your cards:
  🂡  🂢  🂣  🂤  🂥  🂦  🂧  🂨  🂩  🂪  🂫  🂭  🂮  

Choose a card (0-12): 3
🧒 You play: 🂤
🤖 Bot1 plays: 🂭
🤖 Bot2 plays: 🃍
🤖 Bot3 plays: 🃞

🎉 User wins the round!
```

---

## 📜 Rules & Mechanics

### Card Hierarchy
| **Rank** (Strong → Weak) | **Suit** (Strong → Weak) |
|--------------------------|--------------------------|
| A (Ace)                  | ♠ Spades                 |
| K (King)                 | ♥ Hearts                 |
| Q (Queen)                | ♦ Diamonds               |
| J (Jack)                 | ♣ Clubs                  |
| 10 → 2 (Numerical)       |                          |

### Game Rules
1. **Leading Suit**: First player sets the suit; others must follow if possible
2. **Following Suit**: Players must play same suit if holding it
3. **Spreading**: If unable to follow suit, any card may be played
4. **Winning Tricks**: Highest card of leading suit wins the round
5. **Tie Breaker**: Same rank? Higher suit wins (Spades > Hearts > Diamonds > Clubs)
6. **Next Round**: Winner leads the next trick

### AI Strategy
- **Follows suit** when possible
- **Plays lowest valid card** when leading
- **Strategic discards** when spreading (preserves high cards)
- **1-second delays** for natural gameplay feel

---

## ⚙️ Configuration & Git Troubleshooting

### File Requirements
Ensure these files are in the same directory:
```bash
main.py
game_logic.py
deck_logic.py
player_logic.py
card_pair_to_emoji.py
```

### Git Setup (For Developers)
```bash
# Initial repository setup
git init
git add .
git commit -m "Initial commit: Trick-taking card game"
git branch -M main
git remote add origin https://github.com/your-username/card-game.git
git push -u origin main
```

### Python Compatibility
- ✅ Python 3.6+
- ✅ Cross-platform (Windows/macOS/Linux)
- ✅ No external dependencies

---

## 🤝 Contributing

### Areas for Enhancement
- **Difficulty Levels**: Easy/Medium/Hard AI strategies
- **Multi-round Games**: Best-of-3 or tournament modes
- **Card Animations**: Smooth card play transitions
- **Sound Effects**: Audio feedback for plays and wins
- **Statistics**: Player performance tracking

### Contribution Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Emojis not displaying** | Use modern terminal: Windows Terminal, iTerm2, or GNOME Terminal |
| **"python not found"** | Use `python3` on Linux/Mac or ensure Python is in PATH |
| **Invalid card selection** | Follow ✅ indicators - must follow leading suit if possible |
| **Import errors** | Check all files are in same directory and named correctly |
| **Game crashes** | Ensure Python 3.6+ and terminal supports Unicode |

### Quick Fix Test
```python
# Test emoji support
python -c "print('🎴 🂡 🂱 🃁 🃑')"
# If cards display, your terminal supports the game
```

---

## 📄 License & Credits

### License
MIT License - feel free to use in personal and educational projects.

### Credits
- **Game Design**: Classic trick-taking mechanics
- **Emoji System**: Unicode Playing Cards block (U+1F0A0–U+1F0FF)
- **Code Architecture**: Clean, modular Python design

### Acknowledgments
Thanks to the Python community for robust standard libraries that make projects like this possible without external dependencies.

---

**Enjoy the game!** 🎉 If you encounter issues, check the troubleshooting section or open an issue on GitHub.

*Ready to play? Run `python main.py` and may the best strategist win!* ♠️♥️♦️♣️
