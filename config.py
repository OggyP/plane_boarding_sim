# Types:
#   E | Emergency Escape row
#   S | Normal Seat
#   _ | Walkable row
#   # | Blocked off area

from pygame import Vector2


class Sim_Config:
    def __init__(self) -> None:
        self.ROW_FORMAT: list[list[str, int]] = [
            ("###_###", 1),  # NON SEATS
            ("EEE_###", 1),  # First row
            ("SSS_EEE", 1),  # Second row
            ("SSS_SSS", 13),  # Next 13 rows
            ("EEE_EEE", 1),  # Escape row
            ("SSS_SSS", 16),  # Next 16 rows
            ("###_###", 1),  # NON SEATS
        ]

        self.AISLE_SEATS = []

        for idx, val in enumerate(self.ROW_FORMAT[0][0]):
            if val == '_':
                self.AISLE_SEATS.append(idx)

        self.AISLE_SEATS

        self.SEATS: list[str] = []

        for row_type, amt in self.ROW_FORMAT:
            for i in range(amt):
                self.SEATS.append(row_type)

        self.ROW_COUNT = 0
        for row in self.ROW_FORMAT:
            self.ROW_COUNT += row[1]

        self.SCALE = 0.5

        self.SEAT_DIMENSIONS = [100, 100]  # cm of each, [Width, Depth]

        self.MAX_MOVEMENT_SPEED = 100000  # cm / s

        self.STARTING_POSITION = Vector2(3, -1)

        self.BAGGAGE_WAITING_TIME = 12

        # Dimensions of the screen accounting for a margin of one seat
        self.WIDTH, self.HEIGHT = (self.ROW_COUNT + 2) * self.SEAT_DIMENSIONS[0] * self.SCALE, (len(
            self.ROW_FORMAT[0][0]) + 2) * self.SEAT_DIMENSIONS[1] * self.SCALE

        self.MIN_SEAT_DIM_SCALED = min(
            self.SEAT_DIMENSIONS[0], self.SEAT_DIMENSIONS[1]) * self.SCALE * 0.5

        self.SECTIONS = 3

        self.hold_ups = 0
