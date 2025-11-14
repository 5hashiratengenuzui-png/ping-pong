from pygame import *
calor = (0, 255, 204)
window = display.set_mode((700, 500))
window.fill(calor)
speed_x = 5
speed_y = 5
clock = time.Clock()
font.init()
text = font.SysFont('Arial', 40)
fail_l = text.render('Left FAILIURE', True, (255, 0, 0))
fail_r = text.render('Right FAILIURE', True, (255, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_hight, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 150:
            self.rect.y += self.speed

racket_l = Player('racket (1).png', 5, 350, 7, 150, 20)
racket_r = Player('racket (1).png', 675, 350, 7, 150, 20)
ball = GameSprite('tenis_ball (1).png', 350, 250, 1, 50, 50)

game = True
finish = False
while game:
    if finish != True:
        window.fill(calor)
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(fail_l, (200, 200))
            finish = True
        if ball.rect.x > 650:
            window.blit(fail_r, (200, 200))
            finish = True
        racket_l.update_l()
        racket_l.reset()
        racket_r.update_r()
        racket_r.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)