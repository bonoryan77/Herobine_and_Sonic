#기본이 되는 모듈을 불러오는 코드 입니다.
import time
import pygame, sys
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load('disk11.mp3')
mixer.music.set_volume(1)
#함수들 입니다.
def shield():
    global n
    n = True
    shieldrect = pygame.Rect(rectto.x + 1, rectto.y, 100,200)
    shieldlist = []
    if herobineappear == True:
        shieldlist.append(shieldrect)
        screen.blit(herobinesshield, shieldlist[0])
        shieldlist.remove(shieldrect)
        n = False
        return
def axe():
    axerect = pygame.Rect(rectto.x - 1, rectto.y, 75, 155)
    axelist = []
    if herobineappear == True:
        axelist.append(axerect)
        screen.blit(herobinesaxe, axelist[0])
        axelist.remove(axerect)
        return
def attacking(s):
    global hpofHerobine,listone
    if not s and rect1.colliderect(rectto):
        hpofHerobine -= 1
        if hpofHerobine == 0:
            time.sleep(1)
            listone.remove(rectto)


#화면의 크기를 지정하는 코드 입니다.
width = 1000
height = 700
screen = pygame.display.set_mode((width,height))
listone = []

#중력을 선언하는 코드 입니다.
g = 30

#기본적인 이미지들을 선언하는 코드 입니다.
bgimage = pygame.image.load('그린힐존.png')
bgimage = pygame.transform.scale(bgimage,(1000,700))
img1 = pygame.image.load('소닉_가만히 있을 때 또는 걸을때.png')
img1 = pygame.transform.scale(img1, (80,80))
img3 = pygame.image.load('소닉_달릴때.png')
img3 = pygame.transform.scale(img3, (80,80))
ringimg = pygame.image.load('소닉_링.png')
ringimg = pygame.transform.scale(ringimg,(10,10))
herobine = pygame.image.load('히로빈비리빈빈빈.png')
herobine = pygame.transform.scale(herobine,(200,200))
herobinesshield = pygame.image.load('방패.png')
herobinesshield = pygame.transform.scale(herobinesshield, (100, 200))
herobinesaxe = pygame.image.load('다이아몬드도끼.png')
herobinesaxe = pygame.transform.scale(herobinesaxe, (75,155))
#왼쪽으로 움직이는 등장인물의 이미지가 바뀌게 하는 코드 입니다.
img2 = pygame.transform.flip(img1,True,False)
img2 = pygame.transform.scale(img2,(80,80))
img = img2
img4 = pygame.transform.flip(img3,True,False)
#등장인물의 Rect 객체를 선언하는 코드 입니다.
rect1 = pygame.Rect(890,430,80,80)
rectto = pygame.Rect(241,241,200,200)
bottomrect = pygame.Rect(0,530,1000,10)
herobineappear = False
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
    if keyInput[K_LEFT] and rect1.left > 0 and not rect1.colliderect(rectto):
        if keyInput[K_SPACE] and rect1.top > 0 and not rect1.colliderect(rectto):
            img = img4
        elif not keyInput[K_SPACE]:
            img = img2
        img = pygame.transform.scale(img,(80,80))
        rect1.left -= 30
        print("left")
    elif keyInput[K_RIGHT] and rect1.right < 1000 and not rect1.colliderect(rectto):
        if keyInput[K_SPACE] and rect1.top > 0 and not rect1.colliderect(rectto):
            img = img3
        elif not keyInput[K_SPACE]:
            img = img1
        img = pygame.transform.scale(img,(80,80))
        rect1.right += 30
        print("right")
    if keyInput[K_SPACE] and rect1.top > 0 and not rect1.colliderect(rectto):
        rect1.y -= 60
    for each in [bottomrect]:
        if not rect1.colliderect(each):
            rect1.y += g
#히로빈을 움직이는 코드 입니다.
    screen.blit(bgimage,(0,0))
    if herobineappear:
        screen.blit(herobine,(rectto))
    if rect1.x <= 750: 
        herobineappear = True
        mixer.music.play()
        listone.append(rectto)
        shield()
        axe()
        attacking(n)
        # while not hpofHerobine == 0:
        #     if rectto.colliderect(rect1):

#프레임을 조정하는 코드 입니다.
    CLOCK = pygame.time.Clock()
    CLOCK.tick(10000)
#화면에 이미지들을 띄우는 코드 입니다.
    screen.blit(img,(rect1))
    pygame.display.update()