import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((1000,600))
pygame.display.set_caption("LABERINTO ICB")

blanco=(255,255,255)
Color= (0,255,55)
ColorDos=(70,80,150)
contador_de_pasos=0



#Importamos la imagen del jugador y la meta
Jugador=pygame.image.load("img/oli.png")

posX=50
posY=50

velocidad=50

Meta = pygame.image.load("img/porro.png")
pX= 900
pY = 500



while True:
	
	ventana.fill(blanco)
	""
	class mapa ():
		a= pygame.draw.rect(ventana,(130,130,0),(0,0,1000,50)) #pared superior
		b= pygame.draw.rect(ventana,(130,130,0),(0,550,1000,100))#pared inferior
		c= pygame.draw.rect(ventana,(130,130,0),(0,0,50,600)) #pared izquierda
		pygame.draw.rect(ventana,(130,130,0),(950,0,50,600)) #pared derecha
		pygame.draw.rect(ventana,(130,130,0),(50,100,200,50))#1
		pygame.draw.rect(ventana,(130,130,0),(100,200,250,50))#2
		pygame.draw.rect(ventana,(130,130,0),(300,100,50,250))#3
		pygame.draw.rect(ventana,(130,130,0),(50,300,200,50))#4
		pygame.draw.rect(ventana,(130,130,0),(150,350,50,150))#5
		pygame.draw.rect(ventana,(130,130,0),(100,400,50,100))#6
		pygame.draw.rect(ventana,(130,130,0),(250,400,150,100))#7
		pygame.draw.rect(ventana,(130,130,0),(400,400,50,150))#8
		pygame.draw.rect(ventana,(130,130,0),(350,300,200,50))#9
		pygame.draw.rect(ventana,(130,130,0),(400,100,50,150))#10
		pygame.draw.rect(ventana,(130,130,0),(450,100,200,50))#11
		pygame.draw.rect(ventana,(130,130,0),(600,100,50,350))#12
		pygame.draw.rect(ventana,(130,130,0),(500,400,100,50))#13
		pygame.draw.rect(ventana,(130,130,0),(500,200,50,100))#14
		pygame.draw.rect(ventana,(130,130,0),(500,450,50,50))#15
		pygame.draw.rect(ventana,(130,130,0),(600,500,50,50))#16
		pygame.draw.rect(ventana,(130,130,0),(650,350,50,50))#17
		pygame.draw.rect(ventana,(130,130,0),(700,50,50,150))#18
		pygame.draw.rect(ventana,(130,130,0),(750,100,50,150))#19
		pygame.draw.rect(ventana,(130,130,0),(650,250,150,50))#20
		pygame.draw.rect(ventana,(130,130,0),(850,100,50,450))#21
		pygame.draw.rect(ventana,(130,130,0),(750,350,100,50))#22
		pygame.draw.rect(ventana,(130,130,0),(700,450,100,50))#23
		pygame.draw.rect(ventana,(130,130,0),(750,350,50,100))#24
		pygame.draw.rect(ventana,(130,130,0),(350,350,50,50))#25

		

	
	mapa ()
	ventana.blit(Jugador,(posX,posY))
	ventana.blit(Meta,(pX,pY))
	
#Esto hace que la ventana se cierre si precionamos la X
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
			
		elif evento.type ==pygame.KEYDOWN:
			if evento.key==K_LEFT:
				posX-=velocidad
			elif evento.key==K_RIGHT:
				posX+=velocidad
			if evento.key==K_UP:
				posY-=velocidad
			elif evento.key==K_DOWN:
				posY+=velocidad
				
		elif evento.type ==pygame.KEYUP:
			if evento.key==K_LEFT:
				contador_de_pasos=contador_de_pasos +1
				#print (contador_de_pasos)
			elif evento.key==K_RIGHT:
				contador_de_pasos=contador_de_pasos +1
				#print (contador_de_pasos)
			if evento.key==K_UP:
				contador_de_pasos=contador_de_pasos +1
				#print (contador_de_pasos)
			elif evento.key==K_DOWN:
				contador_de_pasos=contador_de_pasos +1
				#print (contador_de_pasos)
					
	
		
			
			
	#print pygame.mouse.get_pos() muestra la posicion del mouse
	pygame.display.update()


