import pygame, sys
pygame.init()  # initiate modules of pygame

def ballUpdate():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX
    ball.y += ballSpeedY
    if ball.bottom >= screenHeight or ball.top <= 0:
        ballSpeedY *= -1
    if ball.colliderect(player) or ball.colliderect(ai):
        ballSpeedX *= -1
    if ball.right<0 or ball.left >= screenWidth:
        reset()

def playerUpdate():
    global playerSpeedY
    player.y += playerSpeedY
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def aiUpdate():
    ai.centery = ball.centery
    if ai.top <= 0:
        ai.top = 0
    if ai.bottom >= screenHeight:
        ai.bottom = screenHeight

def reset():
    ball.center = (screenWidth/2, screenHeight/2)


# initializing variables
screenWidth = 600
screenHeight = 450

ballSpeedX = 8
ballSpeedY = 8
playerSpeedY = 0

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screenWidth, screenHeight))

# creating rects: pygame.Rect(x position,y position width, height)
ball = pygame.Rect(screenWidth/2-15/2, screenHeight/2-15/2, 15, 15)
player = pygame.Rect(0, screenHeight/2-100/2, 10, 100)
ai = pygame.Rect(screenWidth-10, screenHeight/2-100/2, 10, 100)

while True:
    for event in pygame.event.get():  # gets all user inputs and other events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # check if key is being pressed
            if event.key == pygame.K_UP:
                playerSpeedY = -7
            if event.key == pygame.K_DOWN:
                playerSpeedY = 7
        if event.type == pygame.KEYUP:  # check if key is unpressed
            playerSpeedY = 0

    # updating the window
    screen.fill((50,50,50))
    ballUpdate()  # updates the rect's position
    playerUpdate()  # updates player's position
    aiUpdate()  # updates ai's position
    pygame.draw.ellipse(screen,(255,255,255), ball)
    pygame.draw.rect(screen, (255,255,255), player)
    pygame.draw.rect(screen, (255,255,255), ai)
    pygame.display.flip()
    clock.tick(60)  # game runs at 60 fps
