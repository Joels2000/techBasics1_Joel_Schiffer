import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 8: Generative Class Animation")
clock = pygame.time.Clock()

class SpaceOrb:
    def __init__(self, image_path):
        # I'm loading the base image passed from the main program
        self.base_image = pygame.image.load(image_path).convert_alpha()
    
        self.size = random.randint(30, 70)
        self.image = pygame.transform.scale(self.base_image, (self.size, self.size))
      
        # This lets me use ONE image asset but get a whole spectrum of colors
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(150, 255))
        self.image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)
      
        self.x = random.randint(100, WIDTH - 100)
        self.base_y = random.randint(100, HEIGHT - 100) # Anchor point for non-linear wave
        self.y = self.base_y
        
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.wave_speed = random.uniform(0.02, 0.07) # How fast it wobbles
        self.wave_amplitude = random.randint(20, 60) # How high/low it wobbles
      
        self.angle = random.uniform(0, math.pi * 2)

    def update(self):
        self.x += self.speed_x
        
        # This makes the orb bob up and down smoothly like it's floating on water
        self.angle += self.wave_speed
        self.y = self.base_y + math.sin(self.angle) * self.wave_amplitude
        
        if self.x > WIDTH + self.size:
            self.x = -self.size
        elif self.x < -self.size:
            self.x = WIDTH + self.size

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))


# I created a list to hold all my objects so I can update them all at once in a loop
orbs_list = []

# Spawning 15 completely unique instances using a loop
for i in range(15):
    try:
        # Creating the object and appending it to our list
        new_orb = SpaceOrb("orb.png")
        orbs_list.append(new_orb)
    except Exception as e:
        print("Error loading 'orb.png'. Make sure the image is in the same folder!")
        pygame.quit()
        sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    screen.fill((10, 10, 25))
    
    # Iterating through my list to update and draw every object
    for orb in orbs_list:
        orb.update()  # Calculates its next non-linear position
        orb.draw(screen) # Renders it to the screen
        
    pygame.display.flip()
    
    # Cap the frame rate at 60 FPS so it runs smoothly on all computers
    clock.tick(60)

pygame.quit()
