import pygame

class Title(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("image/title/title.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(430, 10, 100, 100)

