from glob import glob
from pickle import NONE
from random import randint
from pygame import Vector2
from config import *
import pygame
from passengers import Passenger

passengers: list[list[None | Passenger]] = [
    [None for i in range(len(SEATS[0]))] for i in range(len(SEATS))]

passengers[int(STARTING_POSITION.x)][int(STARTING_POSITION.y)] = Passenger(Vector2(randint(0, len(SEATS[0]) - 1), randint(0, ROW_COUNT - 1)))


def drawAndUpdatePassengers(WINDOW: pygame.Surface) -> None:
    global passengers
    min_seat_dimensions_scaled = min(
        SEAT_DIMENSIONS[0], SEAT_DIMENSIONS[1]) * SCALE * 0.5
    current_row_number = 0  # 0 is row 1, 1 is row 2 etc
    new_passenger_positions = [row[:] for row in passengers]
    for row in passengers:
        person_within_row_number = 0
        for person in row:
            if person != None:
                person_circle_centre = Vector2(
                    SEAT_DIMENSIONS[1] * SCALE + min_seat_dimensions_scaled +
                    current_row_number * SEAT_DIMENSIONS[1] * SCALE,
                    HEIGHT - ((person_within_row_number + 2)
                            * SEAT_DIMENSIONS[0] * SCALE - min_seat_dimensions_scaled),
                )
                pygame.draw.circle(WINDOW, (0, 255, 0),
                                person_circle_centre, min_seat_dimensions_scaled)
                person_update_info = person.update(passengers, pygame.Vector2(person_within_row_number, current_row_number))
                if person_update_info != None:
                    if person_update_info == 'Done':
                        new_passenger_positions[current_row_number][person_within_row_number] = None
                        new_passenger_positions[int(STARTING_POSITION.x)][int(STARTING_POSITION.y)] = Passenger(Vector2(randint(0, len(SEATS[0]) - 1), randint(0, ROW_COUNT - 1)))
                    else:
                        new_passenger_positions[int(person_update_info.y)][int(person_update_info.x)] = passengers[current_row_number][person_within_row_number]
                        new_passenger_positions[current_row_number][person_within_row_number] = None
            person_within_row_number += 1
        current_row_number += 1
    passengers = new_passenger_positions


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