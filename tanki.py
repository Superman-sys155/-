from pygame import *

window = display.set_mode((700,500))

background = transform.scale(image.load('Фон.jpg'), (700, 500))

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

class Player(Game_Sprite):
    def update(self):
        keys = key.get_pressed()
        if self.rect.x > 5 and keys[K_a]:
            self.rect.x -= self.speed
        if self.rect.x < 620 and keys[K_d]:
            self.rect.x += self.speed
        if self.rect.y < 420 and keys[K_s]:
            self.rect.y += self.speed
        if self.rect.y > 5 and keys[K_w]:
            self.rect.y -= self.speed

class Player_2(Game_Sprite):
    def update(self):
        keys = key.get_pressed()
        if self.rect.x > 5 and keys[K_LEFT]:
            self.rect.x -= self.speed
        if self.rect.x < 620 and keys[K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.y < 420 and keys[K_DOWN]:
            self.rect.y += self.speed
        if self.rect.y > 5 and keys[K_UP]:
            self.rect.y -= self.speed

tank1 = Player('tank1.png', 50,400, 50, 70, 4)
tank2 = Player_2('tank2.png', 600,400, 70, 70, 4)

finish = False
game = True

clock = time.Clock()
FPS = 90

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))
    tank1.draw()
    tank2.draw()
    tank1.update()
    tank2.update()
    display.update()
    clock.tick(FPS)