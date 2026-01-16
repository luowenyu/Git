#!/usr/bin/env python3
"""
Beach Shooter Game
A fun pygame shooting game with sea beach background and cartoon characters
"""

import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
SAND = (238, 214, 175)
WATER = (64, 164, 223)
DARK_WATER = (41, 128, 185)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

class Player(pygame.sprite.Sprite):
    """Player character - a cartoon surfer"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 60), pygame.SRCALPHA)
        self.draw_player()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = 100
        self.max_health = 100
        self.shoot_cooldown = 0

    def draw_player(self):
        """Draw a cartoon surfer character"""
        # Head (circle)
        pygame.draw.circle(self.image, (255, 220, 177), (25, 15), 12)
        # Eyes
        pygame.draw.circle(self.image, BLACK, (20, 13), 2)
        pygame.draw.circle(self.image, BLACK, (30, 13), 2)
        # Smile
        pygame.draw.arc(self.image, BLACK, (18, 10, 14, 10), 3.14, 6.28, 2)
        # Body (rectangle with rounded edges)
        pygame.draw.ellipse(self.image, (0, 150, 255), (15, 25, 20, 25))
        # Arms
        pygame.draw.line(self.image, (255, 220, 177), (15, 30), (5, 40), 4)
        pygame.draw.line(self.image, (255, 220, 177), (35, 30), (45, 40), 4)
        # Legs
        pygame.draw.line(self.image, (0, 100, 200), (20, 50), (15, 60), 5)
        pygame.draw.line(self.image, (0, 100, 200), (30, 50), (35, 60), 5)

    def update(self):
        """Update player position based on key presses"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Keep player on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def shoot(self):
        """Create a bullet"""
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 15
            return Bullet(self.rect.centerx, self.rect.top)
        return None

class Enemy(pygame.sprite.Sprite):
    """Enemy character - a cartoon sea monster"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((45, 45), pygame.SRCALPHA)
        self.draw_enemy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1, 3)
        self.health = 30
        self.direction = random.choice([-1, 1])

    def draw_enemy(self):
        """Draw a cartoon sea monster"""
        # Body (blob shape)
        pygame.draw.ellipse(self.image, (150, 50, 200), (5, 10, 35, 30))
        # Eyes (angry)
        pygame.draw.circle(self.image, RED, (15, 20), 5)
        pygame.draw.circle(self.image, RED, (30, 20), 5)
        pygame.draw.circle(self.image, BLACK, (15, 20), 2)
        pygame.draw.circle(self.image, BLACK, (30, 20), 2)
        # Teeth
        for i in range(4):
            points = [(10 + i*7, 35), (13 + i*7, 40), (16 + i*7, 35)]
            pygame.draw.polygon(self.image, WHITE, points)
        # Tentacles
        pygame.draw.circle(self.image, (120, 40, 180), (5, 35), 5)
        pygame.draw.circle(self.image, (120, 40, 180), (40, 35), 5)

    def update(self):
        """Move enemy down the screen with slight horizontal movement"""
        self.rect.y += self.speed
        self.rect.x += self.direction * 2

        # Change direction occasionally
        if random.randint(0, 50) == 0:
            self.direction *= -1

        # Remove if off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    """Player's bullet - water splash"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, 15), pygame.SRCALPHA)
        # Draw a water splash bullet
        pygame.draw.ellipse(self.image, (100, 200, 255), (0, 0, 8, 15))
        pygame.draw.ellipse(self.image, (150, 220, 255), (1, 2, 6, 11))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        """Move bullet up the screen"""
        self.rect.y -= self.speed

        # Remove if off screen
        if self.rect.bottom < 0:
            self.kill()

class BeachShooter:
    """Main game class"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Beach Shooter")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Create player
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.all_sprites.add(self.player)

        # Game variables
        self.score = 0
        self.enemy_spawn_timer = 0
        self.game_over = False
        self.wave_number = 1

    def draw_background(self):
        """Draw the beach scene background"""
        # Sky
        self.screen.fill(SKY_BLUE)

        # Sun
        pygame.draw.circle(self.screen, YELLOW, (700, 80), 40)
        pygame.draw.circle(self.screen, ORANGE, (700, 80), 35)

        # Ocean waves (animated)
        wave_offset = (pygame.time.get_ticks() // 50) % 40
        for i in range(0, SCREEN_WIDTH + 40, 40):
            pygame.draw.arc(self.screen, DARK_WATER,
                          (i - wave_offset, SCREEN_HEIGHT - 250, 40, 30),
                          0, 3.14, 3)

        # Water
        pygame.draw.rect(self.screen, WATER, (0, SCREEN_HEIGHT - 200, SCREEN_WIDTH, 200))

        # Sand
        pygame.draw.ellipse(self.screen, SAND,
                          (-50, SCREEN_HEIGHT - 150, SCREEN_WIDTH + 100, 180))

        # Palm tree
        self.draw_palm_tree(100, SCREEN_HEIGHT - 140)

    def draw_palm_tree(self, x, y):
        """Draw a simple palm tree"""
        # Trunk
        pygame.draw.rect(self.screen, (139, 90, 43), (x, y - 80, 15, 80))
        # Leaves
        for angle in range(0, 360, 45):
            end_x = x + 7 + int(30 * math.cos(math.radians(angle)))
            end_y = y - 80 + int(20 * math.sin(math.radians(angle)))
            pygame.draw.line(self.screen, GREEN, (x + 7, y - 80), (end_x, end_y), 5)

    def draw_ui(self):
        """Draw the user interface"""
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Wave
        wave_text = self.small_font.render(f"Wave: {self.wave_number}", True, WHITE)
        self.screen.blit(wave_text, (10, 50))

        # Health bar
        health_bar_width = 200
        health_bar_height = 20
        health_ratio = self.player.health / self.player.max_health

        pygame.draw.rect(self.screen, RED,
                        (SCREEN_WIDTH - health_bar_width - 10, 10,
                         health_bar_width, health_bar_height))
        pygame.draw.rect(self.screen, GREEN,
                        (SCREEN_WIDTH - health_bar_width - 10, 10,
                         health_bar_width * health_ratio, health_bar_height))
        pygame.draw.rect(self.screen, WHITE,
                        (SCREEN_WIDTH - health_bar_width - 10, 10,
                         health_bar_width, health_bar_height), 2)

        # Health text
        health_text = self.small_font.render(f"HP: {int(self.player.health)}", True, WHITE)
        self.screen.blit(health_text, (SCREEN_WIDTH - health_bar_width - 10, 35))

    def spawn_enemy(self):
        """Spawn a new enemy"""
        x = random.randint(50, SCREEN_WIDTH - 50)
        enemy = Enemy(x, -50)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def handle_collisions(self):
        """Handle all collision detection"""
        # Bullets hitting enemies
        for bullet in self.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            if hit_enemies:
                bullet.kill()
                for enemy in hit_enemies:
                    enemy.health -= 10
                    if enemy.health <= 0:
                        enemy.kill()
                        self.score += 10

        # Enemies hitting player
        hit_player = pygame.sprite.spritecollide(self.player, self.enemies, True)
        if hit_player:
            self.player.health -= 20
            if self.player.health <= 0:
                self.game_over = True

    def run(self):
        """Main game loop"""
        running = True

        while running:
            self.clock.tick(FPS)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_over:
                        bullet = self.player.shoot()
                        if bullet:
                            self.bullets.add(bullet)
                            self.all_sprites.add(bullet)
                    elif event.key == pygame.K_r and self.game_over:
                        # Restart game
                        self.__init__()

            if not self.game_over:
                # Update
                self.all_sprites.update()

                # Spawn enemies
                self.enemy_spawn_timer += 1
                spawn_rate = max(30, 90 - (self.wave_number * 5))
                if self.enemy_spawn_timer >= spawn_rate:
                    self.spawn_enemy()
                    self.enemy_spawn_timer = 0

                # Increase difficulty
                if self.score > 0 and self.score % 100 == 0:
                    if self.score // 100 > self.wave_number - 1:
                        self.wave_number += 1

                # Handle collisions
                self.handle_collisions()

            # Draw
            self.draw_background()
            self.all_sprites.draw(self.screen)
            self.draw_ui()

            # Game over screen
            if self.game_over:
                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                overlay.set_alpha(128)
                overlay.fill(BLACK)
                self.screen.blit(overlay, (0, 0))

                game_over_text = self.font.render("GAME OVER!", True, RED)
                score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
                restart_text = self.small_font.render("Press R to Restart", True, WHITE)

                self.screen.blit(game_over_text,
                               (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                SCREEN_HEIGHT // 2 - 60))
                self.screen.blit(score_text,
                               (SCREEN_WIDTH // 2 - score_text.get_width() // 2,
                                SCREEN_HEIGHT // 2))
                self.screen.blit(restart_text,
                               (SCREEN_WIDTH // 2 - restart_text.get_width() // 2,
                                SCREEN_HEIGHT // 2 + 60))

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = BeachShooter()
    game.run()
