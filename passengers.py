from pygame.math import Vector2
from config import MAX_MOVEMENT_SPEED, SEATS


class Passenger():
    def __init__(self, current_position: Vector2, endingPos: Vector2) -> None:
        print(current_position)
        self.ending_seat: Vector2 = Vector2(endingPos)
        self.waiting_for_seat_shuffle = False
        self.at_seat = False
        self.go_to: Vector2 | None = None
        self.colour = (63 + round(192 * endingPos.x / (len(SEATS[0]) - 1)), 63 + round(192 * endingPos.y / (len(SEATS) - 1)), 63 + round(192 * endingPos.y / (len(SEATS) - 1)))
        self.pos: Vector2  = Vector2(current_position)
        self.skip = False

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
                    check_for_people_pos = Vector2(
                        self.pos.x, self.ending_seat.y)
                    direction_to_seat_x = int(
                        difference_in_pos.x / abs(difference_in_pos.x))
                    detected_people: list[passengers] = []
                    while (direction_to_seat_x > 0 and check_for_people_pos.x < self.ending_seat.x) or (direction_to_seat_x < 0 and check_for_people_pos.x > self.ending_seat.x):
                        if get_passengers(check_for_people_pos) is not None:
                            detected_people.append([Vector2(check_for_people_pos.x, check_for_people_pos.y), Vector2(
                                self.pos.x, self.pos.y + 2 + len(detected_people))])
                        check_for_people_pos.x += direction_to_seat_x

                    if len(detected_people) > 0:
                        if self.waiting_for_seat_shuffle:
                            return None
                        self.waiting_for_seat_shuffle = True
                        return detected_people
                direction_to_seat = int(
                    difference_in_pos.y / abs(difference_in_pos.y))
                new_pos = Vector2(self.pos)
                new_pos.y += direction_to_seat
                if get_passengers(new_pos) == None:
                    self.pos = new_pos
                    return None
        else:
            # Get out of seat
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
                if get_passengers(new_pos) == None:
                    self.pos = new_pos
                    return None
            else:
                direction_to_seat = int(
                    difference_in_pos.x / abs(difference_in_pos.x))
                new_pos = Vector2(self.pos)
                new_pos.x += direction_to_seat
                if get_passengers(new_pos) == None:
                    self.pos = new_pos
                    return None
            return None


passengers: list[Passenger] = []


def get_passengers(position: Vector2):
    for passenger in passengers:
        if int(passenger.pos.x) == int(position.x) and int(passenger.pos.y) == int(position.y):
            return passenger

    return None
