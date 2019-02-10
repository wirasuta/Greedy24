import pygame
from DeckOfCards import DeckOfCards
from solve import solve
# --------------------------------
# Initilize UI Variables and Fonts
# --------------------------------
pygame.init()
bgcolor = (60, 142, 83)
screen = pygame.display.set_mode((900, 700))


# Fonts and Texts
pygame.font.init() # you have to call this at the start, 
Titlefont = pygame.font.SysFont('lobster14', 50)
Credfont = pygame.font.SysFont('lobster14', 30)
Textfont = pygame.font.SysFont('dejavuserif',20, True)
Title = Titlefont.render('24 Cards The Game', False, (0, 0, 0))
Creds =Credfont.render('By Garda, Dika, Tude', False, (0, 0, 0))
Reset = Credfont.render('Reset',False,(0,0,0))

# -------------------
# Create Game Objects
# -------------------

class CardSprite(pygame.sprite.Sprite):
    def __init__(self,val,sym):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("img/PNG/%s%s.png" % (val,sym)).convert()
        self.image = pygame.transform.scale(self.image, (160, 220))
        self.rect=self.image.get_rect()
        self.rect.x = 680
        self.rect.y = 460
        print ("img/JPEG/%s%s.png" % (val,sym))




class DeckSprite(pygame.sprite.Sprite):
 def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #Get Deck Image
    self.image=pygame.image.load("img/PNG/gray_back.png").convert()
    self.image = pygame.transform.scale(self.image, (160, 220))
    self.rect=self.image.get_rect()
    self.rect.x = 680
    self.rect.y = 460

# ----------------------------------- 
# Initiate Game objects and variables
# -----------------------------------

done = False
clock = pygame.time.Clock()
rectangle_draging = False
deck = DeckOfCards()
decksp = DeckSprite()
deckBox = decksp.rect
cardGroup = pygame.sprite.Group()
cardList = []
values = []
remaining = 52
ncards = 0
Button = pygame.rect.Rect(60,600,100,60)
solved = False
pointNum= 0
expression = ""
currentCard = None

CardBox = []
CardBox.append(pygame.draw.rect(screen, (0,0,0), pygame.Rect(60, 190, 160,220), 2))
CardBox.append(pygame.draw.rect(screen, (0,0,0), pygame.Rect(270, 190, 160,220), 2))
CardBox.append(pygame.draw.rect(screen, (0,0,0), pygame.Rect(470, 190, 160,220), 2))
CardBox.append(pygame.draw.rect(screen, (0,0,0), pygame.Rect(680, 190, 160,220), 2))
isEmpty = [True,True,True,True]



# ------------
# UI Functions
# ------------

def drawScreen() :
    #Title Box
    # pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 10, 880,140), 2)

    #4 Card Box
    # pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 160, 880,280), 2)
    # Individual card Outline
    pygame.draw.rect(screen, (0,0,0), CardBox[0], 2)
    pygame.draw.rect(screen, (0,0,0), CardBox[1], 2)
    pygame.draw.rect(screen, (0,0,0), CardBox[2], 2)
    pygame.draw.rect(screen, (0,0,0), CardBox[3], 2)
    # Card deck outline
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(680, 460, 160,220), 2)
    #Deck Back
    screen.blit(decksp.image, [decksp.rect.x,decksp.rect.y])
    #Button
    pygame.draw.rect(screen,(0,0, 0), Button,6)

    #Disply Text
    screen.blit(Title,(250,30))
    screen.blit(Creds,(290,100))
    screen.blit(Points,(520,600))
    screen.blit(Remainder,(400,640))
    screen.blit(Expr,(60,450))
    screen.blit(Reset,(80,610))
    cardGroup.draw(screen)


def reset(n) : 
    global ncards, isEmpty, expression, pointNum, values
    if n ==1 :
        remaining = 52
        ncards = 0
        deck = DeckOfCards()
    if n == 0 :
        ncards = 0
        isEmpty = [True for _ in range(4)]
        expression = ""
        pointNum = 0
        values = []

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
                                if (newcard.index == 1) :
                                    values.append(1)
                                else :
                                    values.append(newcard.index)

                                
                                ncards = ncards+1
                                remaining = remaining - 1
                                # print(newcard.getValue())
                                # print(newcard.getSymbol())
                        elif Button.collidepoint(event.pos) : 
                            reset(0)
                            cardGroup.remove([obj for obj in cardGroup ])
                            cardList = []

                        for Card in cardList :
                            if Card.rect.collidepoint(event.pos) :
                                currentCard = Card.rect
                                rectangle_draging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = currentCard.x - mouse_x
                                offset_y = currentCard.y - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if currentCard != None :
                            if (currentCard.colliderect(CardBox[0]) and isEmpty[0]) :
                                currentCard.x = 60
                                currentCard.y = 190
                                isEmpty[0] = False
                            elif (currentCard.colliderect(CardBox[1]) and isEmpty[1]) :
                                currentCard.x = 270
                                currentCard.y = 190
                                isEmpty[1] = False
                            elif (currentCard.colliderect(CardBox[2]) and isEmpty[2]) :
                                currentCard.x = 470
                                currentCard.y = 190
                                isEmpty[2] = False                         
                            elif (currentCard.colliderect(CardBox[3]) and isEmpty[3]) :
                                currentCard.x = 680
                                currentCard.y = 190
                                isEmpty[3] = False

                        currentCard = None
                        rectangle_draging = False

                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_draging:
                        mouse_x, mouse_y = event.pos
                        currentCard.x = mouse_x + offset_x
                        currentCard.y = mouse_y + offset_y


        if all([c == False for c in isEmpty]) :
            if (solved == False) :
                result = solve([values[0],values[1],values[2],values[3]])
                pointNum = result[1]
                expression = result[0]
                solved == True
            
        screen.fill(bgcolor)
        #Update remaining 
        Remainder = Textfont.render('Remaining Cards : %s' % (remaining), False, (0, 0, 0))
        Expr = Credfont.render('Optimal Expression : %s' % (expression),False,(0,0,0))
        Points = Textfont.render('Points : %.2f' % (pointNum), False, (0, 0, 0))
        drawScreen()


        pygame.display.flip()
        clock.tick(30)
