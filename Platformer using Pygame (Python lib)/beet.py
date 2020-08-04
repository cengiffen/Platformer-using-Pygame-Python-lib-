import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Beet Eater')

clock = pygame.time.Clock()


background_song = pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1)
chew_sound = pygame.mixer.Sound('sounds/chews.wav')
vomit_sound = pygame.mixer.Sound('sounds/vomit.wav')


class BeetRoot:
    beet_draw = pygame.image.load('img/beetroot.png')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picture = pygame.transform.scale(self.beet_draw, (self.width, self.height))
        self.visible = True

    def draw(self, screen):
        if self.visible:
            screen.blit(self.picture, (self.x, self.y))

    def eaten(self):
        self.visible = False


class Mushroom:
    mushroom_draw = pygame.image.load('img/mushroom.jpg')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picture = pygame.transform.scale(self.mushroom_draw, (self.width, self.height))
        self.visible = True

    def draw(self, screen):
        if self.visible:
            screen.blit(self.picture, (self.x, self.y))

    def eaten(self):
        self.visible = False


class Platform:
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))


class Krisjim:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.jumping = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.health = 2
        self.score = 0

    def draw(self, screen):
        if self.left:
            screen.blit(eat_left_SMALL, (self.x, self.y))
        elif self.right:
            screen.blit(eat_right_SMALL, (self.x, self.y))
        else:
            screen.blit(char_SMALL, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 20, 75, 10))
        pygame.draw.rect(screen, (0, 128, 0), (self.x, self.y - 20, int((self.health * 37.5)), 10))

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            font1 = pygame.font.SysFont('comicsans', 200, True)
            text = font1.render('DED LOL', 1, (255, 0, 0))
            self.jumping = False
            screen.blit(text, (400 - int((text.get_width() / 2)), 350))
            pygame.display.update()
            i = 0
            while i < 300:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
            self.x = 100
            self.y = 630
            self.jumping = False
            self.health = 3
            self.score -= 5

    def win(self):
        font1 = pygame.font.SysFont('comicsans', 120, True)
        text = font1.render('TOO MUCH BEET', 1, (255, 0, 0))
        screen.blit(text, (400 - int((text.get_width() / 2)), 350))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


def redraw():
    screen.blit(bg, (0, 0))
    text = font.render('Score: ' + str(kris.score), 1, (0, 0, 0))
    screen.blit(text, (680, 10))
    kris.draw(screen)
    for root in beetroots:
        root.draw(screen)
    for room in mushrooms:
        room.draw(screen)

    platform1.draw(screen)
    platform2.draw(screen)
    platform3.draw(screen)

    pygame.display.update()


play = True
font = pygame.font.SysFont('comicsans', 30, True)

kris = Krisjim(100, 630, 70, 140)
beetroot = BeetRoot(500, 630, 80, 80)
beetroot2 = BeetRoot(700, 630, 80, 80)
beetroot3 = BeetRoot(100, 480, 80, 80)
beetroot4 = BeetRoot(500, 480, 80, 80)
beetroot5 = BeetRoot(700, 480, 80, 80)
beetroot6 = BeetRoot(100, 250, 80, 80)
beetroot7 = BeetRoot(300, 250, 80, 80)
beetroot8 = BeetRoot(500, 250, 80, 80)
beetroot9 = BeetRoot(300, 50, 80, 80)
beetroot10 = BeetRoot(700, 50, 80, 80)
beetroot11 = BeetRoot(500, 50, 80, 80)
beetroots = [beetroot, beetroot2, beetroot3, beetroot4, beetroot5, beetroot6, beetroot7, beetroot8, beetroot9,
             beetroot10, beetroot11]
mushroom = Mushroom(300, 630, 80, 80)
mushroom2 = Mushroom(300, 480, 80, 80)
mushroom3 = Mushroom(600, 250, 80, 80)
mushroom4 = Mushroom(100, 50, 80, 80)
mushroom5 = Mushroom(400, 50, 80, 80)
mushroom6 = Mushroom(600, 480, 80, 80)
mushroom7 = Mushroom(200, 250, 80, 80)
mushroom8 = Mushroom(700, 250, 80, 80)
mushroom9 = Mushroom(600, 50, 80, 80)
mushroom10 = Mushroom(400, 250, 80, 80)
mushrooms = [mushroom, mushroom2, mushroom3, mushroom4, mushroom5, mushroom6, mushroom7, mushroom8, mushroom9, mushroom10]
platform1 = Platform((255, 0, 127), 0, 580, 800, 20)
platform2 = Platform((178, 102, 255), 0, 380, 800, 20)
platform3 = Platform((178, 255, 102), 0, 180, 800, 20)

bg = pygame.image.load('img/bg.png')
eat_left = pygame.image.load('img/eat_left.png')
eat_left_SMALL = pygame.transform.scale(eat_left, (kris.width, kris.height))
eat_right = pygame.image.load('img/eat_right.png')
eat_right_SMALL = pygame.transform.scale(eat_right, (kris.width, kris.height))
char = pygame.image.load('img/char.png')
char_SMALL = pygame.transform.scale(char, (kris.width, kris.height))

going_down = 0

while play:
    clock.tick(64)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    if going_down > 0:
        going_down += 1
    if going_down > 8:
        going_down = 0

    for root in beetroots:
        if root.visible:
            if root.x < kris.x + (kris.width / 2) < root.x + root.width and root.y + root.height > kris.y + (
                    kris.height / 2) > root.y:
                root.eaten()
                kris.score += 1
                if kris.score == 11:
                    kris.win()
                chew_sound.play()

    for room in mushrooms:
        if room.visible:
            if room.x < kris.x + (kris.width / 2) < room.x + room.width and room.y + room.height > kris.y + (
                    kris.height / 2) > room.y:
                room.eaten()
                kris.hit()
                vomit_sound.play()

    if kris.jumping and kris.jumpCount < 0:
        if kris.y + kris.height < platform3.y:
            kris.jumping = False
            kris.jumpCount = 8
            kris.y = platform3.y - kris.height
        elif kris.y + kris.height < platform2.y:
            kris.jumping = False
            kris.jumpCount = 8
            kris.y = platform2.y - kris.height
        elif kris.y + kris.height < platform1.y:
            kris.jumping = False
            kris.jumpCount = 8
            kris.y = platform1.y - kris.height

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and kris.x - kris.vel > 0:
        kris.x -= kris.vel
        kris.left = True
        kris.right = False
    if keys[pygame.K_RIGHT] and kris.x + kris.width + kris.vel < 800:
        kris.x += kris.vel
        kris.left = False
        kris.right = True
    if not kris.jumping:
        if keys[pygame.K_SPACE]:
            kris.jumping = True
            kris.left = False
            kris.right = False
        elif keys[pygame.K_DOWN] and going_down == 0:
            if kris.y == platform3.y - kris.height:
                kris.y = platform2.y - kris.height
            elif kris.y == platform2.y - kris.height:
                kris.y = platform1.y - kris.height
            elif kris.y == platform1.y - kris.height:
                kris.y = 630
            going_down = 1

    else:
        if kris.jumpCount >= -8:
            kris.y -= kris.jumpCount * abs(kris.jumpCount)
            kris.jumpCount -= 1
        else:
            kris.jumpCount = 8
            kris.jumping = False

    redraw()

pygame.quit()
