import pygame 
import random
pygame.init()
W=600
H=600
gameWindow=pygame.display.set_mode((W,H+60))
pygame.display.set_caption("Snake Ladder")

board=pygame.image.load("Components\\board.jpg").convert_alpha()
board=pygame.transform.scale(board,(W,H)).convert_alpha()

bgimg=pygame.image.load("Components\\bgimg.jpg").convert_alpha()
bgimg=pygame.transform.scale(bgimg,(W,H)).convert_alpha()

d=[0]
snake_ladder = {1:38,4:14,17:7,9:31,21:42,28:84,51:67,54:34,62:19,64:60,72:91,80:99,87:36,93:73,95:75,98:79}
for x in range(1,7):
    i = pygame.image.load(f"Components\\d{x}.jpg").convert_alpha()
    i = pygame.transform.scale(i,(60,60)).convert_alpha()
    d.append(i)

P=pygame.image.load("Components\\P.png").convert_alpha()
C=pygame.image.load("Components\\C.png").convert_alpha()

P=pygame.transform.scale(P,(int(W/20),int(H/20))).convert_alpha()
C=pygame.transform.scale(C,(int(W/20),int(H/20))).convert_alpha()


clock=pygame.time.Clock()
font=pygame.font.SysFont(None,int(H/10))
font2=pygame.font.SysFont(None,int(50))
fps=10

pygame.mixer.music.load("Sounds//music.wav")
snake = pygame.mixer.Sound("Sounds//snake.wav")
ladder = pygame.mixer.Sound("Sounds//ladder.wav")

def text_screen(text, color, x, y,font):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def welcome():
    gameexit=False
    while not gameexit:
        gameWindow.blit(bgimg,(0,0))
        gameWindow.blit(P,(0,int(9*H/10)))
        gameWindow.blit(C,(int(W/20),int(9*H/10)))
        gameWindow.blit(d[6],(int(W/2)-int(d[6].get_width()/2),H))
        text_screen("Snake-Ladder",(0,0,0),int(W/4),int(H/2),font2)
        text_screen("Press Space Bar to Play",(0,0,0),int(W/4),int(H/2 + H/15),font2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game()
        pygame.display.update()
        clock.tick(fps)

def game():
    pygame.mixer.music.play(-1)
    gamerunning = True
    px,cx = 0,30
    py,cy = 540,540
    
    pn,cn = 0,0
    
    n = 6

    p , c = 1, 0
    
    strtp , strtc = 0,0
    
    dpn = 0
    dcn = 0
    blockp=0
    blockc=0
    blockp2 = 1
    blockc2 = 1
    while(gamerunning):
        pygame.draw.rect(gameWindow,(0,0,0),[0,0,W,H+60])
        gameWindow.blit(board,(0,0))
        gameWindow.blit(P,(px,py))
        gameWindow.blit(C,(cx,cy))
        gameWindow.blit(d[n],(int(W/2)-int( d[n].get_width()/2),H))
        text_screen(f"pn = {pn}",(250,0,0),0,600,font2)
        text_screen(f"cn = {cn}",(250,0,0),420,600,font2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamerunning = False
            if event.type==pygame.KEYDOWN :
                if(event.key==pygame.K_d and p):
                    n = random.randint(1,6)
                    if(n==6):
                        blockp=1
                    if(pn+n>100):
                        p=0
                        c=1
                        strtp = 0
                        dpn = 0
                        if(pn in snake_ladder.keys()):
                            if(snake_ladder[pn] - pn > 0):
                                pygame.mixer.Sound.play(ladder)
                            else:
                                pygame.mixer.Sound.play(snake)
                            pn = snake_ladder[pn]

                    strtp = 1
        if(blockp):
            if(p and strtp and blockp2):
                pn += 1
                dpn += 1

            if(pn==100):
                px = 0
                py = 0
            else:
                if(pn%10):
                    if((pn//10)%2==0):
                        px = 60*((pn%10)-1)
                    else:
                        px = 600 - 60*(pn%10)
                    py = 540 - 60*(pn//10)
                else:
                    if((pn/10)%2):
                        px = 540
                    else:
                        px = 0
                    py = 540 - 60*(pn//10)+60

            if(dpn >= n ):
                strtp = 0
                p = 0
                c = 1
                dpn = 0
                if(pn in snake_ladder.keys()):
                    if(snake_ladder[pn] - pn > 0):
                            pygame.mixer.Sound.play(ladder)
                    else:
                        pygame.mixer.Sound.play(snake)
                    pn = snake_ladder[pn]

        if(blockc!=1):
            n=random.randint(1,6)
            if(n==6):
                blockc=1
        if(blockc):
            if(c):
                n = random.randint(1,6)
                strtc = 1
                if(cn+n>100):
                    strtc = 0
                    p = 1
                    c = 0
                    dcn=0
                    if(cn in snake_ladder.keys()):
                        cn = snake_ladder[cn]

                if(cn+n==100):
                    blockc2 = 1

            
            if(c and strtc ):
                cn += 1
                dcn += 1
            
            if(dcn >= n ):
                strtc = 0
                p = 1
                c = 0
                dcn=0
                if(cn in snake_ladder.keys()):
                    cn = snake_ladder[cn]

            if(cn==100):
                cx = 0
                cy = 0
            elif(cn==0):
                cx = 30
                cy = 540
            else:
                if(cn%10):
                    if((cn//10)%2==0):
                        cx = 60*((cn%10)-1) + 30
                    else:
                        cx = 630 - 60*(cn%10)
                    cy = 540 - 60*(cn//10)
                else:
                    if((cn/10)%2):
                        cx = 570
                    else:
                        cx = 30
                    cy = 540 - 60*(cn//10) + 60
        
        if(pn==100 or cn == 100):
            strtp = 0
            strtc = 0
            p=0
            c=0
            pygame.draw.rect(gameWindow,(0,0,0),[0,0,W,H+60])
            text_screen(f"pn = {pn}",(250,0,0),0,600,font2)
            text_screen(f"cn = {cn}",(250,0,0),420,600,font2)
            done(pn,cn)
        
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def done(pn,cn):
    pygame.mixer.music.pause()
    pygame.display.update()
    win=""
    gameexit=False
    while not gameexit:
        gameWindow.blit(bgimg,(0,0))
        if(pn>cn):gameWindow.blit(P,(W/2,H/4))
        else:gameWindow.blit(C,(W/2,H/4))
        text_screen((lambda x: "You win" if x>0 else "Comp win")(pn-cn) ,(lambda x: (0,0,0) if x<0 else (250,0,0))(pn-cn),int(W/4),int(H/2),font2)
        text_screen("Press Space Bar to Replay",(lambda x: (0,0,0) if x<0 else (250,0,0))(pn-cn),int(W/4),int(H/2 + H/15),font2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game()
        pygame.display.update()
        clock.tick(fps)                   
    pygame.quit()
    quit()
welcome()
