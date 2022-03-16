from pygame.math import Vector2
from config import MAX_MOVEMENT_SPEED

class Passenger():
    def __init__(self, endingPos: Vector2) -> None:
        self.endine_seat: Vector2 = endingPos
        self.movecooldown = 0
    
    def update(self, passengers: list[list[any]], own_position: Vector2):
        difference_in_pos = self.endine_seat - own_position
        if difference_in_pos.y == 0:
            pass
        else:
            direction_to_seat = int(difference_in_pos.y / abs(difference_in_pos.y))
            new_pos = own_position
            new_pos.y += direction_to_seat
            print(new_pos)
            if passengers[int(new_pos.x)][int(new_pos.y)] == None:
                passengers[int(new_pos.x)][int(new_pos.y)] = self
                passengers[int(own_position.x)][int(own_position.y)] = None