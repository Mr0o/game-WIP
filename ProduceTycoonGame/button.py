import pygame

from ProduceTycoonGame.vectors import Vector

class Button():
    def __init__(self, screen: pygame.Surface, pos: Vector, text = "3x3"):
        self.screen = screen
        self.pos = pos
        self.text = text

        self.width = 21
        self.height = 20
        self.color = (0, 0, 255)
        self.showRect = False

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.interactableRect = pygame.Rect(0, 0, self.screen.get_height() // 25 * 3, self.screen.get_height() // 25 * 3)
        
    
    def events(self, mouseClicked: bool):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and mouseClicked:
            self.color = (0, 123, 255)
            self.showRect = True
        else:
            self.color = (0, 0, 255)

    def update(self):
        self.interactableRect.center = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def draw(self):

        objectSize = pygame.font.SysFont('Arial', 15, bold=True)
        text = objectSize.render(self.text, True, (0, 0, 0))

        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(text, (self.pos.x, self.pos.y))

        if self.showRect:
            pygame.draw.rect(self.screen, self.color, self.interactableRect)