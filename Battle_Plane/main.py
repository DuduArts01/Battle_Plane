import pygame
from title import Title
from button import Button
from loading import Loading
from pilot import Pilot
import os
from time import sleep


pygame.init()

width_window = 854
hight_window = 480

screen = pygame.display.set_mode([width_window, hight_window])
#dimension display

pygame.display.set_caption("Battle Plane")
#name of game in display

#directory Main
directory_main = os.path.dirname(__file__)

#directory Title
directory_title = os.path.join(directory_main, "image/title")

#directory Buttons
directory_button = os.path.join(directory_main, "image/button")

#directory Pilot
directory_pilot = os.path.join(directory_main, "image/pilot")

#   MAIN MENU
#Title
image_title_game = pygame.image.load(os.path.join(directory_title, "name_game.png")).convert_alpha()
title_game = Title(image_title_game, 427, 90, 45, 0, 45, 27, 6)

#Button Start
sprite_sheet_start = pygame.image.load(os.path.join(directory_button, "start/start.png")).convert_alpha()
start_button = Button(sprite_sheet_start, 427, 350, 32, 0, 32, 13, 6)

#Button Store
sprite_sheet_store = pygame.image.load(os.path.join(directory_button, "store/store.png")).convert_alpha()
store_button = Button(sprite_sheet_store, 60, 250, 31, 0, 31, 32, 2)

#   LOADING
#directory Loading
directory_loading = os.path.join(directory_main, "image/loading")

sprite_sheet_loading = pygame.image.load(os.path.join(directory_loading, "loading.png")).convert_alpha()
sprite_sheet_bar_loading = pygame.image.load(os.path.join(directory_loading,"bar_loading.png")).convert_alpha()

loading = Loading(sprite_sheet_loading, 440, 300, 83, 0, 83, 13, 2, 4, 12, True)
bar_loading = Loading(sprite_sheet_bar_loading, 427, 240, 32, 0, 32, 16, 4, 8, 3, False)

#   GAME
pilot_sprite_sheet = pygame.image.load(os.path.join(directory_pilot, "pilot.png")).convert_alpha()
pilot = Pilot(pilot_sprite_sheet, 0, 0, 26, 51, 28, 52, 2, 12, 24)

# STORE
image_title_store = pygame.image.load(os.path.join(directory_title, "store.png")).convert_alpha()
title_store = Title(image_title_store, 427, 80, 32, 0, 32, 15, 5)

#Control Loop
mainLoop = True
mainmenuLoop = True
loadingLoop = False
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
                loadingLoop = True
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
            title_game.draw(screen)

            

            pygame.display.update()
            #display update

        while loadingLoop:
            pygame.display.set_caption("Battle Plane (Loading)")     
            if(loading.exit_loading):
                screen.fill([0, 0, 0])
                loading.draw(screen)
                bar_loading.draw(screen)
            else:
                gameLoop = True
                loadingLoop = False
                
            pygame.display.update()
        
        while gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    mainLoop = False
                    
            screen.fill([255, 255, 255])
            
            pilot_draw(screen)
            
            pygame.display.update()
            
        while storeLoop:
            pygame.display.set_caption("Battle Plane (Store)")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    storeLoop = False
                    mainLoop = False

            screen.fill([41, 21, 8])
            
            title_store.draw(screen)
            
            pygame.display.update()

pygame.quit()
