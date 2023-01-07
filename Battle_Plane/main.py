import pygame
from start import Start
from option import Option

pygame.init()

display = pygame.display.set_mode([1366, 768])
#dimension display

pygame.display.set_caption("Battle_Plane")
#name of game in display

#Object
buttonGroup = pygame.sprite.Group() 

button_Start = Start(buttonGroup)
button_Start.image = pygame.transform.scale(button_Start.image, [300, 100])
button_Start.rect = pygame.Rect(530, 430, 300, 100)
button_Start.center = (530, 430)

button_Option = Option(buttonGroup)
button_Option.image = pygame.transform.scale(button_Option.image, [200, 70])
button_Option.rect = pygame.Rect(583, 545, 200, 70)
button_Option.center = (583, 545)

gameLoop = True
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                #close window

        display.fill([43, 163, 39])
        #color of display
        buttonGroup.draw(display)

        buttonGroup.update()


        pygame.display.update()
        #display update
