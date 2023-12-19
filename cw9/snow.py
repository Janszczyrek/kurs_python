import sys
import pygame
import random


class Snowflake(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, scale=1, rotationAngle=0):
        pygame.sprite.Sprite.__init__(self)
        self.freeze = False
        self.image = pygame.image.load("snowflake.png")
        self.image = pygame.transform.rotate(self.image, rotationAngle)
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, width), y)

    def update(self, event_list):
        snowflakesCollided = pygame.sprite.spritecollide(self, snowflakes, 0)
        if self.rect.y > height or len(snowflakesCollided) > 6:
            self.freeze = True
        if not self.freeze:
            self.move_down()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.kill()
        if self.freeze == True and self.rect.y < 0:
            pygame.time.set_timer(DRAW_SNOWFLAKE_EVENT, 0)
            pygame.display.set_caption("Game over!")
    def move_down(self):
        self.rect.x += random.randint(-2, 2)
        self.rect.y += 3


def update_snowflakes(snowflakes, event_list):
    for snowflake in snowflakes:
        snowflake.update(event_list)


DRAW_SNOWFLAKE_EVENT = pygame.USEREVENT
GAME_OVER_EVENT = pygame.USEREVENT

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)

# INITIALIZE THE GAME
pygame.init()  # to zawsze na starcie
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)  # return Surface
pygame.display.set_caption("Snowflakes")
pygame.time.set_timer(DRAW_SNOWFLAKE_EVENT, 200)

font = pygame.font.Font("freesansbold.ttf", 32)

# CLOCK
FPS = 60  # frames per second setting
clock = pygame.time.Clock()


snowflakes = pygame.sprite.Group()

# MAIN GAME LOOP
while True:
    # HANDLE EVENTS
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:  # QUIT Event
            pygame.quit()  # deaktywacja pygame
            sys.exit(0)
        if event.type == DRAW_SNOWFLAKE_EVENT:
            snowflakes.add(
                Snowflake(
                    rotationAngle=random.randint(0, 360), scale=random.uniform(0.5, 2)
                )
            )
    update_snowflakes(snowflakes, event_list)

    screen.fill(black)
    snowflakes.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
