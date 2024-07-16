import pygame, random

pygame.init()

ancho= 800
largo= 600
size=(800,600)
velocidad= 10
vidas=5
moneda_velocity= 5
score=0
moneda_aceleracion=0.5

FPS=60
clock=pygame.time.Clock()

fuente= pygame.font.SysFont("arial.tlf", 120)
score_text=fuente.render("Score:"+str(score),True,(0,0,0),(0,255,0))
score_rect=score_text.get_rect() 
score_rect.topleft = (350,10)

vidas_text=fuente.render("Vidas:"+str(vidas),True,(0,0,0),(0,255,0))
vidas_rect=vidas_text.get_rect() 
vidas_rect.topleft = (10,10)

perdiste_text=fuente.render("F en el chat:",True,(0,0,0),(0,255,0))
perdiste_rect=perdiste_text.get_rect() 
perdiste_rect.center = (ancho/2, largo/2)

pantalla= pygame.display.set_mode((ancho,largo))

black_image=pygame.image.load("black.png")
black_rect=black_image.get_rect()
black_rect.topleft=(64,largo/2)

moneda_image=pygame.image.load("moneda.png")
moneda_image= pygame.transform.scale(moneda_image,(60,60))
moneda_rect=moneda_image.get_rect()
moneda_rect.topleft=(ancho-200,largo/2)

fondo=pygame.image.load("fondo.png")
fondo=pygame.transform.scale(fondo,(ancho,largo))


running=True

while running:

    teclas= pygame.key.get_pressed()
    if teclas[pygame.K_UP] and black_rect.top>64:
        black_rect.y -= velocidad 
    if teclas[pygame.K_DOWN] and black_rect.bottom<largo:
        black_rect.y += velocidad 



#mover la moneda 

    if moneda_rect.x<0:
        vidas -=1
        print("me quedan: "+str(vidas))
        moneda_rect.x= ancho+100
        moneda_rect.y= random.randint(64,largo-32)
    else:
        moneda_rect.x -=moneda_velocity 


    if black_rect.colliderect(moneda_rect):
        score= score+1
        print(f"Mi puntaje es{score}")
        moneda_velocity+= moneda_aceleracion
        moneda_rect.x= ancho+100
        moneda_rect.y= random.randint(64,largo-32)

    vidas_text=fuente.render("Vidas:"+str(vidas),True,(0,0,0),(0,255,0))
    score_text=fuente.render("Score:"+str(score),True,(0,0,0),(0,255,0))



    if vidas == 0:
        pantalla.blit(perdiste_text,perdiste_rect)
        pygame.display.update()
        pausar = True 
        while pausar:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    score=0
                    vidas=5
                    moneda_velocity=5
                    pausar=False

                if evento.type == pygame.QUIT:
                    running=False
                    pausar=False
                    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running= False

    pantalla.blit(fondo,(0,0))
    pantalla.blit(black_image,black_rect)
    pantalla.blit(moneda_image,moneda_rect)

    pantalla.blit(score_text, score_rect)
    pantalla.blit(vidas_text,vidas_rect) 
    
    

    pygame.display.update()
    clock.tick(FPS)

