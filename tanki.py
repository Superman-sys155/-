from pygame import *

window = display.set_mode((700,500))

background = transform.scale(image.load('Фон.jpg'), (700, 500))

font.init()
font_type = font.SysFont('Calibri', 30)

font_big = font.SysFont('Calibri', 50)

class Game_Sprite(sprite.Sprite):
    def __init__(self,name_image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(name_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Woll(sprite.Sprite):
    def __init__(self, x, y, width, height, color = (30, 127, 0)):
        super().__init__()
        self.color = color 
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def draw_woll(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(Game_Sprite):
    def __init__(self,name_image, x, y, size_x, size_y, speed, direction):
        super().__init__(name_image, x, y, size_x, size_y, speed)
        self.direction = direction
    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()
        elif self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x > 700:
                self.kill()
        elif self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.kill()
        elif self.direction == 'down':
            self.rect.y += self.speed
            if self.rect.y > 500:
                self.kill()

bullets = sprite.Group()
class Player(Game_Sprite):
    def __init__(self,name_image, x, y, size_x, size_y, speed):
        super().__init__(name_image, x, y, size_x, size_y, speed)
        self.images = {
            'up': transform.scale(image.load('tank1_up.png'),(size_x, size_y)),
            'right': transform.scale(image.load('tank1_right.png'),(size_y, size_x)),
            'left': transform.scale(image.load('tank1_left.png'),(size_y, size_x)),
            'down': transform.scale(image.load('tank1_down.png'),(size_x, size_y))
        }
        self.direction = 'up'
        self.lives = 7

    def update(self):
        keys = key.get_pressed()
        if self.rect.x > 5 and keys[K_a]:
            self.rect.x -= self.speed
            self.direction = 'left'
            if sprite.spritecollide(self, woller, False):
                self.rect.x += self.speed
        if self.rect.x < 630 and keys[K_d]:
            self.rect.x += self.speed
            self.direction = 'right'
            if sprite.spritecollide(self, woller, False):
                self.rect.x -= self.speed
        if self.rect.y < 430 and keys[K_s]:
            self.rect.y += self.speed
            self.direction = 'down'
            if sprite.spritecollide(self, woller, False):
                self.rect.y -= self.speed            
        if self.rect.y > 5 and keys[K_w]:
            self.rect.y -= self.speed
            self.direction = 'up'
            if sprite.spritecollide(self, woller, False):
                self.rect.y += self.speed          
        self.image = self.images[self.direction]
        x  = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def shot(self):
        direction = self.direction
        if self.direction == 'up':
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 10, 10, 8,direction) 
        if self.direction == 'right':
            bullet = Bullet('bullet.png', self.rect.x, self.rect.centery, 10, 10, 8,direction) 
        if self.direction == 'left':
            bullet = Bullet('bullet.png', self.rect.x, self.rect.centery, 10, 10, 8,direction) 
        if self.direction == 'down':
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 10, 10, 8,direction) 
        bullets.add(bullet)

bullets_2 = sprite.Group()
class Player_2(Game_Sprite):
    def __init__(self,name_image, x, y, size_x, size_y, speed):
        super().__init__(name_image, x, y, size_x, size_y, speed)
        self.images = {
            'up': transform.scale(image.load('tank2_up.png'),(size_x, size_y)),
            'right': transform.scale(image.load('tank2_right.png'),(size_y, size_x)),
            'left': transform.scale(image.load('tank2_left.png'),(size_y, size_x)),
            'down': transform.scale(image.load('tank2_down .png'),(size_x, size_y))
        }
        self.direction = 'up'
        self.lives = 7

    def update(self):
        keys = key.get_pressed()
        if self.rect.x > 5 and keys[K_LEFT]:
            self.rect.x -= self.speed
            self.direction = 'left'
            if sprite.spritecollide(self, woller, False):
                self.rect.x += self.speed            
        if self.rect.x < 630 and keys[K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 'right'
            if sprite.spritecollide(self, woller, False):
                self.rect.x -= self.speed            
        if self.rect.y < 430 and keys[K_DOWN]:
            self.rect.y += self.speed
            self.direction = 'down'
            if sprite.spritecollide(self, woller, False):
                self.rect.y -= self.speed            
        if self.rect.y > 5 and keys[K_UP]:
            self.rect.y -= self.speed
            self.direction = 'up'
            if sprite.spritecollide(self, woller, False):
                self.rect.y += self.speed     
        self.image = self.images[self.direction] 
        x  = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def shot(self):
        direction = self.direction
        if self.direction == 'up':
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 10, 10, 8,direction) 
        if self.direction == 'right':
            bullet = Bullet('bullet.png', self.rect.x, self.rect.centery, 10, 10, 8,direction) 
        if self.direction == 'left':
            bullet = Bullet('bullet.png', self.rect.x, self.rect.centery, 10, 10, 8,direction) 
        if self.direction == 'down':
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 10, 10, 8,direction) 
        bullets_2.add(bullet)

woll_1 = Woll(130, 179, 10, 319)
woll_2 = Woll(204, 179, 10, 319)
woll_3 = Woll(130, 179, 74, 10 )
woll_4 = Woll(223, 1, 10, 75)
woll_5 = Woll(111, 66, 112, 10)
woll_7 = Woll(390,1, 10, 229)
woll_8 = Woll(390,229, 150, 10 )
woll_9 = Woll(532, 1, 10, 238)
woll_10 = Woll(532, 330, 10, 330)
woll_11 = Woll(390, 330, 10, 362)
woll_12 = Woll(390, 330, 142, 10)


woller = sprite.Group()
woller.add(woll_1)
woller.add(woll_2)
woller.add(woll_3)
woller.add(woll_4)
woller.add(woll_5)
woller.add(woll_7)
woller.add(woll_8)
woller.add(woll_9)
woller.add(woll_10)
woller.add(woll_11)
woller.add(woll_12)

tank1 = Player('tank1_up.png', 50,400, 35, 60, 4)
tank2 = Player_2('tank2_up.png', 600,400, 35, 60, 4)

finish = False
game = True

clock = time.Clock()
FPS = 90

mixer.init()
mixer.music.load('миньены_прикол.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)

gav = mixer.Sound('monkey.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                tank1.shot()
        if e.type == MOUSEBUTTONDOWN:
            tank2.shot()

    
    if not finish:
        sprite.groupcollide(bullets,woller, True,  False)
        sprite.groupcollide(bullets_2, woller, True, False)

        if sprite.spritecollide(tank2, bullets, True):
            tank2.lives -= 1
            gav.play()

        if sprite.spritecollide(tank1, bullets_2, True):
            tank1.lives -= 1
            gav.play()
        
        window.blit(background, (0,0))
        bullets.draw(window)
        bullets.update()
        bullets_2.draw(window)
        bullets_2.update()
        lives_text1 = font_type.render(f'Lives_: {tank1.lives}', True, (136, 153, 56))
        lives_text2 = font_type.render(f'Lives_: {tank2.lives}', True, (118, 127, 96))
        window.blit(lives_text1, (10,10))
        window.blit(lives_text2, (570,10))
        tank1.draw()
        tank2.draw()
        woller.draw(window)
        tank1.update()
        tank2.update()
        if tank1.lives <= 0:
            win = font_big.render('Второй танк победил!', True, (56, 81, 237))
            window.blit(win, (150, 250))
            finish = True

        if tank2.lives <= 0:
            win = font_big.render('Первый танк победил!', True, (56, 81, 237))
            window.blit(win, (150, 250))
            finish = True

        display.update()
        clock.tick(FPS)