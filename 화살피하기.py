import pygame
import random

################################################################################

pygame.init() # 초기화

#화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 
pygame.display.set_caption("sheep's alive") #게임 이름

#FPS
clock = pygame.time.Clock()
################################################################################

#1. 사용자 게임 초기화(배경화면, 캐릭터, 좌표, 속도, 폰트 등)
#양 캐릭터
sheep = pygame.image.load("C:\python\화살피하기\양.png")
sheep_size = sheep.get_rect().size #이미지의 크기
sheep_width = sheep_size[0] #가로 크기
sheep_height = sheep_size[1] #세로 크기
sheep_x_pos = (screen_width / 2) - (sheep_width / 2) #화면 가로 중간에 위치
sheep_y_pos = screen_height - sheep_height #화면 세로 아래에 위치

#좌표
to_x = 0
to_y = 0

#속도
sheep_speed = 10

#화살 캐릭터
enemy = pygame.image.load("C:\python\화살피하기\화살.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #초당 프레임 수 설정

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #게임이 진행되도록 체크하는 것
        if event.type == pygame.QUIT: #게임자가 직접 x창을 눌렀을때
            running = False #게임이 끝남

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= sheep_speed
            elif event.key == pygame.K_RIGHT:
                to_x += sheep_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    #3. 게임 캐릭터 위치 정의 
    sheep_x_pos += to_x

    #밖으로 안 나가게
    if sheep_x_pos < 0:
        sheep_x_pos = 0
    elif sheep_x_pos > screen_width - sheep_width:
        sheep_x_pos = screen_width - sheep_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    #4. 충돌처리
    sheep_rect = sheep.get_rect()
    sheep_rect.left = sheep_x_pos
    sheep_rect.top = sheep_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌여부 확인
    if sheep_rect.colliderect(enemy_rect):
        print("DIE")
        running = False

    #5. 화면에 그리기
    screen.fill((233,185,255)) #보라색 배경
    screen.blit(sheep, (sheep_x_pos, sheep_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    pygame.display.update() #게임화면 다시 그리기
  
#게임 종료
pygame.quit()