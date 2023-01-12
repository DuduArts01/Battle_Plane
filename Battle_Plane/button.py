import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2, scale, *groups):
        super().__init__(*groups)
        self.image = image 
        self.x = x
        self.y = y
        self.scale = scale
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        self.rect = pygame.Rect(x, y, self.width * scale, self.height * scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.image1 = image
        self.image2 = image2

        self.clicked = False
        self.action = False

    def draw(self, surface):
        self.action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.image = self.image2
                self.image = pygame.transform.scale(self.image, (int(self.width * self.scale), int(self.height * self.scale)))
                self.rect = pygame.Rect(self.x, self.y, self.width * self.scale, self.height * self.scale)
                self.action = True

            else:
                self.clicked = False
                self.action = False
                self.image = self.image1
                self.image = pygame.transform.scale(self.image, (int(self.width * self.scale), int(self.height * self.scale)))
                self.rect = pygame.Rect(self.x, self.y, self.width * self.scale, self.height * self.scale)

  

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))




        pass
