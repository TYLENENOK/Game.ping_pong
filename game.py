from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг понг')
 
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Rackets(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

background = transform.scale(image.load('Фон2.jpg'), (700,500))

racket1 = Rackets('ракетка левая.png',30,200,15,40,100)
racket2 = Rackets('ракетка правая.png',630,200,15,40,100)

ball = GameSprite('теннисный мяч.png',320,230,25,50,50)

FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    racket1.update_l()
    racket2.update_r()
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    time.delay(FPS)

    