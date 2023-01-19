import pygame, sys
from title import Title
from button import Button
from loading import Loading
import os
from time import sleep


pygame.init()

width_window = 854
hight_window = 480

#Dimension Screen
screen = pygame.display.set_mode([width_window, hight_window], pygame.RESIZABLE)

#directory Main
directory_main = os.path.dirname(__file__)

#directory Title
directory_title = os.path.join(directory_main, "image/title")

#directory Buttons
directory_button = os.path.join(directory_main, "image/button")

#directory Loading
directory_loading = os.path.join(directory_main, "image/loading")

#directory Pilot
directory_pilot = os.path.join(directory_main, "image/pilot")

#           IMAGES
#   MAIN MENU
#Title
image_title_game = pygame.image.load(os.path.join(directory_title, "name_game.png")).convert_alpha()
title_game = Title(image_title_game, (screen.get_width() / 2), (screen.get_height() / 5), 45, 0, 45, 27, (screen.get_width() / 3), (screen.get_height() / 3))

#Button Start
sprite_sheet_start = pygame.image.load(os.path.join(directory_button, "start/start.png")).convert_alpha()
start_button = Button(sprite_sheet_start, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 5), 32, 0, 32, 13, (screen.get_width() / 4), (screen.get_height() / 5))

#   LOADING

sprite_sheet_loading = pygame.image.load(os.path.join(directory_loading, "loading.png")).convert_alpha()
sprite_sheet_bar_loading = pygame.image.load(os.path.join(directory_loading,"bar_loading.png")).convert_alpha()


#   GAME

# STORE
image_title_store = pygame.image.load(os.path.join(directory_title, "store.png")).convert_alpha()
#title_store = Title(image_title_store, 427, 80, 32, 0, 32, 15, 5)

#Control Loop
mainLoop = True
mainmenuLoop = True
loadingLoop = False
gameLoop = False
optionLoop = False
storeLoop = False

PLAY_MOUSE_POS = pygame.mouse.get_pos()

if __name__ == "__main__":
    while mainLoop:
        while mainmenuLoop:
            pygame.display.set_caption("BATTLE PLANE (MAIN MENU)")

            screen.fill([0, 255, 247])
            #color of display

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainmenuLoop = False
                    mainLoop = False
                    #close window

                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    #title
                    title_game = Title(image_title_game, (screen.get_width() / 2), (screen.get_height() / 5), 45, 0, 45, 27, (screen.get_width() / 3), (screen.get_height() / 3))
                    start_button = Button(sprite_sheet_start, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 5), 32, 0, 32, 13, (screen.get_width() / 4), (screen.get_height() / 5))

            if start_button.action:
                loadingLoop = True
                mainmenuLoop = False

            title_game.draw(screen)
            start_button.draw(screen) 

            pygame.display.update()
            #display update

        
        loading = Loading(sprite_sheet_loading, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 3), 83, 0, 83, 13, (screen.get_width() / 5), (screen.get_height() / 15), 4, 12, True)
        bar_loading = Loading(sprite_sheet_bar_loading, (screen.get_width() / 2), (screen.get_height() / 2), 32, 0, 32, 16, (screen.get_width() / 5), (screen.get_height() / 5), 8, 3, False)


        while loadingLoop:
            pygame.display.set_caption("BATTLE PLANE (LOADING)")     
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    loading = Loading(sprite_sheet_loading, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 3), 83, 0, 83, 13, (screen.get_width() / 5), (screen.get_height() / 15), 4, 12, True)
                    bar_loading = Loading(sprite_sheet_bar_loading, (screen.get_width() / 2), (screen.get_height() / 2), 32, 0, 32, 16, (screen.get_width() / 5), (screen.get_height() / 5), 8, 3, False)
            
            if(loading.exit_loading):
                screen.fill([0, 0, 0])
                loading.draw(screen)
                bar_loading.draw(screen)
            else:
                gameLoop = True
                loadingLoop = False
                
            pygame.display.update()
        
        while gameLoop:
            pygame.display.set_caption("BATTLE PLANE (GAME)")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    mainLoop = False

            screen.fill([255, 255, 255])

            pygame.display.update()

pygame.quit()
sys.exit()
