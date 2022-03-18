import pygame
import plane
from config import *
from passengers import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.init()
pygame.display.set_caption("Plane Boarding / Exiting Simulation")

clock = pygame.time.Clock()

sim_running = True

key_pressed = True

tick = 0

while sim_running:
    # clock.tick(MAX_MOVEMENT_SPEED / SEAT_DIMENSIONS[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sim_running = True
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            key_pressed = True

    # if key_pressed:
    WINDOW.fill((0, 0, 0))
    plane.draw_seats(WINDOW)
    plane.draw_and_update_passengers(WINDOW)
    plane.attempt_to_create_passenger()
    pygame.display.update()
    # pygame.image.save(WINDOW, "./frames/frame_" + str(tick) + ".jpeg")
    tick += 1
    key_pressed = False
