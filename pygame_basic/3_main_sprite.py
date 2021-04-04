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

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("/Volumes/Geozedo60/Python/pygame/character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]         #캐릭터 가로
character_height = character_size[1]        #캐릭터 세로
character_x_pos = screen_width/2-character_width/2           #좌우위치, 화면의 1/2 위치에 설정
character_y_pos = screen_height-character_height             #상하위치, 화면 가장 아래에 설정 (좌표를 찾기 위해서 케릭터 높이 만큼 뺌)

#이벤트 루프
running = True  #게임 진행에 대한 불리언, 종료되지 않도록 기본 설정 되어 있음 (필수)
while running:
    for event in pygame.event.get():    #이벤트 발새영부 체크
        if event.type == pygame.QUIT:   #종료 x 버튼을 누르면 끝나도록 되어 있음
            running = False             #게임 진행중이 아님을 확인

    screen.blit(background,(0, 0))      #배경이미지 불러오기
    screen.blit(character,(character_x_pos,character_y_pos))    #케릭터이미지 불러오기
    #screen.fill((0,0,255))             #배경이미지를 rgb 값으로도 넣을수 있음
    pygame.display.update()             #화면 배경을 매번 업데이트 되어야함 (필수)




#이벤트 루프 종료/게임 종료
pygame.quit()

