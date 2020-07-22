import pygame
import datetime
import time

#Variables
HEIGHT = 600
WIDTH = 1200
BORDER = 20
VELOCITY = 1
FRAMERATE = 1000000000

class Ball:
    RADIUS = 20
    def __init__(self, screen, x, y, vx, vy):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        pygame.draw.circle(self.screen, colour, (self.x, self.y), self.RADIUS)

    def update(self, bgColor, fgColor, paddle):
        self.show(bgColor)
        if self.x > WIDTH:
            return
        new_x = self.x + self.vx
        new_y = self.y + self.vy
        if new_x - self.RADIUS < BORDER:
            self.vx = -self.vx
        if (new_y - self.RADIUS) < BORDER or ((new_y + self.RADIUS) > (HEIGHT - BORDER)):
            self.vy = -self.vy
        elif (abs(paddle.y - self.y) < (Paddle.HEIGHT //2) + self.RADIUS) and ((new_x + self.RADIUS) > (WIDTH - Paddle.WIDTH)):
            self.vx = -self.vx
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(fgColor)

class Paddle:
    WIDTH = 15
    HEIGHT = 80

    def __init__(self, screen, y):
        self.screen = screen
        self.y = y

    def show(self,color):
        pygame.draw.rect(self.screen, color, pygame.Rect((WIDTH - self.WIDTH, self.y - (self.HEIGHT//2)), (self.WIDTH, self.HEIGHT)))

    def update(self, bgColor, fgColor):
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fgColor)

def main():
    print('Inside Main.')
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('PingPong')
    fgColor = pygame.Color('green')
    bgColor = pygame.Color('black')
    pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (WIDTH - Paddle.WIDTH, BORDER)))
    pygame.draw.rect(screen, fgColor , pygame.Rect((0, 0), (BORDER, HEIGHT)))
    pygame.draw.rect(screen, fgColor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH - Paddle.WIDTH, BORDER)))

    ballPLay = Ball(screen, WIDTH - Paddle.WIDTH - Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)
    ballPLay.show(fgColor)
    paddle = Paddle(screen, HEIGHT//2)
    paddle.show(fgColor)

    clock = pygame.time.Clock()
    game_ended = False
    start_time = datetime.datetime.now().replace(microsecond=0)
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
           break
        clock.tick(FRAMERATE)
        pygame.display.flip()
        if game_ended:
            continue
        ballPLay.update(bgColor, fgColor, paddle)
        paddle.update(bgColor, fgColor)
        if ballPLay.x > WIDTH:
            end_time = datetime.datetime.now().replace(microsecond=0)
            play_time = end_time - start_time
            play_time_str = datetime.time(0, 0, play_time.seconds).strftime("%M:%S")
            game_ended = True
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Game Ended ' + play_time_str, True, fgColor, bgColor)
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(text, textRect)

    pygame.quit()

if __name__ == '__main__':
    main()