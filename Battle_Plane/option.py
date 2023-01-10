import pygame

class Option(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("image/button/option/option.png")
        self.image = pygame.transform.scale(self.image, [200, 70])
        self.rect = pygame.Rect(583, 545, 200, 70)

        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load("image/button/option/option.png").convert_alpha()
        self.image2 = pygame.image.load("image/button/option/option_pressed.png").convert_alpha()

        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2
                self.image = pygame.transform.scale(self.image, [200, 70])
                self.rect = pygame.Rect(583, 545, 200, 70)


            else:
                self.touche = False
                self.image = self.image1
                self.image = pygame.transform.scale(self.image, [200, 70])
                self.rect = pygame.Rect(583, 545, 200, 70)

        pass
