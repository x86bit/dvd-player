import pygame, time
from pygame.locals import *
pygame.init()
display = pygame.display.set_mode((900, 600))
dvd = pygame.image.load("dvd.png")
dvd = pygame.transform.scale(dvd, (200, 87))
global dvdX, dvdY, dvdTEdge, dvdBEdge, dvdLEdge, dvdREdge, direction
dvdX = 50
direction = "rd"
dvdY = 50
dvdTEdge = pygame.Rect(dvdX, (dvdY - 2), 200, 1)
dvdBEdge = pygame.Rect(dvdX, (dvdY + 88), 200, 1)
dvdLEdge = pygame.Rect((dvdX - 2), dvdY, 1, 87)
dvdREdge = pygame.Rect((dvdX + 201), dvdY, 1, 87)
dvdRect = pygame.Rect(dvdX, dvdY, 200, 87)
baseRect = pygame.Rect(10, 10, 880, 580)
crashed = False
def checkCollsions():
    global direction
    if not baseRect.colliderect(dvdBEdge):
        if direction == "rd":
            direction = "ru"
        if direction == "ld":
            direction = "lu"
    if not baseRect.colliderect(dvdREdge):
        if direction == "ru":
            direction = "lu"
        if direction == "rd":
            direction = "ld"
    if not baseRect.colliderect(dvdTEdge):
        if direction == "lu":
            direction = "ld"
        if direction == "ru":
            direction = "rd"
    if not baseRect.colliderect(dvdLEdge):
        if direction == "ld":
            direction = "rd"
        if direction == "lu":
            direction = "ru"
def updateRects():
    global dvdTEdge, dvdBEdge, dvdLEdge, dvdREdge
    dvdTEdge = pygame.Rect(dvdX, (dvdY - 2), 200, 1)
    dvdBEdge = pygame.Rect(dvdX, (dvdY + 88), 200, 1)
    dvdLEdge = pygame.Rect((dvdX - 2), dvdY, 1, 87)
    dvdREdge = pygame.Rect((dvdX + 201), dvdY, 1, 87)
    dvdRect = pygame.Rect(dvdX, dvdY, 200, 87)
    baseRect = pygame.Rect(10, 10, 880, 580)
def moveDirection():
    global dvdX, dvdY, direction
    if direction == "rd":
        dvdX += 1
        dvdY += 1
    if direction == "ru":
        dvdX += 1
        dvdY -= 1
    if direction == "ld":
        dvdX -= 1
        dvdY += 1
    if direction == "lu":
        dvdX -= 1
        dvdY -= 1
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
    checkCollsions()
    moveDirection()
    updateRects()
    display.fill((255, 255, 255))
    pygame.draw.rect(display, (0, 0, 0), baseRect)
    display.blit(dvd, (dvdX, dvdY))
    #pygame.draw.rect(display, (255, 0, 0), dvdTEdge)
    #pygame.draw.rect(display, (255, 0, 0), dvdBEdge)
    #pygame.draw.rect(display, (255, 0, 0), dvdLEdge)
    #pygame.draw.rect(display, (255, 0, 0), dvdREdge)
    pygame.display.flip()
    time.sleep(.001)
