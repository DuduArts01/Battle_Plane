import pygame


class Pilot(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, scale, count_image, clock):
        pygame.sprite.Sprite.__init__(self)

        self.images_load = []

        for i in range(count_image):
            img = sprite_sheet.subsurface((i * image_x, image_y), (width, height))
            
            img = pygame.transform.scale(img, (width * scale, height * scale))
            self.images_load.append(img)

        self.index = 0


        self.image = self.images_load[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        

        self.clock = pygame.time.Clock()
        self.fps = clock


    def draw(self, surface):
        self.clock.tick(self.fps)
        
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.index = 3
                    self.image = self.images_load[int(self.index)]
                elif event.key == pygame.K_s:
                    self.index = 0
                    self.image = self.images_load[int(self.index)]
                elif event.key == pygame.K_a:
                    self.index = 10
                    self.image = self.images_load[int(self.index)]
                elif event.key == pygame.K_d:
                    self.index = 6
                    self.image = self.images_load[int(self.index)]

        if keys[pygame.K_w]:
            self.index = 3
            self.image = self.images_load[int(self.index)]
            self.index = 4
            self.image = self.images_load[int(self.index)]
            self.index = 5
            self.image = self.image_load[int(self.index)]

        elif keys[pygame.K_s]:
            self.index = 0
            self.image = self.images_load[int(self.index)]
            self.index = 1
            self.image = self.images_load[int(self.index)]
            self.index = 2
            self.image = self.images_load[int(self.index)]
     
        elif keys[pygame.K_a]:
            self.index = 9
            self.image = self.images_load[int(self.index)]
            self.index = 10
            self.image = self.images_load[int(self.index)]
            self.index = 11
            self.image = self.images_load[int(self.index)]
 
        elif keys[pygame.K_d]:
            self.index = 6
            self.image = self.images_load[int(self.index)]
            self.index = 7
            self.image = self.images_load[int(self.index)]
            self.index = 8
            self.image = self.images_load[int(self.index)]

        
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
