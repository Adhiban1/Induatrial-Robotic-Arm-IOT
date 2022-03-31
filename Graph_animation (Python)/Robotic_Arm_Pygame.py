import pygame
from math import *

pygame.init()
width = 1200
height = 630
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Robotic Arm")
clock = pygame.time.Clock()

font = pygame.font.Font("freesansbold.ttf", 32)
text = font.render("GeeksForGeeks", True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (width // 2, height // 2)

while True:
    clock.tick(60)
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                display.fill((255, 255, 255))

    # pygame.draw.line(
    #     display,
    #     (255, 0, 0),
    #     (width / 2, height / 2),
    #     (width / 2 - 100, height / 2 - 100),
    #     5,
    # )
    # pygame.draw.line(
    #     display,
    #     (255, 0, 0),
    #     (width / 2 - 100, height / 2 - 100),
    #     (width / 2, height / 2 - 200),
    #     5,
    # )

    pygame.draw.line(display, (255, 255, 255), (0, height / 2), (width, height / 2))
    pygame.draw.line(display, (255, 255, 255), (width / 2, 0), (width / 2, height))
    # pygame.draw.circle(display, (0, 255, 0), (width / 2 - 100, height / 2 - 100), 10)
    # pygame.draw.circle(display, (0, 255, 0), (width / 2, height / 2 - 200), 10)

    x1 = pygame.mouse.get_pos()[0]
    y1 = pygame.mouse.get_pos()[1]
    d = sqrt((width / 2 - x1) ** 2 + (height / 2 - y1) ** 2)
    if d < 2 * 100 * sqrt(2):

        # pygame.draw.line(
        #     display, (100, 100, 100), (width / 2, height / 2), pygame.mouse.get_pos()
        # )
        # pygame.draw.circle(
        #     display, (100, 100, 100), ((x1 + width / 2) / 2, (height / 2 + y1) / 2), 5
        # )
        t = acos(d / (2 * 100 * sqrt(2))) + acos((x1 - width / 2) / d)
        pygame.draw.line(
            display,
            (255, 0, 0),
            (width / 2, height / 2),
            (width / 2 + 100 * sqrt(2) * cos(t), height / 2 - 100 * sqrt(2) * sin(t)),
            5,
        )
        pygame.draw.line(
            display,
            (255, 0, 0),
            (width / 2 + 100 * sqrt(2) * cos(t), height / 2 - 100 * sqrt(2) * sin(t)),
            (x1, y1),
            5,
        )
        pygame.draw.circle(
            display,
            (0, 255, 0),
            (width / 2 + 100 * sqrt(2) * cos(t), height / 2 - 100 * sqrt(2) * sin(t)),
            10,
        )
        pygame.draw.circle(display, (0, 255, 0), (x1, y1), 10)
        pygame.draw.circle(display, (0, 255, 0), (width / 2, height / 2), 10)
    else:
        pygame.draw.circle(display, (100, 100, 100), (width / 2, height / 2), 10)
    pygame.display.update()
