import pygame




def setup():
    """ The setup method for display and set mode, caption ..."""
    pygame.init()
    #win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Hulo Game")
    
    run()

def run():
    """ The main running function """
    win = pygame.display.set_mode((500, 500))
    x = 50
    y = 50
    width = 40
    height = 40
    vel = 15 # Velocity
    run = True
    while  run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel

        pygame.draw.rect(win, (255, 255, 0), (x, y, width, height))
        pygame.display.update()
    
    pygame.quit()
if __name__ == "__main__":
    setup()
