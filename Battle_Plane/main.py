import pygame
from pygame.locals import *
from start import Start
from option import Option
from store import Store
from title import Title

pygame.init()

display = pygame.display.set_mode([1366, 768])
#dimension display

pygame.display.set_caption("Battle Plane")
#name of game in display

#Object
buttonGroup = pygame.sprite.Group()
titleGroup = pygame.sprite.Group()
storeGroup = pygame.sprite.Group()
titleGroup = pygame.sprite.Group()

def main_menu():
    title = Title(titleGroup)
    title.image = pygame.transform.scale(title.image, [500, 250])
    title.rect = pygame.Rect(430, 10, 500, 200)

    button_Store = Store(storeGroup)
    button_Store.image = pygame.transform.scale(button_Store.image, [50, 50])
    button_Store.rect = pygame.Rect(20, 200, 50, 50)

    button_Start = Start(buttonGroup)
    button_Start.image = pygame.transform.scale(button_Start.image, [300, 100])
    button_Start.rect = pygame.Rect(530, 430, 300, 100)
    button_Start.center = (530, 430)

    button_Option = Option(buttonGroup)
    button_Option.image = pygame.transform.scale(button_Option.image, [200, 70])
    button_Option.rect = pygame.Rect(583, 545, 200, 70)
    button_Option.center = (583, 545)


main_menu()

gameLoop = True
clock = pygame.time.Clock()
PLAY_MOUSE_POS = pygame.mouse.get_pos()

if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                #close windowi

        display.fill([0, 255, 247])
        #color of display

        titleGroup.draw(display)
        buttonGroup.draw(display)
        storeGroup.draw(display)


        storeGroup.update()
        titleGroup.update()
        buttonGroup.update()


        pygame.display.update()
        #display update
