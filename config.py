# Types:
#   E | Emergency Escape row
#   S | Normal Seat
#   _ | Walkable row
#   # | Blocked off area

from pygame import Vector2


ROW_FORMAT: list[list[str, int]] = [
    ("###_###", 1),  # NON SEATS
    ("EEE_###", 1),  # First row
    ("SSS_EEE", 1),  # Second row
    ("SSS_SSS", 13),  # Next 13 rows
    ("EEE_EEE", 1),  # Escape row
    ("SSS_SSS", 16),  # Next 16 rows
    ("###_###", 1),  # NON SEATS
]

AISLE_SEATS = []

for idx, val in enumerate(ROW_FORMAT[0][0]):
    if val == '_':
        AISLE_SEATS.append(idx)

print(AISLE_SEATS)


SEATS: list[str] = []

for row_type, amt in ROW_FORMAT:
    for i in range(amt):
        SEATS.append(row_type)

ROW_COUNT = 0
for row in ROW_FORMAT:
    ROW_COUNT += row[1]

SCALE = 0.5

SEAT_DIMENSIONS = [100, 100]  # cm of each, [Width, Depth]

MAX_MOVEMENT_SPEED = 100000  # cm / s

STARTING_POSITION = Vector2(3, -1)

BAGGAGE_WAITING_TIME = 20

# Dimensions of the screen accounting for a margin of one seat
WIDTH, HEIGHT = (ROW_COUNT + 2) * SEAT_DIMENSIONS[0] * SCALE, (len(
    ROW_FORMAT[0][0]) + 2) * SEAT_DIMENSIONS[1] * SCALE

MIN_SEAT_DIM_SCALED = min(
    SEAT_DIMENSIONS[0], SEAT_DIMENSIONS[1]) * SCALE * 0.5

hold_ups = 0