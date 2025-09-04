from pygame import *
font.init()

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

font_l = font.Font(None, 60)
lose1 = font_l.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font_l.render('PLAYER 2 LOSE!', True, (180,0,0))

racket1 = Rackets('ракетка левая.png',30,200,15,40,100)
racket2 = Rackets('ракетка правая.png',630,200,15,40,100)

ball = GameSprite('теннисный мяч.png',320,230,25,50,50)

speed_x = 7
speed_y = 7

FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 445 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 65:
            finish = True
            window.blit(lose1, (180, 230))
        if ball.rect.x > 590:
            finish = True
            window.blit(lose2, (180,230))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    time.delay(FPS)


    
