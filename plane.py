from random import choice
from pygame import Vector2
from config import *
from passengers import *


class Plane:
    def __init__(self, config: Sim_Config) -> None:
        self.config = config
        self.seat_choices: list[Vector2] = []
        position: Vector2 = Vector2(0, 0)
        self.passengers: list[Passenger] = []
        self.seat_shuffles = 0
        for row in self.config.SEATS:
            for area in row:
                if area == 'E' or area == 'S':
                    self.seat_choices.append(Vector2(position.x, position.y))
                position.x += 1
            position.x = 0
            position.y += 1

    def draw_and_update_passengers(self, WINDOW: pygame.Surface or None) -> None:
        for passenger in self.passengers:
            if WINDOW is not None:
                passenger.render(self, WINDOW)
            person_update_info = passenger.update(self.passengers, self)
            if person_update_info != None and person_update_info != 'Done':
                if isinstance(person_update_info, list):
                    for update_info in person_update_info:
                        self.get_passengers(
                            update_info[0]).go_to = update_info[1]
                elif person_update_info == 'Done':
                    pass
                elif person_update_info == 'Moved':
                    self.passengers.insert(0, self.passengers.pop(
                        self.passengers.index(passenger)))

    def attempt_to_create_passenger(self):
        if self.get_passengers(self.config.STARTING_POSITION) == None:
            if not len(self.seat_choices):
                return
            ending_pos = choice(self.seat_choices)
            self.seat_choices.remove(ending_pos)
            self.create_passenger(self.config.STARTING_POSITION, ending_pos)

    def create_passenger(self, position: Vector2, ending_position: Vector2):
        self.passengers.append(Passenger(position, ending_position, self))

    def get_passengers(self, position: Vector2):
        for passenger in self.passengers:
            if int(passenger.pos.x) == int(position.x) and int(passenger.pos.y) == int(position.y):
                return passenger

        return None

    def draw_seats(self, WINDOW: pygame.Surface):
        current_row_number = 0  # 0 is row 1, 1 is row 2 etc
        for row in self.config.SEATS:
            seat_within_row_number = 0
            for seat in row:
                if seat != '_':
                    seat_rect = pygame.Rect(
                        # X on screen pos
                        self.config.SEAT_DIMENSIONS[1] * self.config.SCALE +
                        current_row_number * \
                        self.config.SEAT_DIMENSIONS[1] * self.config.SCALE,
                        self.config.HEIGHT - ((seat_within_row_number + 2)              # Y on screen pos
                                              * self.config.SEAT_DIMENSIONS[0] * self.config.SCALE),
                        # Width
                        self.config.SEAT_DIMENSIONS[1] * self.config.SCALE,
                        self.config.SEAT_DIMENSIONS[0] * self.config.SCALE)                         # Height
                    if seat == 'E' or seat == 'S':
                        pygame.draw.rect(WINDOW, (255, 0, 0) if seat == 'E' else (
                            255, 255, 255), seat_rect, 2)
                    elif seat == '#':
                        pygame.draw.rect(WINDOW, (255, 255, 255), seat_rect)
                seat_within_row_number += 1
            current_row_number += 1
        
    def fully_boarded(self) -> bool:
        for passenger in self.passengers:
            if passenger.pos.x in self.config.AISLE_SEATS:
                return False

        return True
