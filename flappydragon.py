import pygame, random

pygame.init()

ancho= 800
largo= 600
size=(800,600)
velocidad= 10
score=0


FPS=60
clock=pygame.time.Clock()

fuente= pygame.font.SysFont("arial.tlf", 120)
score_text=fuente.render("Score:"+str(score),True,(0,0,0),(0,255,0))
score_rect=score_text.get_rect() 
score_rect.topleft = (0,0)

tubo_altura=[150,200,300]
altura_ramdom=random.choice(tubo_altura)

tubo1=pygame.image.load("tubo1 (1).png")
tubo1_rect=tubo1.get_rect() 
tubo1_rect.x=largo+100
tubo1_rect.y=0

tubo2=pygame.image.load("tubo1 (2).png")
tubo2_rect=tubo2.get_rect() 
tubo2_rect.x=largo+100
tubo2_rect.y=random.randint(400,largo-100)

tubo2=pygame.image.load("tubo1 (2).png")

perdiste_text=fuente.render("F en el chat:",True,(0,0,0),(0,255,0))
perdiste_rect=perdiste_text.get_rect() 
perdiste_rect.center = (ancho/2, largo/2)


pantalla= pygame.display.set_mode((ancho,largo))

black_image=pygame.image.load("black.png")
black_rect=black_image.get_rect()
black_rect.topleft=(64,largo/2)

fondo=pygame.image.load("fondo.png")
fondo=pygame.transform.scale(fondo,(ancho,largo))

running=True

while running:

    perdiste_text=fuente.render("F en el chat:",True,(0,0,0),(0,255,0))
    perdiste_rect=perdiste_text.get_rect() 
    perdiste_rect.center = (ancho/2, largo/2)

    black_rect.y+=5

    if (tubo1_rect.x<0) and (tubo2_rect.x<0):
        score += 1
        tubo1_rect.x=largo+100
        tubo1_rect.y=0

        tubo2_rect.x=largo+100
        tubo2_rect.y=random.randint(400,largo-100)

    else: 
        tubo1_rect.x -= velocidad
        tubo2_rect.x -= velocidad

    if (black_rect.colliderect(tubo1_rect)) or (black_rect.colliderect(tubo2_rect)):
        pantalla.blit(perdiste_text, perdiste_rect)
        pygame.display.update()

    
        pausar= True 

        while pausar:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score=0 
                    tubo1_rect.x=largo+100
                    tubo2_rect.x=largo+100
                    black_rect.y=largo/2

                    pausar=False
                if event.type == pygame.QUIT:
                    pausar=False
                    running=False


        



    teclas= pygame.key.get_pressed()
    if teclas[pygame.K_UP] and black_rect.top>64:
        black_rect.y -= velocidad 


    score_text=fuente.render("Score:"+str(score),True,(0,0,0),(0,255,0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running= False

    pantalla.blit(fondo,(0,0))
    pantalla.blit(black_image,black_rect)
    pantalla.blit(score_text, score_rect)
    pantalla.blit(tubo1,tubo1_rect)
    pantalla.blit(tubo2,tubo2_rect)
    
    pygame.display.update()
    clock.tick(FPS)

