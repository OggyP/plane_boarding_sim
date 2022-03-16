from pickle import NONE
from pygame import Vector2
from config import *
import pygame
from passengers import Passenger

passengers: list[list[None | Passenger]] = [
    [None for i in range(len(SEATS[0]))] for i in range(len(SEATS))]

passengers[0][3] = Passenger(Vector2(4, 4))


def drawAndUpdatePassengers(WINDOW: pygame.Surface) -> None:
    min_seat_dimensions_scaled = min(
        SEAT_DIMENSIONS[0], SEAT_DIMENSIONS[1]) * SCALE * 0.5
    current_row_number = 0  # 0 is row 1, 1 is row 2 etc
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
                person.update(passengers, pygame.Vector2(person_within_row_number, current_row_number))
            person_within_row_number += 1
        current_row_number += 1
