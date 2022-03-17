from audioop import reverse
from random import randint, choice
from pygame import Vector2
from config import *
import pygame
from passengers import *

seat_choices: list[Vector2] = []

position: Vector2 = Vector2(0, 0)
for row in SEATS:
    for area in row:
        if area == 'E' or area == 'S':
            seat_choices.append(Vector2(position.x, position.y))
        position.x += 1
    position.x = 0
    position.y += 1


def draw_and_update_passengers(WINDOW: pygame.Surface) -> None:
    global passengers
    min_seat_dimensions_scaled = min(
        SEAT_DIMENSIONS[0], SEAT_DIMENSIONS[1]) * SCALE * 0.5

    for passenger in passengers:
        person_circle_centre = Vector2(
            SEAT_DIMENSIONS[1] * SCALE + min_seat_dimensions_scaled +
            passenger.pos.y * SEAT_DIMENSIONS[1] * SCALE,
            HEIGHT - ((passenger.pos.x + 2)
                      * SEAT_DIMENSIONS[0] * SCALE - min_seat_dimensions_scaled),
        )
        pygame.draw.circle(WINDOW, passenger.colour,
                           person_circle_centre, min_seat_dimensions_scaled)
        person_update_info = passenger.update(passengers)
        if person_update_info != None and person_update_info != 'Done':
            if isinstance(person_update_info, list):
                for update_info in person_update_info:
                    get_passengers(update_info[0]).go_to = update_info[1]
            elif person_update_info == 'Done':
                pass
                # new_passenger_positions[current_row_number][person_within_row_number] = None
                # new_passenger_positions[int(STARTING_POSITION.x)][int(STARTING_POSITION.y)] = Passenger(
                #     Vector2(randint(0, len(SEATS[0]) - 1), randint(0, ROW_COUNT - 1)))
            elif person_update_info == 'Moved':
                passengers.insert(0, passengers.pop(
                    passengers.index(passenger)))


def attempt_to_create_passenger():
    if get_passengers(STARTING_POSITION) == None:
        if not len(seat_choices):
            return
        ending_pos = choice(seat_choices)
        seat_choices.remove(ending_pos)
        create_passenger(STARTING_POSITION, ending_pos)

def create_passenger(position: Vector2, ending_position: Vector2):
    passengers.append(Passenger(position, ending_position))

def draw_seats(WINDOW: pygame.Surface):
    current_row_number = 0  # 0 is row 1, 1 is row 2 etc
    for row in SEATS:
        seat_within_row_number = 0
        for seat in row:
            if seat != '_':
                seat_rect = pygame.Rect(
                    # X on screen pos
                    SEAT_DIMENSIONS[1] * SCALE +
                    current_row_number * SEAT_DIMENSIONS[1] * SCALE,
                    HEIGHT - ((seat_within_row_number + 2)              # Y on screen pos
                              * SEAT_DIMENSIONS[0] * SCALE),
                    # Width
                    SEAT_DIMENSIONS[1] * SCALE,
                    SEAT_DIMENSIONS[0] * SCALE)                         # Height
                if seat == 'E' or seat == 'S':
                    pygame.draw.rect(WINDOW, (255, 0, 0) if seat == 'E' else (
                        255, 255, 255), seat_rect, 2)
                elif seat == '#':
                    pygame.draw.rect(WINDOW, (255, 255, 255), seat_rect)
            seat_within_row_number += 1
        current_row_number += 1