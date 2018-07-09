import pygame
import numpy as np
import population as P

# Control parameters
info = {"width":400, "height":300, "target":np.array([200,50]), "rcx":200, "rcy":150, "rw":200, "rh":20, 
         "screen": None, "loopcount":0, "maxcount":800}

# Pygame setup
pygame.init()
screen = pygame.display.set_mode([info["width"], info["height"] ])
info["screen"] = screen
pygame.display.set_caption("Smart rockets in python")
done = False
clock = pygame.time.Clock()

# Go
popul = P.Population(info)
gencount = 0

while not done :
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    clock.tick(30)
    screen.fill((75,75,75))

    # Simulation    
    popul.run()
    info["loopcount"] += 1
    if (info["loopcount"] == info["maxcount"]): 
        print("\nGeneration: ",gencount)
        gencount += 1
        popul.evaluate()
        popul.selection()
        info["loopcount"] = 0   
       
    # Draw target
    pygame.draw.circle(screen, (0,255,0), info["target"], 10)
    # Draw obstacle
    ltx = info["rcx"] - info["rw"]/2
    lty = info["rcy"] - info["rh"]/2 
    pygame.draw.rect(screen, (255,255,255), [ltx,lty,info["rw"],info["rh"] ])
    
    #Update drawing progress print
    pygame.display.flip()
    if info["loopcount"]%200 == 0:
        print("Frames: ",info["loopcount"])


pygame.quit()

