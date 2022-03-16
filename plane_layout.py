import pygame
from config import *


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
