import pygame

from ProduceTycoonGame.vectors import Vector
from ProduceTycoonGame.tile import Tile, Type


class TileMap():
    def __init__(self, screen: pygame.Surface, pos: Vector):
        self.screen = screen
        self.pos = pos
        self.mov = Vector(0, 0)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.zoom = self.screen.get_width()

        self.rows = self.screen.get_height() // 25
        self.col = self.screen.get_width() // 25
        self.tileMapStartingPos = self.pos.copy()
        
        # create the grid of tiles
        self.tileMapGrid = self.createTileGrid(self.zoom, self.rows, self.col, self.tileMapStartingPos) 

        # creates rectangle size of screen for border
        self.rect = pygame.Rect((0, 0), (self.width, self.height))

        # highlighted tile
        self.highlightedTile = None

        # selected tile
        self.selectedTile = None

    def createTileGrid(self, zoom: int, numRows: int, numCols: int, tileMapStartingPos: Vector):
        # create grid of tiles
        tileSize = zoom // numCols

        tileMapGrid: list[Tile] = []
        for i in range(numRows):
            for j in range(numCols):
                pos = Vector(tileMapStartingPos.x + j * tileSize,
                               tileMapStartingPos.x + i * tileSize)
                if i == 0 or j == 0 or i == numRows-1 or j == numCols-1:
                    tileMapGrid.append(Tile(self.screen, pos, tileSize, Type.BOUNDARY))
                elif (i + j) % 2 == 0:
                    tileMapGrid.append(Tile(self.screen, pos, tileSize, Type.INTERACTABLE))
                else:
                    tileMapGrid.append(Tile(self.screen, pos, tileSize, Type.WALKABLE))

        return tileMapGrid

    def events(self, mouseClicked: bool = False):
        # checking if mouse is hovering over tile
        self.highlightedTile = None
        for tile in self.tileMapGrid:
            tile.isHighlighted = False
            if tile.rect.collidepoint(pygame.mouse.get_pos()):
                self.highlightedTile = tile
                tile.isHighlighted = True
                if mouseClicked:
                    if self.selectedTile is not None:
                        # deselecting selected tile
                        self.selectedTile.isSelected = False
                    if self.selectedTile == tile:
                        # deselecting tile
                        tile.isSelected = False
                        self.selectedTile = None
                    else:
                        # selecting tile
                        self.selectedTile = tile
                        self.selectedTile.isSelected = True

    def update(self):
        for tile in self.tileMapGrid:
            tile.update()

        # updating position of tileMap
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def draw(self):
        # drawing tileMap
        for tile in self.tileMapGrid:
            tile.draw()

        # draws border
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)
        

    def getTileByID(self, tileID: int):
        for tile in self.tileMapGrid:
            if tile.id == tileID:
                return tile
    
    def getTileByPos(self, pos: Vector):
        for tile in self.tileMapGrid:
            # if pos collides with tile rect
            if tile.rect.collidepoint(pos.x, pos.y):
                return tile

    # returns the neighbors of a tile
    def getNeighbors(self, tile: Tile) -> list[Tile]:
        neighbors: list[Tile] = []

        # get the tiles that collide with the tile
        for tile2 in self.tileMapGrid:
            if tile.rect.colliderect(tile2.rect):
                neighbors.append(tile2)
        
        # get the tiles that are adjacent to the tile
        for tile2 in self.tileMapGrid:
            if tile2.rect.collidepoint(tile.pos.x + tile.size, tile.pos.y):
                neighbors.append(tile2)
            elif tile2.rect.collidepoint(tile.pos.x - tile.size, tile.pos.y):
                neighbors.append(tile2)
            elif tile2.rect.collidepoint(tile.pos.x, tile.pos.y + tile.size):
                neighbors.append(tile2)
            elif tile2.rect.collidepoint(tile.pos.x, tile.pos.y - tile.size):
                neighbors.append(tile2)
        
        # get the tiles that are diagonal to the tile
        for tile2 in self.tileMapGrid:
            if tile2.rect.collidepoint(tile.pos.x + tile.size, tile.pos.y + tile.size):
                neighbors.append(tile2)
            elif tile2.rect.collidepoint(tile.pos.x - tile.size, tile.pos.y + tile.size):
                neighbors.append(tile2)
            elif tile2.rect.collidepoint(tile.pos.x + tile.size, tile.pos.y - tile.size):
                neighbors.append(tile2)
            elif tile2.rect.collidepoint(tile.pos.x - tile.size, tile.pos.y - tile.size):
                neighbors.append(tile2)

        # remove the orignal tile from the neighbors list
        if tile in neighbors:
            neighbors.remove(tile)

        return neighbors

        # get walkable tiles
    def getWalkableTiles(self) -> list[Tile]:
        walkableTiles: list[Tile] = []
        for tile in self.tileMapGrid:
            if tile.type == Type.WALKABLE:
                walkableTiles.append(tile)
        return walkableTiles
