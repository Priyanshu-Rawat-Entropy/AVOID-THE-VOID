A simple 2D survival game built with **Python** and **Pygame**.
Collect targets, increase your score and grow longer while trying to survive the moving Void!

The goal is simple:
-  Move around the game area
-  Collect the targets
-  Increase your score
-  Grow longer as you collect targets
-  Avoid the moving Void
-  Try to survive as long as possible
The game combines simple movement, collision detection, random spawning, scoring and a continuously moving obstacle.

# Technical Details

| Component | Details |
|-----------|---------|
| Language | Python |
| Game Library | Pygame |
| Window Size | 500 × 500 pixels |
| Game Loop | Custom `game_loop()` function |
| Target FPS | 120 FPS |
| Player Speed | 4 pixels/frame |
| Void Speed | 10 pixels/frame |
| Player Starting Position | (250, 250) |
| Player Growth | 20 pixels |
| Initial Player Length | 1 |
| Background | Black `(0, 0, 0)` |
| Target Color | Red `(225, 0, 0)` |
| Void Color | Light Gray `(225, 225, 225)` |
| Player Body | Random RGB colors |
| Controls | WASD / Arrow Keys |
| Collision Detection | Distance-based |
| Randomization | Python `random` module |
| Timer | Minutes and seconds |

# Objective

Collect the targets to increase your score and grow your player trail.
At the same time, avoid the moving Void.
The longer you survive, the better!



# Requirements

Make sure you have Python installed.

Install Pygame with:
'''text 
   bash
pip install pygame
'''

# Controls

| Key | Action |
|-----|--------|
| ⬆️ W | Move Up |
| ⬇️ S | Move Down |
| ⬅️ A | Move Left |
| ➡️ D | Move Right |
| Enter | Restart |

# Gameplay Video

https://github.com/user-attachments/assets/25b1eef5-b01a-40ee-9940-f10cdd25b137

# Future Improvements
Some features I would like to add:

 - Main menu
 - Start / pause screen
 - Game-over screen
 - High-score system
 - Sound effects
 - Background music
 - Difficulty levels
 - Better graphics
 - Multiple types of obstacles
 - Settings menu
 
