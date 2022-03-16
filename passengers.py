import pygame
from pygame.math import Vector2
from config import MAX_MOVEMENT_SPEED

class Passenger():
    def __init__(self, endingPos: Vector2) -> None:
        print(endingPos)
        self.endine_seat: Vector2 = endingPos
        self.movecooldown = 0
        self.at_seat = False
    
    def update(self, passengers: list[list[any]], own_position: Vector2):
        if self.at_seat:
            return None
        difference_in_pos = self.endine_seat - own_position
        if difference_in_pos.y == 0:
            if difference_in_pos.x == 0:
                self.at_seat = True
                return "Done"
            direction_to_seat = int(difference_in_pos.x / abs(difference_in_pos.x))
            new_pos = own_position
            new_pos.x += direction_to_seat
            print(new_pos)
            if passengers[int(new_pos.y)][int(new_pos.x)] == None:
                return new_pos
        else:
            direction_to_seat = int(difference_in_pos.y / abs(difference_in_pos.y))
            new_pos = own_position
            new_pos.y += direction_to_seat
            print(new_pos)
            if passengers[int(new_pos.y)][int(new_pos.x)] == None:
                return new_pos
        return None