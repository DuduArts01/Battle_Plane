import pygame
from title import Title
import button
from time import sleep

pygame.init()

width_window = 1366
hight_window = 768

screen = pygame.display.set_mode([width_window, hight_window])
#dimension display

pygame.display.set_caption("Battle Plane")
#name of game in display

#Object



#Groups
titleGroup = pygame.sprite.Group()
buttonGroup = pygame.sprite.Group()

#Button Start
start_img_1 = pygame.image.load("image/button/start/start.png").convert_alpha()
start_img_2 = pygame.image.load("image/button/start/start_pressed.png").convert_alpha()
start_button = button.Button(540, 400, start_img_1, start_img_2, 9, buttonGroup)

#Button Option
option_img_1 = pygame.image.load("image/button/option/option.png").convert_alpha()
option_img_2 = pygame.image.load("image/button/option/option_pressed.png").convert_alpha()
option_button = button.Button(600, 550, option_img_1, option_img_2, 5, buttonGroup)

#Button Store
store_img_1 = pygame.image.load("image/button/store/store.png").convert_alpha()
store_img_2 = pygame.image.load("image/button/store/store_pressed.png").convert_alpha()
store_button = button.Button(20, 230, store_img_1, store_img_2, 2, buttonGroup)

def main_menu():
    title = Title(titleGroup)
    title.image = pygame.transform.scale(title.image, [500, 250])
    title.rect = pygame.Rect(430, 10, 500, 200)

main_menu()

mainLoop = True
mainmenuLoop = True
gameLoop = False
optionLoop = False
storeLoop = False

clock = pygame.time.Clock()

PLAY_MOUSE_POS = pygame.mouse.get_pos()

if __name__ == "__main__":
    while mainLoop:
        clock.tick(60)
        while mainmenuLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainmenuLoop = False
                    mainLoop = False
                    #close windowi

            if start_button.action == True:
                gameLoop = True
                sleep(0.5)
                mainmenuLoop = False

            if option_button.action == True:
                optionLoop = True
                sleep(0.5)
                mainmenuLoop = False

            if store_button.action == True:
                storeLoop = True
                sleep(0.5)
                mainmenuLoop = False

            screen.fill([0, 255, 247])
            #color of display

            start_button.draw(screen)
            option_button.draw(screen)
            store_button.draw(screen)
            titleGroup.draw(screen)
            
            titleGroup.update()



            pygame.display.update()
            #display update

        while gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    mainLoop = False

            screen.fill([255,78,32])

            pygame.display.update()

        while optionLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    optionLoop = False
                    mainLoop = False
            screen.fill([255, 255, 255])
            
            pygame.display.update()
        while storeLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    storeLoop = False
                    mainLoop = False
            screen.fill([43, 5, 65])
            
            pygame.display.update()

pygame.quit()
