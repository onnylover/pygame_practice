
import os
import pygame

#--------- 필수 환경 설정
#초기화 (필수)
pygame.init()

#화면 크기 설정 (필수)
screen_width = 640  #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (필수)
pygame.display.set_caption("PANGPANG Game by DINGDONG") #게임이름

#FPS (필수)
clock = pygame.time.Clock()

#--------- 사용자 설정
#배경 이미지 불러오기
current_path = os.path.dirname(__file__)        #현재 파일의 위치 반환
image_path =os.path.join(current_path,"images") #images 폴더 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]        #스테이지 높이위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_heigh = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_heigh - stage_height

#좌표이동 (키보드 이동 연결)
character_to_x = 0
character_speed = 8

#무기만들기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_with = weapon_size[0]    #무기가 날아가는 위치와 길이를 파악하기 위해 

#무기는 여러발 동시에 가능함
weapons = []

#무기 이동 속도
weapon_speed = 15

#적 캐릭터 관련
#텍스트 정보
#폰트 정의
#총 시간
#시직 시간정보
#이벤트 루프
running = True  #게임 진행에 대한 불리언, 종료되지 않도록 기본 설정 되어 있음 (필수)
while running:
    dt = clock.tick(60)     #게임화면의 초당 프레임수를 설정
    #------------ 실제 이벤트 영역 설정
    for event in pygame.event.get():    #이벤트 발생여부 체크)
        if event.type == pygame.QUIT:   #종료 x 버튼을 누르면 끝나도록 되어 있음
            running = False             #게임 진행중이 아님을 확인
            
    #키보드 동작 반영
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:      #왼쪽으로 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:      #오른쪽으로 이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:   #무기발사
                weapon_x_pos = character_x_pos + character_width/2 - weapon_with/2    #캐릭터 위치에서 무기 반만큼 이동시켜서 캐릭터 가운데에서 발사되도록
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    #프레임 내에 위치 설정
    character_x_pos += character_to_x

    #캐릭터 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    #무기 위치를 위로 조정
    weapons = [[w[0],w[1]-weapon_speed] for w in weapons]   #위로 올라가는것 처럼 보이기

    #천장에 닿은 무기 없애기
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]    #천정에 안 닿은거만 남겨둠, y좌표가 0보다 큰 경우


    #충돌 처리 collision    
    #충돌 체크
    #타이머 설정
    #경과 시간 계산
    #타이어 시간이 0 이하면 게임 종료
    #화면 배경을 매번 업데이트 되어야함 (필수, 순서대로 노출)
    screen.blit(background,(0,0))
    for weapon_x_pos,weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()             
    
#잠시 대기 (2초)
pygame.time.delay(2000)

#이벤트 루프 종료/게임 종료 (필수)
pygame.quit()

