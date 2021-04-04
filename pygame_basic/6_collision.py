import pygame

#초기화 (반드시 해야함)
pygame.init()

#화면 크기 설정
screen_width = 1024  #가로
screen_height = 768 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("DINGDONG Game") #게임이름   -> 여기서 실행하고 내용이 없으면 자동으로 종료됨

#FPS 
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("/Volumes/Geozedo60/Python/pygame/background.png")

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("/Volumes/Geozedo60/Python/pygame/character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]         #캐릭터 가로
character_height = character_size[1]        #캐릭터 세로
character_x_pos = screen_width/2-character_width/2           #좌우위치, 화면의 1/2 위치에 설정
character_y_pos = screen_height-character_height             #상하위치, 화면 가장 아래에 설정 (좌표를 찾기 위해서 케릭터 높이 만큼 뺌)

#좌표이동 (키보드 이동 연결)
to_x = 0
to_y = 0

#이동속도
moveSpeed = 1.1

#적 캐릭터 관련
enermy = pygame.image.load("/Volumes/Geozedo60/Python/pygame/enermy.png")
enermy_size = enermy.get_rect().size  #이미지의 크기를 구해옴
enermy_width = enermy_size[0]         #캐릭터 가로
enermy_height = enermy_size[1]        #캐릭터 세로
enermy_x_pos = screen_width/2-enermy_width/2           #좌우위치, 화면의 1/2 위치에 설정
enermy_y_pos = screen_height/2-enermy_height/2             #상하위치, 화면 1/2 위치에 설정 (좌표를 찾기 위해서 케릭터 높이 만큼 뺌)

#이벤트 루프
running = True  #게임 진행에 대한 불리언, 종료되지 않도록 기본 설정 되어 있음 (필수)
while running:
    dt = clock.tick(60)     #게임화면의 초당 프레임수를 설정
    #print("fps : "+str(clock.get_fps()))

    #캐릭터가 100만큼 이동
    #10fps : 1초 동안 10번 동작 -> 1회 동작에 10씩 이동 (이동의 값이 달라짐)
    #20fps : 1초 동안 20번 동작 -> 1회 동작에 5씩 이동


    for event in pygame.event.get():    #이벤트 발새영부 체크
        if event.type == pygame.QUIT:   #종료 x 버튼을 누르면 끝나도록 되어 있음
            running = False             #게임 진행중이 아님을 확인
    

        if event.type == pygame.KEYDOWN:        #키보드를 눌렀는지 확인
            if event.key == pygame.K_LEFT:      #키보드 방향 : 왼쪽
                to_x -= moveSpeed
            elif event.key == pygame.K_RIGHT:   #키보드 방향 : 오른쪽
                to_x += moveSpeed
            elif event.key == pygame.K_UP:      #키보드 방향 : 위쪽
                to_y -= moveSpeed
            elif event.key == pygame.K_DOWN:    #키보드 방향 : 아래쪽
                to_y += moveSpeed
        
        if event.type == pygame.KEYUP:          #키보드를 떼고 있는지 확인 (KEYUP<->KEYDOWN)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt     #포지션 변경에 대해 x 변수값 변경  // dt 를 곱하는 이유는 fps 를 감안해서 동작하도록 함
    character_y_pos += to_y * dt     #포지션 변경에 대해 y 변수값 변경

    #가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    #세로 경계값 처리        
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height

    #충돌 처리 collision    
    character_rect = character.get_rect()       #케릭터의 사각정보에 위치 정보를 넣어줌
    character_rect.left = character_x_pos       
    character_rect.top = character_y_pos

    enermy_rect = enermy.get_rect()             #케릭터의 사각정보에 위치 정보를 넣어줌
    enermy_rect.left = enermy_x_pos       
    enermy_rect.top = enermy_y_pos

    #충돌 체크
    if character_rect.colliderect(enermy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background,(0, 0))      #배경이미지 불러오기
    screen.blit(character,(character_x_pos,character_y_pos))    #케릭터이미지 불러오기
    screen.blit(enermy,(enermy_x_pos,enermy_y_pos))    #적캐릭터 그리기
    #screen.fill((0,0,255))             #배경이미지를 rgb 값으로도 넣을수 있음
    pygame.display.update()             #화면 배경을 매번 업데이트 되어야함 (필수)
    


#이벤트 루프 종료/게임 종료
pygame.quit()

