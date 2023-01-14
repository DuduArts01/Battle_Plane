import pygame

class Loading(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, scale, count_image, time, which):
        pygame.sprite.Sprite.__init__(self)

        self.images_load = []

        for i in range(count_image):
            img = sprite_sheet.subsurface((i * image_x, image_y), (width, height))
            img = pygame.transform.scale(img, (width * scale, height * scale))
            self.images_load.append(img)

        self.which = which

        self.index = 0

        self.count_image = count_image

        self.time = time

        self.image = self.images_load[self.index]
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.count_loading = 0
        self.exit_loading = False

        self.clock = pygame.time.Clock()

    def draw(self, surface):
        self.clock.tick(12)
        
        if(self.which == 1):
            print(f"loading = {self.index}")
        else:
            print(f"bar loading = {self.index}")

        if(self.index > self.count_image):
            self.index = 0
        self.index += 0.25
        
        self.image = self.images_load[int(self.index)]

        self.count_loading += 0.25
        if(int(self.count_loading) > self.time):
            self.exit_loading = True

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass
