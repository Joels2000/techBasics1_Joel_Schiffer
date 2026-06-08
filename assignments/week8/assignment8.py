#before: install pygame in terminal (pip install pygame)
import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 8: Sunset Generative Animation")
clock = pygame.time.Clock()

# I changed the name to SunsetCloud because it fits my actual image much better!
class SunsetCloud:
    def __init__(self, image_path):
        self.base_image = pygame.image.load(image_path).convert_alpha()
        
        self.size = random.randint(50, 100)
        self.image = pygame.transform.scale(self.base_image, (self.size, self.size))
        
        # Tinting the image with warm sunset colors (Reds, Oranges, Purples)
        # This enhances the natural colors of my sunset photo!
        self.color = (random.randint(200, 255), random.randint(100, 180), random.randint(50, 150))
        self.image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)
        
        # Random starting positions across the screen
        self.x = random.randint(100, WIDTH - 100)
        self.base_y = random.randint(100, HEIGHT - 100) # Anchor point for the wavy float
        self.y = self.base_y
        
        # Unique speeds so some clouds drift faster than others
        self.speed_x = random.choice([-2, -1, 1, 2]) # Slower speed for a calm breeze effect
        self.wave_speed = random.uniform(0.01, 0.04) # Smooth, slow wobble
        self.wave_amplitude = random.randint(20, 50) # How high it floats up and down
        
        # Every instance tracks its own math angle independently
        self.angle = random.uniform(0, math.pi * 2)

    def update(self):
        self.x += self.speed_x
        # This makes them float up and down gently
        self.angle += self.wave_speed
        self.y = self.base_y + math.sin(self.angle) * self.wave_amplitude
        
        # If a cloud drifts off-screen, it spawns on the other side
        if self.x > WIDTH + self.size:
            self.x = -self.size
        elif self.x < -self.size:
            self.x = WIDTH + self.size

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

# A list to hold all our sunset elements
clouds_list = []

for i in range(12):
    new_cloud = SunsetCloud("my_image.png")
    clouds_list.append(new_cloud)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Refreshing the background to a dark twilight purple/blue instead of pitch black
    screen.fill((25, 20, 40))
    
    for cloud in clouds_list:
        cloud.update()  
        cloud.draw(screen) 
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
