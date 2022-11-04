from turtle import clear
import pygame
pygame.init()


#colores
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
green = (0,255,0)
red = (255, 0, 0)
azul =  (0,0,128)
green1 = (0, 100, 0)
amarillo = (255,255,0)
player_width = 15
player_height = 90

#obstaculo
obstaculo_x = 400
obstaculo_y = 10
obstaculo_velocidad_y = 1
centro=150

#obstaculo2
obstaculo2_x = 400
obstaculo2_y = 520
obstaculo2_velocidad_y = 1






screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

#coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

#contador
contador1=0
contador2=0
tiempo=0
tiempo2=70

# coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3



game_over = False
while not game_over:
   
    mifuente=pygame.font.Font(None,100)
    mitexto=mifuente.render(str(contador1),25,(white))
    mifuente=pygame.font.Font(None,100)
    mitexto2=mifuente.render(str(contador2),25,(white))
    mifuente=pygame.font.Font(None,200)
    ganar1=mifuente.render("gano el jugador 1",25,(white))
    mifuente=pygame.font.Font(None,100)
    tiempo_pantalla=mifuente.render(str(tiempo),25,(white))
    tiempo2=pygame.time.get_ticks()/1000
    tiempo-=1
  
   
   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # Jugador1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            
            # Jugador 2ygame.K_UP:
            if  event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # Jugador1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
   
    if obstaculo_y > 229 or obstaculo_y < 10:
        obstaculo_velocidad_y *= -1

    if obstaculo2_y > 520 or obstaculo2_y < 301:
        obstaculo2_velocidad_y *= -1

    
    
   
    # Revisa si la pelota sale del lado derecho
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        contador1+=1

        # Si sale de la pantalla, invierte direccion 
        pelota_speed_x *=-1
        pelota_speed_y *=-1
    # Revisa si la pelota sale del lado izquierdo
    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        contador2 +=1
        #si sale de la pantalla, invierte direccion 
        pelota_speed_x *=-1
        pelota_speed_y *+-1

        #obstaculo1
    
    
    

    

    
    


    #Modifica las coordenadas para dar mov. a los jugadores/ pelota
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    # Movimiento de pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    #obstaculo movimiento
    obstaculo_y += obstaculo_velocidad_y
    obstaculo2_y += obstaculo2_velocidad_y




    
    screen.fill(green)
    #zona de dibujo
    linea_vertical = pygame.draw.rect(screen, green1, (0,0,50,800))
    linea_vertical = pygame.draw.rect(screen, green1, (50,0,350,800))
    linea_vertical = pygame.draw.rect(screen, green1, (250,0,50,800))
    
    
    
    
    
    
    
    #parte de zona dibujo    
    jugador1 = pygame.draw.rect(screen, amarillo, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, red, (player2_x_coor, player2_y_coor, player_width, player_height))
    linea_central=pygame.draw.rect(screen, white, (400,0,10,1000))
    linea_centro=pygame.draw.ellipse(screen, white, (300,200,200,200),15)
    obstaculo = pygame.draw.rect(screen, black, (obstaculo_x, obstaculo_y, player_width, player_height))
    obstaculo2 = pygame.draw.rect(screen, black, (obstaculo2_x, obstaculo2_y, player_width, player_height))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
    
    #Colisiones 
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2) or pelota.colliderect(obstaculo):
        pelota_speed_x *=-1

    screen.blit(mitexto,(200,300))
    screen.blit(mitexto2,(600,300))
    screen.blit(tiempo_pantalla,(350,10))
    
    
    
    #print(pelota_x,pelota_y)
    print("puntaje:", contador1,contador2)

    
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()