import random
import pygame

# screen_width = 1024
# enermy_width = 70
# ran_pos = random.randint(0,screen_width-enermy_width)
# print(ran_pos)

enermy = pygame.image.load("/Volumes/Geozedo60/Python/pygame/enermy.png")
enermy_size = enermy.get_rect().size  #이미지의 크기를 구해옴
enermy_width = enermy_size[0]         #캐릭터 가로
enermy_height = enermy_size[1]
print(enermy_width)
print(type(enermy_width))