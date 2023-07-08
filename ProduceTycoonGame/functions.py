import pygame

# import vectors
from ProduceTycoonGame.vectors import Vector

def inputMovement(pos: Vector) -> Vector:
    keys = pygame.key.get_pressed()
    # Each key moves the tileMap the oposite direction that we want our character to move.
    # Scroll left
    if keys[pygame.K_a]:
        pos.x += 20
    # Scroll right
    if keys[pygame.K_d]:
        pos.x -= 20
    # Scroll down
    if keys[pygame.K_w]:
        pos.y += 20
    # Scroll Up
    if keys[pygame.K_s]:
        pos.y -= 20
    
    # get relative mouse position
    relMousePos = pygame.mouse.get_rel()
    # get mouse buttons
    mouseButtons = pygame.mouse.get_pressed()
    # if left mouse button is pressed
    if mouseButtons[0]:
        # scroll tileMap
        pos.x += relMousePos[0]
        pos.y += relMousePos[1]

    # after all movement has been checked returns updated x and y positions
    return pos.copy()

# def changeTile(guest, movement):
#     # move left
#     if movement == "left":
#         return guest.tileMap.getTileLeft(guest.tile.id)
#     # move right
#     if movement == "right":
#         return guest.tileMap.getTileRight(guest.tile.id)
#     # move up
#     if movement == "up":
#         return guest.tileMap.getTileUp(guest.tile.id)
#     # move down
#     if movement == "down":
#         return guest.tileMap.getTileDown(guest.tile.id)

#     # returns the current tile if movement equals anything else
#     return guest.tile

# def newPath(guest, tileID: int, targetTile: int, append):
#     self.guest = guest
#     self.tileID = tileID
#     self.targetTile = targetTile
#     self.append = append
#     self.movements = [[]]

    

#     if guest.tileMap.getTile(tileID).type == guest.Type.BOUNDARY:
#         return []

#     if tileID == targetID:
#         return self.movements

    
