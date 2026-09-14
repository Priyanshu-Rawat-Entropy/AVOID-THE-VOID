import pygame as pg

import random



pg.init()


def game_loop():
    x=250
    y=250


    start=0
    sec=1
    Min=0

    xf=random.randint(0, x)
    yf=random.randint(0, y)
    x1=random.randint(0, 500)
    y1=random.randint(0,500)

    growth=20

    velo=4
    velo_void=10

    fps=120

    vel_x=0
    vel_y=0
    void_x=0
    void_y=0



    points=0

    screen=pg.display.set_mode((500,500))

    pg.display.set_caption('TEST_ver_0.0.3')
    quitg=False
    # game_over=False
    s_list=[[250,250]]
    s_lenght=1

    def plot(s_list,r,b,g):
        for x,y in s_list:
            pg.draw.circle(screen, (r,b,g),(x,y) , 10)
    while not quitg:
        if s_list[0] in s_list[1:len(s_list)] or( abs(x-x1)<25 and abs(y-y1)<25):
            # count=0
            if abs(x-x1)<25 and abs(y-y1)<25:

                # screen.fill((0,0,0))

                r1=random.randint(1,50)
                r2=random.randint(1,50)
                p1=random.randint(0, 500)
                p2=random.randint(0,500)
                p3=random.randint(0, 500)
                c1=random.randint(0, 250)
                c2=random.randint(0, 250)

                s1=random.randint(50, 52)
                s2=random.randint(40, 70)



                pg.draw.circle(screen, (225,0,0), (p1,p2), r1)

                pg.draw.circle(screen, (225,0,180), (p2,p1), r2)


                screen.blit(pg.font.SysFont(None, s1).render('^&&^&    D E A T H    !@#%# ',True,'black'),[20,220])
                screen.blit(pg.font.SysFont(None, 70).render(' 1 ',True,'darkgreen'),[p1,p3])
                screen.blit(pg.font.SysFont(None, 70).render(' 0 ',True,'darkgreen'),[p3,p2])
            # while count<100:
                # screen.fill((0,0,0))
            else:
                r=random.randint(1,50)
                r2=random.randint(1,50)
                p1=random.randint(0, 500)
                p2=random.randint(0,500)
                p3=random.randint(0, 500)
                c1=random.randint(0, 250)
                c2=random.randint(0, 250)
                c3=random.randint(0,250)
                s1=random.randint(20, 50)
                s2=random.randint(40, 70)
                s3=random.randint(60, 61)


                pg.draw.circle(screen, (225,0,0), (p1,p2), r)
                pg.draw.circle(screen, (225,0,0), (p2,p1), r2)

                # count+=1

                screen.blit(pg.font.SysFont(None, s1).render('DEAD',True,'white'),[p3,p2])
                screen.blit(pg.font.SysFont(None, s1).render('DEAD',True,'black'),[p2,p3])


                # screen.blit(pg.font.SysFont(None, s2).render(' I77T97T DIE 6843 ',True,'black'),[75,250])
                # screen.blit(pg.font.SysFont(None, s2).render(' I77T97T DIE 6843 ',True,'black'),[p2,p1])
                # screen.blit(pg.font.SysFont(None, s1).render('DEAD !@#%##%^&&^& ',True,'black'),[p1,p2])
                # screen.blit(pg.font.SysFont(None, s3).render('^&&^&    OVER    !@#%# ',True,'darkred'),[20,220])
                # screen.blit(pg.font.SysFont(None, c3).render(' 1 ',True,'darkgreen'),[p1,p3])
                # screen.blit(pg.font.SysFont(None, c3).render(' 0 ',True,'darkgreen'),[p3,p2])
                # screen.blit(pg.font.SysFont(None, 30).render('YOUR POINTS : '+str(points),True,'black'),[150,350])

        else:

            start+=1

            if start%60==0:

                sec+=1
                if sec>=60:
                    sec=0 
                    Min+=1
            pg.time.Clock().tick(fps)

            kevent=pg.key.get_pressed()
            if x>=500 :
                x=0
            elif x<=0:
                x=500
            elif y<=0:
                y=500
            elif y>=500:
                y=0

            if kevent[pg.K_LEFT] or kevent[pg.K_a]:
                vel_x=-velo
                vel_y=0
            elif kevent[pg.K_RIGHT] or kevent[pg.K_d]:
                vel_x=velo
                vel_y=0
            elif kevent[pg.K_UP] or kevent[pg.K_w]:
                vel_y=-velo
                vel_x=0
            elif kevent[pg.K_DOWN] or kevent[pg.K_s]:
                vel_y=velo
                vel_x=0 
            x+=vel_x
            y+=vel_y
            if abs(x-xf)<30 and abs(y-yf)<30:
                points+=1

                xf=random.randint(50,250)
                yf=random.randint(50,250)

                s_lenght+=1


            head=[]
            head.append(x+growth)
            head.append(y+growth)
            s_list.append(head)
            screen.fill((0,0,0))
            # p1=random.randint(0, 500)
            # p2=random.randint(0,500)
            # p3=random.randint(0, 500)
            # screen.blit(pg.font.SysFont(None, 50).render('1' ,True,'green'),[p1,p2])
            # screen.blit(pg.font.SysFont(None, 50).render('0' ,True,'green'),[p2,p1])
            # screen.blit(pg.font.SysFont(None, 50).render('1' ,True,'darkgreen'),[p1,p3])
            # screen.blit(pg.font.SysFont(None, 50).render('0' ,True,'darkgreen'),[p2,p3])
            # screen.blit(pg.font.SysFont(None, 50).render('1' ,True,'green'),[p3,p2])
            # screen.blit(pg.font.SysFont(None, 50).render('0' ,True,'darkgreen'),[p3,p1])

            screen.blit(pg.font.SysFont(None,30).render( f"{Min}min {sec}sec" ,True,'red'),[390,10])
            pg.draw.circle(screen, (225,0,0), (xf,yf), 10)
            r=random.randint(10,15)

            if x1>=500 :
                x1=0    
            elif x1<=0:
                x1=500
            elif y1<=0:
                y1=500
            elif y1>=500:
                y1=0

            l=[1,2,3,4]
            void_mo=random.choice(l)

            if void_mo==1:
                void_x=-velo_void
                void_y=0
            elif void_mo==2:
                void_x=velo_void
                void_y=0
            elif void_mo==3:
                void_y=-velo_void
                void_x=0
            elif void_mo==4:
                void_y=velo_void
                void_x=0 
            x1+=void_x
            y1+=void_y
            pg.draw.circle(screen, (225,225,225), (x1,y1), r)
            if abs(x-x1)<80 and abs(y-y1)<80:
                xo=random.randint(150,165)
                screen.blit(pg.font.SysFont(None, xo).render('R U N !!' ,True,'red'),[25,200])


            if len(s_list)>s_lenght:
                del s_list[0]

            r=random.randint(0, 225)
            b=random.randint(0, 225)
            g=random.randint(0, 225)

            plot(s_list,r,b,g)

        for event in pg.event.get():
            if event.type==pg.QUIT:
                quitg=True
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    game_loop()

        pg.display.update()

    pg.quit()
game_loop()