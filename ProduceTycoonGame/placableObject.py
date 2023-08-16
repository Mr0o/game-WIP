import pygame

from ProduceTycoonGame.vectors import Vector
from ProduceTycoonGame.tile import Type
from ProduceTycoonGame.UserInterface.button import Button
from ProduceTycoonGame.UserInterface.placableObjectGUI import PlacableObjectGUI, TypeObject

id = 0

# see if somethings changed if not dont worry about updating
# remove tilemap
# find better way for exit button to coexist
# change events to not return
# getter for pos
#

class PlacableObject():
    def __init__(self, screen: pygame.Surface, pos: Vector, size: int, rows: int = 1, cols: int = 1, elements: list = [], image: str = './Resources/Images/Banana_ProduceTycoon.png'):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.rows = rows
        self.cols = cols
        self.elements = elements

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.rows * self.size, self.cols * self.size))

        self.isPlaced = False
        self.canPlace = True
        self.rect = self.image.get_rect()

        self.exitButton = Button(self.screen, Vector(0, 0), 'X', 20, 20, (255, 0, 0))

        self.gui = PlacableObjectGUI(self.screen, Vector(self.screen.get_width() - 100, 25), 100, 100, (200, 150, 170))

    def checkIfCanPlace(self):
        for element in self.elements:
            if element.rect.colliderect(self.rect):
                self.canPlace = False
                break
            else:
                self.canPlace = True

    def moveToNewPos(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.isPlaced = False
            return self.isPlaced
        return self.isPlaced

    def events(self, previousMouseClick: bool = False, mouseClicked: bool = False, events: list = []):
        if self.isPlaced:
            if mouseClicked and self.rect.collidepoint(pygame.mouse.get_pos()):
                self.gui.hidden = not self.gui.hidden
            self.gui.events(mouseClicked, events)

        self.checkIfCanPlace()

        mousePos = pygame.mouse.get_pos()
        if mousePos[0] % self.size == 1 :
            newPosX = (mousePos[0] - 1)- self.rows * self.size // 2
            self.pos.x = newPosX
        if mousePos[1] % self.size == 0:
            newPosY = mousePos[1] - self.cols * self.size // 2
            self.pos.y = newPosY
            
        # changes tile type to object if rect collides with tile and mouse is clicked
        if self.canPlace and not mouseClicked and previousMouseClick:
            self.isPlaced = True

    def update(self):
        if self.isPlaced:
            self.gui.update()

            match self.gui.type:
                case TypeObject.WATERMELON:
                    self.image = pygame.image.load('./Resources/Images/WatermelonBin.png')
                    print("Watermelon")
                case TypeObject.BANANAS:
                    self.image = pygame.image.load('./Resources/Images/Banana_ProduceTycoon.png')
                    print("Bananas")
                case TypeObject.APPLES:
                    self.image = pygame.image.load('./Resources/Images/Apple_ProduceTycoon.png')
                    print("Apples")
                case TypeObject.TOMATOES:
                    self.image = pygame.image.load('./Resources/Images/Tomato.png')
                    print("Tomatoes")
                case _:
                    self.image = pygame.image.load('./Resources/Images/Banana_ProduceTycoon.png')
            return
        # will figure out later works for now lol
        if self.cols % 2 == 1 and self.rows % 2 == 1:
            self.pos.x += self.size * 3 // 4
            self.pos.y -= 1
        if self.cols % 2 == 1:
            self.pos.y += self.size * 3 / 4 - 1
        elif self.rows % 2 == 1:
            self.pos.x -= 1
            self.pos.x += self.size * 3 / 4
        self.rect.topleft = (self.pos.x, self.pos.y)

    def draw(self):
        if not self.isPlaced:
            self.exitButton.draw()

        self.screen.blit(self.image, self.rect.topleft)

        if not self.gui.hidden:
            self.gui.draw()

    def getPos(self):
        return self.pos

    def getPlaced(self):
        return self.isPlaced
