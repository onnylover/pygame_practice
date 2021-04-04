import pygame

#초기화 (반드시 해야함)
pygame.init()

#화면 크기 설정
screen_width = 1024  #가로
screen_height = 768 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("DINGDONG Game") #게임이름   -> 여기서 실행하고 내용이 없으면 자동으로 종료됨

#배경 이미지 불러오기
background = pygame.image.load("/Volumes/Geozedo60/Python/pygame/background.png")

#이벤트 루프
running = True  #게임 진행에 대한 불리언, 종료되지 않도록 기본 설정 되어 있음 (필수)
while running:
    for event in pygame.event.get():    #이벤트 발새영부 체크
        if event.type == pygame.QUIT:   #종료 x 버튼을 누르면 끝나도록 되어 있음
            running = False             #게임 진행중이 아님을 확인

    screen.blit(background,(0, 0))      #배경이미지 불러오기
    #screen.fill((0,0,255))             #배경이미지를 rgb 값으로도 넣을수 있음
    pygame.display.update()             #화면 배경을 매번 업데이트 되어야함 (필수)




#이벤트 루프 종료/게임 종료
pygame.quit()

