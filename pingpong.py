from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

background = (200, 255, 255)
win_height = 700
win_wight = 500
player_l = Player('raketka.png', 30, 200, 4, 50, 150)
player_r = Player('raketka.png', 30, 200, 4, 50, 150)
ball = GameSprite('tennisballpng.jpg', 200, 200, 4, 50, 50)
window = display.set_mode((win_height, win_wight))
window.fill(background)
display.set_caption('пинг понг')
game = True
finish = False
clock = time.Clock()
FPS = 60
while game:    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if not finish:
        player_l.update_l()
        player_l.reset()
        player_r.update_r()
        player_r.reset()
        ball.update()
        ball.reset()
        window.blit(background, (0, 0))
    display.update()
    clock.tick(FPS)