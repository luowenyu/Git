# 🏖️ Beach Shooter Game

A fun pygame shooting game featuring a surfer defending the beach against sea monsters!

## 🎮 Game Features

- **Beautiful Beach Background**: Animated ocean waves, palm trees, and a sunny sky
- **Cartoon Characters**: Play as a cute cartoon surfer character
- **Enemies**: Fight off cartoon sea monsters trying to invade the beach
- **Shooting Mechanics**: Fire water splash bullets at enemies
- **Progressive Difficulty**: Enemies spawn faster as you progress through waves
- **Health System**: Avoid enemies or lose health points
- **Score Tracking**: Earn points for each enemy defeated
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
1. Move your surfer character around the screen
2. Avoid the sea monsters coming from the top
3. Shoot the monsters with water splashes (press SPACEBAR)
4. Each monster defeated gives you 10 points
5. Each monster that touches you deals 20 damage
6. Survive as long as possible and get the highest score!

### Objective
- Defend the beach from waves of sea monsters
- Achieve the highest score possible
- Progress through increasingly difficult waves

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
- **Background**:
  - Blue sky with sun
  - Animated ocean waves
  - Sandy beach
  - Palm tree decoration

## 🏆 Tips for High Scores

1. Keep moving to avoid enemies
2. Shoot continuously - there's a short cooldown between shots
3. Focus on enemies at the top of the screen first
4. Use the edges of the screen for strategic positioning
5. Don't let enemies pile up - eliminate them quickly!

## 🔧 Customization

You can easily modify the game by editing `beach_shooter.py`:

- **Difficulty**: Adjust `spawn_rate` in the game loop
- **Colors**: Modify the color constants at the top
- **Player Speed**: Change `self.speed` in the Player class
- **Enemy Speed**: Adjust the speed range in the Enemy class
- **Damage Values**: Modify damage in collision detection

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
