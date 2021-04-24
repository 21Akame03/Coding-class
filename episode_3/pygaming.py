import pygame 
import os
pygame.font.init()

width, height = 900, 600
WIN = pygame.display.set_mode((width, height))
FPS = 60
MAX_BULLETS = 3
VEL = 5
BULLET_VEL = 7
BORDER = pygame.Rect((width//2) - 5, 0, 10, height) 
WHITE = (255, 255, 255)
RED =(255, 0, 0)
BLACK = (0, 0, 0)
HEALTH_FONT = pygame.font.SysFont('comcsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)


OFFICEMAN_HIT = pygame.USEREVENT + 1
LEGO_HIT = pygame.USEREVENT + 2



#characters
character_width = 60
character_height = 60

man1 = pygame.image.load(os.path.join('assets', 'man1.png'))
man2 = pygame.image.load(os.path.join('assets', 'man2.png'))
space = pygame.image.load(os.path.join('assets', 'space.png'))

man1 = pygame.transform.scale(man1, (60, 60))
man2 = pygame.transform.scale(man2, (60, 60))
space = pygame.transform.scale(space, (width, height))

def draw_window(lego, officeman, lego_bullets, officeman_bullets, lego_health, officeman_health) :
	WIN.blit(space, (0, 0))
	pygame.draw.rect(WIN, (0, 0, 0), BORDER)

	lego_health_text = HEALTH_FONT.render("Health: " + str(lego_health), 1, WHITE)
	officeman_health_text = HEALTH_FONT.render("Health: " +str(officeman_health), 1, WHITE)

	WIN.blit(officeman_health_text, (0, 0))
	WIN.blit(lego_health_text, ((width // 2) + 40 , 0))

	WIN.blit(man1, (lego.x, lego.y))
	WIN.blit(man2, (officeman.x, officeman.y))

	for bullet in lego_bullets:
		pygame.draw.rect(WIN, RED, bullet)
	
	for bullet in officeman_bullets:
		pygame.draw.rect(WIN, BLACK, bullet)

	pygame.display.update()

def draw_winner(text) :
	draw_text = WINNER_FONT.render("K.O", 1, WHITE)
	WIN.blit(draw_text, ( (width // 2) - draw_text.get_width() , (height // 2) - draw_text.get_height()) )
	pygame.display.update()
	pygame.time.delay(500)

	draw_text = WINNER_FONT.render(text, 1, WHITE)
	WIN.blit(draw_text, (width//2, height// 2))
	pygame.display.update()
	pygame.time.delay(700)



def officeman_handle_movement(keys_pressed, officeman) :
	# left key
	if keys_pressed[pygame.K_a] and officeman.x - VEL > 0:
		officeman.x -= VEL
	# right
	if keys_pressed[pygame.K_d] and officeman.x + VEL < BORDER.x - 60:
		officeman.x += VEL
	# up
	if keys_pressed[pygame.K_w] and officeman.y - VEL > 0:
		officeman.y -= VEL
	# down
	if keys_pressed[pygame.K_s] and officeman.y + VEL < height - 60:
		officeman.y += VEL

def lego_handle_movement(keys_pressed, lego) :
	# left key
	if keys_pressed[pygame.K_LEFT] and lego.x - VEL > BORDER.x:
		lego.x -= VEL
	# right
	if keys_pressed[pygame.K_RIGHT] and lego.x + VEL < width - 60:
		lego.x += VEL
	# up
	if keys_pressed[pygame.K_UP] and lego.y - VEL > 0 :
		lego.y -= VEL
	# down
	if keys_pressed[pygame.K_DOWN] and lego.y + VEL < height - 60:
		lego.y += VEL

def handle_bullets(officeman_bullets, lego_bullets, officeman, lego) :
	for bullet in officeman_bullets:
		bullet.x += BULLET_VEL

		if lego.colliderect(bullet):
			pygame.event.post(pygame.event.Event(LEGO_HIT))
			officeman_bullets.remove(bullet)
		elif bullet.x > width:
			officeman_bullets.remove(bullet)

	for bullet in lego_bullets:
		bullet.x -= BULLET_VEL
		if officeman.colliderect(bullet):
			pygame.event.post(pygame.event.Event(OFFICEMAN_HIT))
			lego_bullets.remove(bullet)
		elif bullet.x < 0:
			lego_bullets.remove(bullet)

def main() :

	lego = pygame.Rect(700, 300, 60, 60)
	officeman = pygame.Rect(100, 300, 60, 60)

	lego_health = 5
	officeman_health = 5
	lego_bullets = []
	officeman_bullets = []

	WINNER = ""
	clock = pygame.time.Clock()
	run = True
	while run :
		clock.tick(FPS)
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
			
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LCTRL and len(officeman_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(officeman.x + character_width, officeman.y + character_height // 2, 10, 5)
					officeman_bullets.append(bullet)
					
				if event.key == pygame.K_RCTRL and len(lego_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(lego.x, lego.y + character_height // 2, 10, 5)
					lego_bullets.append(bullet)


			if event.type == LEGO_HIT:
				lego_health -= 1
			if event.type == OFFICEMAN_HIT:
				officeman_health -= 1
			

			if lego_health == 0 :
				WINNER = "MR OFFICEGUY WINS"
			if officeman_health == 0:
				WINNER = "MR LEGO WINS"
			if WINNER != "":
				draw_winner(WINNER)
				run = False
				break
		

		keys_pressed = pygame.key.get_pressed()

		# handle movements
		lego_handle_movement(keys_pressed, lego)
		officeman_handle_movement(keys_pressed, officeman)

		# handle bullet actions
		handle_bullets(officeman_bullets, lego_bullets, officeman, lego)

		# handle updating of the window
		draw_window(lego, officeman, lego_bullets, officeman_bullets, lego_health, officeman_health)

	main()


if __name__ == "__main__" :
	main()