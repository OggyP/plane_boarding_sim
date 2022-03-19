import pygame
from plane import Plane
from config import Sim_Config
from passengers import *


class Plane_Simulation:
    def __init__(self, fps) -> None:
        self.fps = fps
        self.running = True
        self.current_tick = 0
        self.sim_running = True
        self.config = Sim_Config()
        self.plane = Plane(self.config)
        self.WINDOW = pygame.display.set_mode(
            (int(self.config.WIDTH), int(self.config.HEIGHT)))
        self.clock = pygame.time.Clock()

        pygame.display.init()
        pygame.display.set_caption("Plane Boarding / Exiting Simulation")

        while self.running:
            self.tick()

    def tick(self):
        self.clock.tick(self.fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()

        self.WINDOW.fill((0, 0, 0))
        self.plane.draw_seats(self.WINDOW)
        self.plane.draw_and_update_passengers(self.WINDOW)
        self.plane.attempt_to_create_passenger()

        pygame.display.update()

        self.current_tick += 1
