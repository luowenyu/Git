# 🏖️ Beach Shooter Game - Scrolling Edition

A fun pygame shooting game featuring a surfer defending the beach against sea monsters with endless scrolling!

## 🎮 Game Features

- **Scrolling Beach Background**: Continuous scrolling with parallax effect for depth
- **Animated Scenery**: Scrolling clouds, palm trees, and ocean waves
- **Cartoon Characters**: Play as a cute cartoon surfer character
- **Enemies**: Fight off cartoon sea monsters trying to invade the beach
- **Shooting Mechanics**: Fire water splash bullets at enemies
- **Progressive Difficulty**: Game speeds up and enemies spawn faster as you travel further
- **Health System**: Avoid enemies or lose health points
- **Score Tracking**: Earn points for each enemy defeated
- **Distance Tracker**: See how far you've traveled down the beach
- **Wave System**: Survive increasingly difficult waves

## 🕹️ How to Play

### Controls
- **Arrow Keys** or **WASD**: Move the player character
  - ⬆️ W / Up Arrow: Move up
  - ⬇️ S / Down Arrow: Move down
  - ⬅️ A / Left Arrow: Move left
  - ➡️ D / Right Arrow: Move right
- **SPACEBAR**: Shoot water splash bullets
- **R**: Restart game (when game over)

### Gameplay
1. The beach scrolls continuously - you're traveling down an endless coastline!
2. Move your surfer character around the screen to dodge enemies
3. Avoid the sea monsters coming from the top of the screen
4. Shoot the monsters with water splashes (press SPACEBAR)
5. Each monster defeated gives you 10 points
6. Each monster that touches you deals 20 damage
7. The game speeds up the further you travel!
8. Survive as long as possible and travel the farthest distance!

### Objective
- Defend the beach from waves of sea monsters
- Travel the longest distance possible
- Achieve the highest score possible
- Progress through increasingly difficult waves as the game speeds up

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install pygame directly:

```bash
pip install pygame
```

## ▶️ Running the Game

```bash
python beach_shooter.py
```

Or make it executable and run directly:

```bash
chmod +x beach_shooter.py
./beach_shooter.py
```

## 🎯 Game Mechanics

- **Player Health**: Start with 100 HP
- **Enemy Damage**: Each enemy collision deals 20 damage
- **Bullet Damage**: Each bullet deals 10 damage to enemies
- **Enemy Health**: Enemies have 30 HP (3 hits to defeat)
- **Spawn Rate**: Enemies spawn faster with each wave
- **Score System**: 10 points per enemy defeated
- **Wave Progression**: New wave every 100 points

## 🎨 Visual Elements

- **Player**: Cartoon surfer with blue swimwear
- **Enemies**: Purple sea monsters with red eyes and teeth
- **Bullets**: Light blue water splash projectiles
- **Scrolling Background**:
  - Blue sky with floating clouds (parallax scrolling)
  - Fixed sun in the sky
  - Animated ocean waves with scrolling texture
  - Scrolling sandy beach
  - Multiple palm trees that scroll past
  - Multi-layered parallax scrolling for depth effect

## 🏆 Tips for High Scores and Distance

1. Keep moving to avoid enemies as the game speeds up
2. Shoot continuously - there's a short cooldown between shots
3. Focus on enemies at the top of the screen first
4. Use the edges of the screen for strategic positioning
5. Don't let enemies pile up - eliminate them quickly!
6. Watch the scrolling palm trees - they can help you judge speed
7. The further you travel, the faster everything moves - stay alert!
8. Try to balance survival (avoiding enemies) with scoring (shooting enemies)

## 🔧 Customization

You can easily modify the game by editing `beach_shooter.py`:

- **Scroll Speed**: Adjust `self.scroll_speed` in BeachShooter class (default: starts at 2)
- **Difficulty**: Adjust `spawn_rate` in the game loop
- **Colors**: Modify the color constants at the top
- **Player Speed**: Change `self.speed` in the Player class
- **Enemy Speed**: Adjust the speed range in the Enemy class
- **Damage Values**: Modify damage in collision detection
- **Number of Clouds/Trees**: Change the count in `self.clouds` and `self.palm_trees` initialization

## 📝 System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.7+
- **RAM**: 256 MB minimum
- **Display**: 800x600 resolution or higher

## 🐛 Troubleshooting

**Game won't start:**
- Make sure pygame is installed: `pip install pygame`
- Check Python version: `python --version`

**Performance issues:**
- Close other applications
- Update graphics drivers
- Reduce FPS in code if needed

**Controls not working:**
- Make sure the game window has focus (click on it)
- Try both arrow keys and WASD

## 📄 License

This game is open source and free to modify and distribute.

## 🎉 Have Fun!

Enjoy defending the beach from sea monsters! Try to beat your high score and challenge your friends!
