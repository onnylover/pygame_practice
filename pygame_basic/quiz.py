import pygame
import random

#초기화 (반드시 해야함)
pygame.init()

#화면 크기 설정
screen_width = 1024  #가로
screen_height = 768 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("QUIZ Game") #게임이름   -> 여기서 실행하고 내용이 없으면 자동으로 종료됨

#FPS 
clock = pygame.time.Clock()
 
#배경 이미지 불러오기
background = pygame.image.load("/Volumes/Geozedo60/Python/pygame/pygame_basic/quiz_background.png")

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("/Volumes/Geozedo60/Python/pygame/pygame_basic/quiz_character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0]         #캐릭터 가로
character_height = character_size[1]        #캐릭터 세로
character_x_pos = screen_width/2-character_width/2           #좌우위치, 화면의 1/2 위치에 설정
character_y_pos = screen_height-character_height             #상하위치, 화면 가장 아래에 설정 (좌표를 찾기 위해서 케릭터 높이 만큼 뺌)

#좌표이동 (키보드 이동 연결) 
to_x = 0

#이동속도
moveSpeed = 1.1

#적 캐릭터 관련
enermy = pygame.image.load("/Volumes/Geozedo60/Python/pygame/pygame_basic/quiz_enermy.png")
enermy_size = enermy.get_rect().size  #이미지의 크기를 구해옴
enermy_width = enermy_size[0]         #캐릭터 가로
enermy_height = enermy_size[1]        #캐릭터 세로
enermy_x_pos = random.randint(0,screen_width-enermy_width)
enermy_y_pos = 0
enermy_speed = 10

#텍스트 정보
#폰트 정의
game_font = pygame.font.Font(None,40)       #폰트 객체 생성, 폰트/크기


#총 시간
total_time = 10

#시직 시간정보
start_ticks = pygame.time.get_ticks()       #시작 tick 을 받아옴, 자동으로 빼주는 기능이 있음

#이벤트 루프
running = True  #게임 진행에 대한 불리언, 종료되지 않도록 기본 설정 되어 있음 (필수)
while running:
    dt = clock.tick(60)     #게임화면의 초당 프레임수를 설정
    #print("fps : "+str(clock.get_fps()))

    #캐릭터가 100만큼 이동
    #10fps : 1초 동안 10번 동작 -> 1회 동작에 10씩 이동 (이동의 값이 달라짐)
    #20fps : 1초 동안 20번 동작 -> 1회 동작에 5씩 이동


    for event in pygame.event.get():    #이벤트 발생여부 체크
        if event.type == pygame.QUIT:   #종료 x 버튼을 누르면 끝나도록 되어 있음
            running = False             #게임 진행중이 아님을 확인
    
        if event.type == pygame.KEYDOWN:        #키보드를 눌렀는지 확인
            if event.key == pygame.K_LEFT:      #키보드 방향 : 왼쪽
                to_x -= moveSpeed
            elif event.key == pygame.K_RIGHT:   #키보드 방향 : 오른쪽
                to_x += moveSpeed
        
        if event.type == pygame.KEYUP:          #키보드를 떼고 있는지 확인 (KEYUP<->KEYDOWN)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    character_x_pos += to_x * dt     #포지션 변경에 대해 x 변수값 변경  // dt 를 곱하는 이유는 fps 를 감안해서 동작하도록 함

    #가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    enermy_y_pos += enermy_speed
    
    #enermy 랜덤 반복       
    if enermy_y_pos >= screen_height :
        enermy_y_pos = 0
        enermy_x_pos = random.randint(0,screen_width-enermy_width)
        
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

    #타이머 설정
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks()-start_ticks) /1000      #경과시간(ms)을 초단위로 계산
    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))   #출력할 글자 : str로 전환된 남은시간/초, True, 글자색상(rgb)
    screen.blit(timer,(10,10))

    #타이어 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <=0:
        print("타임아웃")
        running = False


    pygame.display.update()             #화면 배경을 매번 업데이트 되어야함 (필수)
    

#잠시 대기 (2초)
pygame.time.delay(2000)

#이벤트 루프 종료/게임 종료
pygame.quit()

