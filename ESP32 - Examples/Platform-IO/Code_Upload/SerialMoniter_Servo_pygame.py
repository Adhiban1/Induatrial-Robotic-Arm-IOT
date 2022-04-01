import pygame
import serial
from math import *
from time import time

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = "COM3"
serialInst.open()

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

init_time = time()

while True:
    clock.tick(60)
    display.fill((0, 0, 0))
    text = font.render(f"{pygame.mouse.get_pos()}", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (width // 2 + 400, height // 2 - 280)
    display.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                display.fill((255, 255, 255))

    pygame.draw.line(display, (255, 255, 255), (0, height / 2), (width, height / 2))
    pygame.draw.line(display, (255, 255, 255), (width / 2, 0), (width / 2, height))

    x1 = pygame.mouse.get_pos()[0]
    y1 = pygame.mouse.get_pos()[1]
    d = sqrt((width / 2 - x1) ** 2 + (height / 2 - y1) ** 2)
    if d < 2 * 100 * sqrt(2):
        t = acos(d / (2 * 100 * sqrt(2))) + acos((x1 - width / 2) / d)

        if time() - init_time > 2:
            print(t * 180 / pi)
            serialInst.write(str(t * 180 / pi).encode("utf-8"))
            init_time = time()

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
