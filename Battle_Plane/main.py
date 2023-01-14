import pygame
from title import Title
from button import Button
from loading import Loading
import os
from time import sleep


pygame.init()


width_window = 1366
hight_window = 768

screen = pygame.display.set_mode([width_window, hight_window])
#dimension display

pygame.display.set_caption("Battle Plane")
#name of game in display

#Groups
titleGroup = pygame.sprite.Group()

#directory Main
directory_main = os.path.dirname(__file__)

#directory Buttons
directory_button = os.path.join(directory_main, "image/button")

#Button Start
sprite_sheet_start = pygame.image.load(os.path.join(directory_button, "start/start.png")).convert_alpha()
start_button = Button(sprite_sheet_start, 680, 500, 32, 0, 32, 13, 11)

#Button Store
sprite_sheet_store = pygame.image.load(os.path.join(directory_button, "store/store.png")).convert_alpha()
store_button = Button(sprite_sheet_store, 60, 300, 31, 0, 31, 32, 2)

#directory Loading
directory_loading = os.path.join(directory_main, "image/loading")

sprite_sheet_loading = pygame.image.load(os.path.join(directory_loading, "loading.png")).convert_alpha()
sprite_sheet_bar_loading = pygame.image.load(os.path.join(directory_loading,"bar_loading.png")).convert_alpha()

loading = Loading(sprite_sheet_loading, 683, 384, 83, 0, 83, 13, 4, 4, 20, 1)
bar_loading = Loading(sprite_sheet_bar_loading, 200, 200, 32, 0, 32, 16, 4, 8, 40, 2)

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
            pygame.display.set_caption("Battle Plane (Main Menu)")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainmenuLoop = False
                    mainLoop = False
                    #close windowi

            if start_button.action:
                gameLoop = True
                sleep(0.5)
                mainmenuLoop = False

            if store_button.action:
                storeLoop = True
                sleep(0.5)
                mainmenuLoop = False
           
            screen.fill([0, 255, 247])
            #color of display

            start_button.draw(screen)
            store_button.draw(screen)
            titleGroup.draw(screen)

            titleGroup.update()

            pygame.display.update()
            #display update

        while gameLoop:
            pygame.display.set_caption("Battle Plane (Start)")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    mainLoop = False


            screen.fill([255, 255, 255])

            if(loading.exit_loading) == False:
                screen.fill([0, 0, 0])
                loading.draw(screen)
                bar_loading.draw(screen)

            pygame.display.update()

        while storeLoop:
            pygame.display.set_caption("Battle Plane (Store)")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    storeLoop = False
                    mainLoop = False
            screen.fill([43, 5, 65])
            
            pygame.display.update()

pygame.quit()
