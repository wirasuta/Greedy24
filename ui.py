import pygame

pygame.init()
bgcolor = (107,150,106)
screen = pygame.display.set_mode((900, 700))
done = False
clock = pygame.time.Clock()
rectangle_draging = False

rectangle = pygame.rect.Rect(30, 460, 160,220)

def drawScreen() :
    #Title Box
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 10, 880,140), 2)
    #4 Card Box
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 160, 880,280), 2)
    # Individual cards
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(60, 190, 160,220), 2)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(270, 190, 160,220), 2)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(470, 190, 160,220), 2)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(680, 190, 160,220), 2)
    # Card deck outline
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 460, 160,220), 2)

    pygame.draw.rect(screen, (255,0,0), rectangle, 0)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if rectangle.collidepoint(event.pos):
                            rectangle_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = rectangle.x - mouse_x
                            offset_y = rectangle.y - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        rectangle_draging = False

                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_draging:
                        mouse_x, mouse_y = event.pos
                        rectangle.x = mouse_x + offset_x
                        rectangle.y = mouse_y + offset_y

        screen.fill(bgcolor)
        drawScreen()
        #         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #             is_blue = not is_blue
        #
        # isPressed = pygame.key.get_pressed()
        # if isPressed[pygame.K_UP] : y -= 3
        # if isPressed[pygame.K_DOWN] : y += 3
        # if isPressed[pygame.K_LEFT] : x -= 3
        # if isPressed[pygame.K_RIGHT] : x += 3
        #
        #
        #
        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 0)
        # screen.fill((0, 0, 0))
        #
        pygame.display.flip()
        clock.tick(30)
