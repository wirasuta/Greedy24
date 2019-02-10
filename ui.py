import pygame
from DeckOfCards import DeckOfCards
#Initilize Global Game Variables
pygame.init()
bgcolor = (107,150,106)
screen = pygame.display.set_mode((900, 700))
done = False
clock = pygame.time.Clock()
rectangle_draging = False



class CardSprite(pygame.sprite.Sprite):
    def __init__(self,val,sym):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("img/JPEG/%s%s.png" % (val,sym)).convert()
        self.image = pygame.transform.scale(self.image, (160, 220))
        self.rect=self.image.get_rect()
        self.rect.x = 680
        self.rect.y = 460
        print ("img/JPEG/%s%s.png" % (val,sym))



class DeckSprite(pygame.sprite.Sprite):
 def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #Get Deck Image
    self.image=pygame.image.load("img/JPEG/gray_back.png").convert()
    self.image = pygame.transform.scale(self.image, (160, 220))
    self.rect=self.image.get_rect()
    self.rect.x = 680
    self.rect.y = 460



deck = DeckOfCards()
decksp = DeckSprite()
deckBox = decksp.rect
cardGroup = pygame.sprite.Group()
cardList = []
ncards = 0

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
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(680, 460, 160,220), 2)
    #Deck Back
    screen.blit(decksp.image, [decksp.rect.x,decksp.rect.y])
    cardGroup.draw(screen)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if deckBox.collidepoint(event.pos):
                            if (ncards < 4) :
                                newcard = deck.draw()
                                newSprite = CardSprite(newcard.getValue(),newcard.getSymbol())
                                cardGroup.add(newSprite)
                                cardList.append(newSprite)
                                # print(newcard.getValue())
                                # print(newcard.getSymbol())

                        for Card in cardList :
                            if Card.rect.collidepoint(event.pos) :
                                currentCard = Card.rect
                                rectangle_draging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = currentCard.x - mouse_x
                                offset_y = currentCard.y - mouse_y
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        currentCard = None
                        rectangle_draging = False

                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_draging:
                        mouse_x, mouse_y = event.pos
                        currentCard.x = mouse_x + offset_x
                        currentCard.y = mouse_y + offset_y

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

        pygame.display.flip()
        clock.tick(30)
