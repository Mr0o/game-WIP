import pygame
import pymunk

from ProduceTycoonGame.vectors import Vector
from ProduceTycoonGame.person import Person

# global
id = 0

class Guest(Person):
    def __init__(self, screen: pygame.Surface, space: pymunk.Space, pos: Vector, name: str = "Guest"):
        global id; id += 1
        super().__init__(screen, space, pos, id, name)

    # draw
    def draw(self):
        super().draw()
        
        # debugging stuff (Will be removed later)
        # load font
        debugFont = pygame.font.SysFont('Arial', 15, bold=True)
        # draw name
        nameText = debugFont.render(self.name, True, (0, 70, 0))
        self.screen.blit(nameText, (self.pos.x, self.pos.y - nameText.get_height()))