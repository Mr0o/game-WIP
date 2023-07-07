import pygame

from ProduceTycoonGame.functions import inputMovement
from ProduceTycoonGame.tile import Tile, Type

class TileMap():
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_mov = 0
        self.y_mov = 0

        # create grid of tiles
        self.rows = screen.get_height() // 50
        self.col = screen.get_width() // 50
        self.tileMap_grid: list[list[Tile]] = []
        self.tileMap_starting_pos = 0
        self.tile_size = screen.get_width() // self.col
        for i in range(self.rows):
            col: list[Tile] = []
            for j in range(self.col):
                if i == 0 or j == 0 or i == self.rows-1 or j == self.col-1:
                    col.append(Tile(self.screen, self.tileMap_starting_pos + j * self.tile_size, self.tileMap_starting_pos + i * self.tile_size, self.tile_size, Type.BOUNDARY))
                elif (i + j) % 2 == 0:
                    col.append(Tile(self.screen, self.tileMap_starting_pos + j * self.tile_size, self.tileMap_starting_pos + i * self.tile_size, self.tile_size, Type.INTERACTABLE))
                else:
                    col.append(Tile(self.screen, self.tileMap_starting_pos + j * self.tile_size, self.tileMap_starting_pos + i * self.tile_size, self.tile_size, Type.WALKABLE))
            self.tileMap_grid.append(col)

        # creates rectangle size of screen for border
        self.rect = pygame.Rect((0, 0), (self.screen.get_width(), self.screen.get_height()))

    def events(self):
        # changing the x and y positions
        self.x_mov, self.y_mov = inputMovement(self.x, self.y)

        # checking if mouse is hovering over tile
        for i in range(self.rows):
            for j in range(self.col):
                if self.tileMap_grid[i][j].rect.collidepoint(pygame.mouse.get_pos()):
                    self.tileMap_grid[i][j].isHighlighted = True
                else:
                    self.tileMap_grid[i][j].isHighlighted = False

    def update(self):
        for i in range(self.rows):
            for j in range(self.col):
                # updates each tiles x and y positions
                self.tileMap_grid[i][j].update(self.x_mov, self.y_mov)
        #updating borders x and y positions
        self.rect.x += self.x_mov 
        self.rect.y += self.y_mov

    def draw(self):
        # drawing tileMap
        for i in range(self.rows):
            for j in range(self.col):
                self.tileMap_grid[i][j].draw()
        # draws border
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)

        

