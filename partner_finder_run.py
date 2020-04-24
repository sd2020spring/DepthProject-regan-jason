"""
Main file to put the running code (since I can't keep track of everything)
"""
import partner_finder_final
import partner_finder_controller
import partner_finder_view

running = True
while running
    player = Player(0,0,playerimage)
    player.draw()
    speedx = 0
    speedy = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            speedy += -1
            speedx = 0
        elif event.type == pygame.K_UP:
            speedy += 1
            speedx = 0
        elif event.type == pygame.K_RIGHT:
            speedx += 1
            speedy = 0
        elif event.type == pygame.K_LEFT:
            speedx += -1
            speedy = 0
        elif event.type == pygame.INTERACT:
            pass
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    player.move(speedx, speedy)
    player.draw()
