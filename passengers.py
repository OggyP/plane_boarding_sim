from pygame.math import Vector2
from config import MAX_MOVEMENT_SPEED, SEATS


class Passenger():
    def __init__(self, current_position, endingPos: Vector2) -> None:
        print(endingPos)
        self.ending_seat: Vector2 = endingPos
        self.waiting_for_seat_shuffle = False
        self.at_seat = False
        self.move_out_of_way: False | int = False
        self.go_to: Vector2 | None = None
        self.colour = (endingPos)
        self.position = current_position
        self.skip = False

    def update(self, passengers: list[list[any]]):
        if self.at_seat and self.go_to is None:
            return None
        difference_in_pos = (
            self.ending_seat if self.go_to is None else self.go_to) - self.position
        if self.go_to is None:
            # Go to seat
            if difference_in_pos.y == 0:
                if difference_in_pos.x == 0:
                    self.at_seat = True
                    return "Done"
                direction_to_seat = int(
                    difference_in_pos.x / abs(difference_in_pos.x))
                new_pos = self.position
                new_pos.x += direction_to_seat
                if passengers[int(new_pos.y)][int(new_pos.x)] == None:
                    return new_pos
            else:
                if difference_in_pos.y == 1:
                    check_for_people_pos = Vector2(
                        self.position.x, self.ending_seat.y)
                    direction_to_seat_x = int(
                        difference_in_pos.x / abs(difference_in_pos.x))
                    detected_people: list[passengers] = []
                    while check_for_people_pos.x >= 0 and check_for_people_pos.x < len(SEATS[int(check_for_people_pos.y)]):
                        if passengers[int(check_for_people_pos.y)][int(check_for_people_pos.x)] is not None:
                            detected_people.append([Vector2(check_for_people_pos.x, check_for_people_pos.y), Vector2(
                                self.position.x, self.position.y + 2 + len(detected_people))])
                        check_for_people_pos.x += direction_to_seat_x

                    if len(detected_people) > 0:
                        if self.waiting_for_seat_shuffle:
                            return None
                        self.waiting_for_seat_shuffle = True
                        return detected_people
                direction_to_seat = int(
                    difference_in_pos.y / abs(difference_in_pos.y))
                new_pos = self.position
                new_pos.y += direction_to_seat
                if passengers[int(new_pos.y)][int(new_pos.x)] == None:
                    return new_pos
        else:
            # Get out of seat
            if difference_in_pos.x == 0:
                if difference_in_pos.y == 0:
                    self.at_seat = False
                    return "Moved"
                direction_to_seat = int(
                    difference_in_pos.y / abs(difference_in_pos.y))
                new_pos = self.position
                new_pos.y += direction_to_seat
                if passengers[int(new_pos.y)][int(new_pos.x)] == None:
                    return new_pos
            else:
                direction_to_seat = int(
                    difference_in_pos.x / abs(difference_in_pos.x))
                new_pos = self.position
                new_pos.x += direction_to_seat
                if passengers[int(new_pos.y)][int(new_pos.x)] == None:
                    return new_pos
            return None
