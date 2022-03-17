import pygame
import plane
from config import *
from passengers import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.init()
pygame.display.set_caption("Plane Boarding / Exiting Simulation")

clock = pygame.time.Clock()

sim_running = True

while sim_running:
    clock.tick(MAX_MOVEMENT_SPEED / SEAT_DIMENSIONS[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sim_running = True
            pygame.quit()
            exit()

    WINDOW.fill((0, 0, 0))
    plane.draw_seats(WINDOW)
    plane.draw_and_update_passengers(WINDOW)
    plane.attempt_to_create_passenger()
    pygame.display.update()