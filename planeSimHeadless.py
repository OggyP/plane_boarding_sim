from plane import Plane
from config import Sim_Config
from passengers import *


class Plane_Simulation:
    def __init__(self) -> None:
        self.current_tick = 0
        self.sim_running = True
        self.config = Sim_Config()
        self.plane = Plane(self.config)
        self.running = True

    def tick(self):
        self.plane.draw_and_update_passengers(None)
        self.plane.attempt_to_create_passenger()
        if self.plane.fully_boarded():
            self.running = False
        self.current_tick += 1


