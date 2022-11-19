#기본이 되는 모듈을 불러오는 코드 입니다.
import pygame, sys
from pygame.locals import *
pygame.init()

#화면의 크기를 지정하는 코드 입니다.
width = 1000
height = 700
screen = pygame.display.set_mode((width,height))

#기본적인 이미지들을 선언하는 코드 입니다.
bgimage = pygame.image.load('그린힐존.png')
bgimage = pygame.transform.scale(bgimage,(1000,700))
img1 = pygame.image.load('소닉_가만히 있을 때 또는 걸을때.png')
img1 = pygame.transform.scale(img1, (40,40))
ringimg = pygame.image.load('소닉_링.png')
ringimg = pygame.transform.scale(ringimg,(10,10))
herobine = pygame.image.load('히로빈비리빈빈빈.png')
herobine = pygame.transform.scale(herobine,(100,100))
#왼쪽으로 움직이는 등장인물의 이미지가 바뀌게 하는 코드 입니다.
img2 = pygame.transform.flip(img1,True,False)
img2 = pygame.transform.scale(img2,(40,40))
#등장인물의 Rect 객체를 선언하는 코드 입니다.
rect1 = pygame.Rect(890,310,40,40)

#본격적인 게임 실행을 돕는 무한반복문 코드 입니다.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#주인공을 조작하는 코드 입니다.
    img = img2
    keyInput = pygame.key.get_pressed()
    if keyInput[K_LEFT] and rect1.left > 0:
        img = img2
        img = pygame.transform.scale(img,(40,40))
        rect1.left -= 3
    elif keyInput[K_RIGHT] and rect1.right < 1000:
        img = img1
        img = pygame.transform.scale(img,(40,40))
        rect1.right += 3
    if keyInput[K_UP] and rect1.top > 0:
        img = img1
        img = pygame.transform.scale(img,(40,40))
        rect1.top -= 3
#화면에 이미지들을 띄우는 코드 입니다.
    screen.blit(bgimage,(0,0))
    screen.blit(img,(rect1))
    pygame.display.update()