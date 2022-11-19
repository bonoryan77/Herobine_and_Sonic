#기본이 되는 모듈을 불러오는 코드 입니다.
import time
import pygame, sys
from pygame.locals import *
pygame.init()


#함수들 입니다.


#화면의 크기를 지정하는 코드 입니다.
width = 1000
height = 700
screen = pygame.display.set_mode((width,height))

#중력을 선언하는 코드 입니다.
g = 0

#기본적인 이미지들을 선언하는 코드 입니다.
bgimage = pygame.image.load('그린힐존.png')
bgimage = pygame.transform.scale(bgimage,(1000,700))
img1 = pygame.image.load('소닉_가만히 있을 때 또는 걸을때.png')
img1 = pygame.transform.scale(img1, (80,80))
ringimg = pygame.image.load('소닉_링.png')
ringimg = pygame.transform.scale(ringimg,(10,10))
herobine = pygame.image.load('히로빈비리빈빈빈.png')
herobine = pygame.transform.scale(herobine,(100,100))
#왼쪽으로 움직이는 등장인물의 이미지가 바뀌게 하는 코드 입니다.
img2 = pygame.transform.flip(img1,True,False)
img2 = pygame.transform.scale(img2,(80,80))
img = img2
#등장인물의 Rect 객체를 선언하는 코드 입니다.
rect1 = pygame.Rect(890,330,80,80)
rectto = pygame.Rect(241,241,125,145)
bottomrect = pygame.Rect(0,430,1000,10)
#체력과 데미지를 선언하는 코드입니다.
hpofsonic = 3
hpofHerobine = 5
attack = 1
damage = 2


#본격적인 게임 실행을 돕는 무한반복문 코드 입니다.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#주인공을 조작하는 코드 입니다.
    keyInput = pygame.key.get_pressed()
    if keyInput[K_LEFT] and rect1.left > 0:
        img = img2
        img = pygame.transform.scale(img,(80,80))
        rect1.left -= 20
    elif keyInput[K_RIGHT] and rect1.right < 1000:
        img = img1
        img = pygame.transform.scale(img,(80,80))
        rect1.right += 20
    if keyInput[K_SPACE] and rect1.top > 0:
        if not pygame.Rect.colliderect(rect1, bottomrect):
            g = -10
            rect1.move_ip(0,g)
        else:
            while pygame.Rect.colliderect(rect1, bottomrect):
                g = 10
                break
        rect1.move_ip(0,g)
            
#프레임을 조정하는 코드 입니다.
    CLOCK = pygame.time.Clock()
    CLOCK.tick(100)
#화면에 이미지들을 띄우는 코드 입니다.
    screen.blit(bgimage,(0,0))
    screen.blit(img,(rect1))
    pygame.display.update()