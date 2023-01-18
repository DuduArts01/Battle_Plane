import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, scale):
        pygame.sprite.Sprite.__init__(self)
        
        self.images_button = []
        
        img = sprite_sheet.subsurface((0 * image_x, image_y), (width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        self.images_button.append(img)

        img = sprite_sheet.subsurface((1 * image_x, image_y), (width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        self.images_button.append(img)


        
        self.image = self.images_button[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.clicked = False
        self.action = False

    def draw(self, surface):
        self.action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.action = True
                self.image = self.images_button[int(1)]

            else:
                self.clicked = False
                self.action = False



        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
