from pygame import *
import random

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("belit_phon.jpg"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image1), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed


ball = GameSprite('ball.jpg', 2, 90, 90, 53, 53)
platforma_r = Player('platform_2.png', 4, 0, 10, 23, 110 )
platforma_l = Player('platform_1.png', 4, 670, 10, 23, 110 )


clock = time.Clock()
FPS = 60
speed_x = 2
speed_y = 2

finish = False

font.init()
font_1 = font.Font(None, 35)
lose1 = font_1.render('PLAYER 1 LOSE!', True, (180,0,0))

font_2 = font.Font(None, 35)
lose2 = font_2.render('PLAYER 2 LOSE!', True, (180,0,0))

game = True 
while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(background,(0,0))
        platforma_r.reset()
        platforma_l.reset()
        platforma_r.update_r()
        platforma_l.update_l()
        ball.reset()

        ball.rect.y += speed_y
        ball.rect.x += speed_x
        
        if ball.rect.y  > 450 or ball.rect.y  < 0:
            speed_y *= -1
        if sprite.collide_rect(platforma_r, ball) or sprite.collide_rect(platforma_l, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose2, (200, 200))

        
            

    display.update()
    clock.tick(FPS)
