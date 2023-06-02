import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Sham Game")

walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'), pygame.image.load('right_3.png'),
pygame.image.load('right_4.png'), pygame.image.load('right_5.png'),
pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
pygame.image.load('left_4.png'), pygame.image.load('left_5.png'),
pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()
x = 50
y = 425
widht = 46
height = 56
speed = 5

isJump = False
jumpCout = 10

left = False
right =False
animCount = 0
lastMove = "right"

class  snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y,), self.radius)

def drawWindow():
    global animCount
    win.blit(bg, (0, 0)) 
    
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount +=1

    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount +=1

    else:
        win.blit(playerStand, (x, y))    
    
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if  lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(snaryad(round(x + widht // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - widht - 5:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCout>=-10:
            if jumpCout < 0:
                y += (jumpCout **2 )/2
            else:
                y -= (jumpCout **2)/2
            jumpCout -=1
        else:
            isJump = False
            jumpCout =  10
    
    drawWindow()
    

pygame.quit()