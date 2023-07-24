import pygame
pygame.init
screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("임시이름")
clock = pygame.time.Clock()
background_1 = pygame.image.load("C:\\Users\\User\\Desktop\\game\\game_design\\background.png")
character = pygame.image.load("C:\\Users\\User\\Desktop\\game\\game_design\\character.png")
character_width = 50
character_height = 50
character_x_pos = 100
character_y_pos = screen_height / 2
character_speed = 0.3
running = True
to_x = 0
to_y = 0
background_1_x_pos = 0
background_1_y_pos = 0
while running :
    #프레임 설정
    dt = clock.tick(60)
    for event in pygame.event.get():
        #게임종료
        if event.type == pygame.QUIT:
            running = False
        #움직이기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x += character_speed
            elif event.key == pygame.K_RIGHT:
                to_x -= character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.  K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.  K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        #화면 이동
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    background_1_x_pos += to_x * dt
    if character_y_pos >= screen_height or character_y_pos <= 0:
        character_y_pos = 0
    if background_1_x_pos <= -2800:
        background_1_x_pos = -2800
    #화면에 표시
    screen.blit(background_1, (background_1_x_pos,background_1_y_pos))
    screen.blit(character, (100, character_y_pos))
    pygame.display.update()
pygame.quit()