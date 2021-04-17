import os
import pygame 

# start module
pygame.init() 

# size of the window
# 	width = 900
# 	height = 500
size = width, height = 900, 500
print (size)

FPS = 60
BLUE = (255, 0, 255)

screen = pygame.display.set_mode(size)

#set title bar to 
pygame.display.set_caption("Space defenders Low budget edition")

f = open("hello.txt", "r")
print(f.read())



""" NOTE: The (0, 0) origin is the top left corner and moving away from it is denoted by positive values """
################################################
# START

# spaceship declaration

man_size = width, height = 50, 50

man1 = pygame.transform.scale(pygame.image.load("man1.png"), man_size)

def drawOnScreen() :
	# fill window in darkness
	screen.fill(BLUE)
		
	# update the screen
	pygame.display.update()
	
	# draw  
	# (300, 100) is the position on screen 
	screen.blit(man1, (200, 150))


def main() :
	
	clock = pygame.time.Clock()
	run = True
	
	# continue loop until run == false
	while run:
		
		# set the max frame rate to FPS
		clock.tick(FPS)
		
		# check for all event occuring in the game window
		for event in pygame.event.get() :
			
			# if the event occured === pygame.QUIT status; stop the while loop
			if event.type == pygame.QUIT :
				run = False
		
		drawOnScreen()
						
	pygame.quit()
		
		

# check if the file is being imported or run as main
if __name__ == "__main__" :
	main()
