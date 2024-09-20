import pygame
pygame.init()

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image



def image(scale_size, file):
	screen = pygame.display.set_mode((16 * 16 * scale_size * 2, 16 * 9 * scale_size * 2))
	pygame.display.set_caption('Spritesheets')

	list = []
	f = open(file)
	for line in f:
		list.append(line[:-1])
		print(line)
		
	f.close()

	sprite_sheet_image = pygame.image.load(list[-7]).convert_alpha()
	sprite_sheet = SpriteSheet(sprite_sheet_image)

	BG = (50, 50, 50)
	BLACK = (0, 0, 0)


	frame_0 = sprite_sheet.get_image(0, 16, 16, scale_size, BLACK)
	frame_1 = sprite_sheet.get_image(1, 16, 16, scale_size, BLACK)
	frame_2 = sprite_sheet.get_image(2, 16, 16, scale_size, BLACK)
	frame_3 = sprite_sheet.get_image(3, 16, 16, scale_size, BLACK)
	frame_4 = sprite_sheet.get_image(4, 16, 16, scale_size, BLACK)
	frame_5 = sprite_sheet.get_image(5, 16, 16, scale_size, BLACK)
	run = True
	while run:

		#calculate each placement
		square = 0
		while square <= 576:
			
			if list[square] == '0':
				temp = frame_0
			elif list[square] == '1':
				temp = frame_1
			elif list[square] == '2':
				temp = frame_2
			elif list[square] == '3':
				temp = frame_3
			elif list[square] == '4':
				temp = frame_4
			elif list[square] == '5':
				temp = frame_5

			x = square % 32
			y = square // 32
			screen.blit(temp, (x* 16 * scale_size, y* 16 * scale_size))
			

			square += 1


		

		#show frame image
		# screen.blit(frame_0, (0, 0))
		# screen.blit(frame_1, (72, 0))
		# screen.blit(frame_2, (150, 0))
		# screen.blit(frame_3, (250, 0))

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	scale_size = 2
	file = input('Name of .txt file: ')
	background = image(scale_size, file)
	#make screen
	screen = pygame.display.set_mode((16 * 16 * scale_size * 2, 16 * 9 * scale_size * 2))
	#update background
	screen.fill(background)