from pygame.math import Vector2
import pygame
from config import *


class Passenger():
    def __init__(self, current_position: Vector2, endingPos: Vector2) -> None:
        print(current_position)
        self.ending_seat: Vector2 = Vector2(endingPos)
        self.waiting_for_seat_shuffle = False
        self.at_seat = False
        self.go_to: Vector2 | None = None
        self.colour = (63 + round(192 * endingPos.x / (len(SEATS[0]) - 1)), 63 + round(
            192 * endingPos.y / (len(SEATS) - 1)), 63 + round(192 * endingPos.y / (len(SEATS) - 1)))
        self.pos: Vector2 = Vector2(current_position)
        self.skip = False

    def render(self, WINDOW: pygame.surface.Surface):
        person_circle_centre = Vector2(
            SEAT_DIMENSIONS[1] * SCALE + MIN_SEAT_DIM_SCALED +
            self.pos.y * SEAT_DIMENSIONS[1] * SCALE,
            HEIGHT - ((self.pos.x + 2)
                      * SEAT_DIMENSIONS[0] * SCALE - MIN_SEAT_DIM_SCALED),
        )
        pygame.draw.circle(WINDOW, self.colour,
                           person_circle_centre, MIN_SEAT_DIM_SCALED)

        person_line_end = Vector2(
            SEAT_DIMENSIONS[1] * SCALE + MIN_SEAT_DIM_SCALED +
            self.ending_seat.y * SEAT_DIMENSIONS[1] * SCALE,
            HEIGHT - ((self.ending_seat.x + 2)
                      * SEAT_DIMENSIONS[0] * SCALE - MIN_SEAT_DIM_SCALED),
        )
        pygame.draw.line(WINDOW, self.colour,
                         person_circle_centre, person_line_end, 2)

    def update(self, passengers: list[list[any]]):
        if self.skip:
            self.skip = False
            return "Moved"
        if self.at_seat and self.go_to is None:
            self.skip = False
        difference_in_pos = (
            self.ending_seat if self.go_to is None else self.go_to) - self.pos
        if self.go_to is None:
            # Go to seat
            if difference_in_pos.y == 0:
                if difference_in_pos.x == 0:
                    self.at_seat = True
                    return "Done"
                direction_to_seat = int(
                    difference_in_pos.x / abs(difference_in_pos.x))
                new_pos = Vector2(self.pos)
                new_pos.x += direction_to_seat
                if get_passengers(new_pos) == None:
                    self.pos = new_pos
                    return None
            else:
                if difference_in_pos.y == 1:
                    direction_to_seat_x = int(
                        difference_in_pos.x / abs(difference_in_pos.x))
                    check_for_people_pos = Vector2(
                        self.pos.x + direction_to_seat_x, self.ending_seat.y)

                    detected_people: list[Vector2] = []
                    while (direction_to_seat_x > 0 and check_for_people_pos.x < self.ending_seat.x) or (direction_to_seat_x < 0 and check_for_people_pos.x > self.ending_seat.x):
                        possible_passenger = get_passengers(check_for_people_pos)
                        if possible_passenger is not None:
                            if possible_passenger.at_seat == False:
                                return None
                            detected_people.append(
                                Vector2(check_for_people_pos))
                        check_for_people_pos.x += direction_to_seat_x

                    if len(detected_people) > 0:
                        detected_people_updates: list[passengers] = []
                        detection_num = 0
                        for detection in detected_people:
                            detected_people_updates.append([Vector2(detection), Vector2(
                                self.pos.x, self.pos.y + 1 + len(detected_people) - detection_num)])
                            detection_num += 1
                        if self.waiting_for_seat_shuffle:
                            return None
                        self.waiting_for_seat_shuffle = True
                        return detected_people_updates
                if not self.ending_seat.y < self.pos.y:
                    for i in range(4):
                        check_pos = Vector2(self.pos)
                        check_pos.y += i
                        check_passenger = get_passengers(check_pos)
                        if check_passenger is not None and check_passenger.ending_seat.y < check_passenger.pos.y:
                            if check_passenger.ending_seat.y == self.ending_seat.y and (difference_in_pos.y == 1 or difference_in_pos.y == 0) :
                                continue
                            else:
                                return None

                direction_to_seat = int(
                    difference_in_pos.y / abs(difference_in_pos.y))
                new_pos = Vector2(self.pos)
                new_pos.y += direction_to_seat
                if get_passengers(new_pos) == None:
                    self.pos = new_pos
                    return None
        else:
            if difference_in_pos.x == 0:
                if difference_in_pos.y == 0:
                    self.at_seat = False
                    self.skip = True
                    self.go_to = None
                    return "Moved"
                direction_to_seat = int(
                    difference_in_pos.y / abs(difference_in_pos.y))
                new_pos = Vector2(self.pos)
                new_pos.y += direction_to_seat
                if get_passengers(new_pos) == None and get_passengers(self.go_to) == None:
                    self.pos = new_pos
                    return None
            else:
                direction_to_seat = int(
                    difference_in_pos.x / abs(difference_in_pos.x))
                new_pos = Vector2(self.pos)
                new_pos.x += direction_to_seat
                if get_passengers(new_pos) == None and get_passengers(self.go_to) == None:
                    self.pos = new_pos
                    return None
            return None


passengers: list[Passenger] = []


def get_passengers(position: Vector2):
    for passenger in passengers:
        if int(passenger.pos.x) == int(position.x) and int(passenger.pos.y) == int(position.y):
            return passenger

    return None
