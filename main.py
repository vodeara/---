from pygame import *


window = display.set_mode((700, 500))
display.set_caption('Пинг - понг')
color_fon = (215, 123, 0)
background = transform.scale(image.load('gg.webp'), (700,500))

font.init()
font1 = font.Font(None, 100)

speed_x = 3
speed_y = 3

clock = time.Clock()
finish = False
game = True
FPS = 60
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w]  and self.rect.y > 20:
            self.rect.y -= self.speed

        if keys_pressed[K_s]  and self.rect.y < 480:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()

        if  keys_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed

        if  keys_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if finish == False:   
            window.fill(color_fon)
            ball.reset()
            player1.reset()
            player1.update_l()
            player2.reset()
            player2.update_r()
        if ball_x <= 0:
            lose = font2.render('LEFT LOSE', True, (215, 215, 23))
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if ball.rect.y >= 450 or ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x <= 0:
            lose = font1.render('LEFT LOSE', True, (215, 215, 23))
            finish = True
            window.blit(lose, (200,200))
        if ball_x >= 500:
            lose = font2.render('RIGHT LOSE', True, (215, 215, 23))
        if ball.rect.x >= 700:
            lose = font1.render('RIGHT LOSE', True, (215, 215, 23))
            finish = True
            window.blit(lose, (200,200))

player1 = Player('i.webp', 5, 275, 25, 100, 5)
player2 = Player('i.webp', 690, 275, 25, 100, 5)
ball = GameSprite('eww.png', 200, 200, 50, 50, 5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish == False:   
        window.fill(color_fon)
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
    



    display.update()
    clock.tick(FPS)




   


        
        
    
    display.update()
    clock.tick(FPS)
