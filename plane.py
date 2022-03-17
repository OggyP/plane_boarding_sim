from audioop import reverse
from random import randint, choice
from pygame import Vector2
from config import *
import pygame
from passengers import Passenger

passengers: list[Passenger] = []

seat_choices: list[Vector2] = []

position: Vector2 = Vector2(0, 0)
for row in SEATS:
    for area in row:
        if area == 'E' or area == 'S':
            seat_choices.append(Vector2(position.x, position.y))
        position.x += 1
    position.x = 0
    position.y += 1


def get_passengers(position: Vector2):
    for passenger in passengers:
        if int(passenger.position.x) == int(position.x) and int(passenger.position.y) == int(position.y):
            return passenger

    return None


def draw_and_update_passengers(WINDOW: pygame.Surface) -> None:
    global passengers
    min_seat_dimensions_scaled = min(
        SEAT_DIMENSIONS[0], SEAT_DIMENSIONS[1]) * SCALE * 0.5
    new_passenger_positions = [row[:] for row in passengers]

    for passenger in passengers:
        person_circle_centre = Vector2(
            SEAT_DIMENSIONS[1] * SCALE + min_seat_dimensions_scaled +
            passenger.position.y * SEAT_DIMENSIONS[1] * SCALE,
            HEIGHT - ((passenger.position.x + 2)
                      * SEAT_DIMENSIONS[0] * SCALE - min_seat_dimensions_scaled),
        )
        pygame.draw.circle(WINDOW, (0, 255, 0),
                           person_circle_centre, min_seat_dimensions_scaled)
        if passenger.skip:
            passenger.skip = False
            continue
        person_update_info = passenger.update(passengers)
        if person_update_info != None:
            if isinstance(person_update_info, list):
                for update_info in person_update_info:
                    get_passengers(update_info[0]).go_to = update_info[1]
            elif person_update_info == 'Done':
                pass
                # new_passenger_positions[current_row_number][person_within_row_number] = None
                # new_passenger_positions[int(STARTING_POSITION.x)][int(STARTING_POSITION.y)] = Passenger(
                #     Vector2(randint(0, len(SEATS[0]) - 1), randint(0, ROW_COUNT - 1)))
            elif person_update_info == 'Moved':
                passengers.append(passengers.pop(
                    passengers.index(passenger)))
                passenger.skip = True
            else:
                new_passenger_positions[int(person_update_info.y)][int(
                    person_update_info.x)] = passengers[current_row_number][person_within_row_number]
                new_passenger_positions[current_row_number][person_within_row_number] = None
    for update_info in cv:
        new_passenger_positions[int(update_info[0].y)][int(
            update_info[0].x)].go_to = update_info[1]
    passengers = new_passenger_positions


def attempt_to_create_passenger():
    if passengers[int(STARTING_POSITION.x)][int(STARTING_POSITION.y)] == None:
        ending_pos = choice(seat_choices)
        seat_choices.remove(ending_pos)
        passengers[int(STARTING_POSITION.x)][int(
            STARTING_POSITION.y)] = Passenger(choice(seat_choices))


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


attempt_to_create_passenger()
