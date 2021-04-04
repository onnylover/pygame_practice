
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
#이동속도
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
    for event in pygame.event.get():    #이벤트 발새영부 체크
        if event.type == pygame.QUIT:   #종료 x 버튼을 누르면 끝나도록 되어 있음
            running = False             #게임 진행중이 아님을 확인
    #키보드 동작 반영    
    #프레임 내에 위치 설정 (프레임속도 반영)
    #가로 경계값 처리
    #세로 경계값 처리        
    #충돌 처리 collision    
    #충돌 체크
    #타이머 설정
    #경과 시간 계산
    #타이어 시간이 0 이하면 게임 종료
    #화면 배경을 매번 업데이트 되어야함 (필수)
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()             
    
#잠시 대기 (2초)
pygame.time.delay(2000)

#이벤트 루프 종료/게임 종료 (필수)
pygame.quit()

