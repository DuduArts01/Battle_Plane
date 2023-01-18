import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image, x, y, image_x, image_y, width, height, scale_x, scale_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.images_button = []
        
        img = image.subsurface((0 * image_x, image_y), (width, height))
        img = pygame.transform.scale(img, (width * scale_x, height * scale_y))
        self.images_button.append(img)



        self.image = self.images_button[0]
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, width * scale_x, height * scale_y)

    def draw(self, surface):
        self.image = self.images_button[int(0)]


        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
