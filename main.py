from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load("background.png"), (700, 500))

x1 = 130
y1 = 100
x2 = 400
y2 = 350

Blu = transform.scale(image.load('Blu.png'), (100, 100))
Red = transform.scale(image.load('RED.png'), (100, 100))

clock = time.Clock()
FPS = 60


game = True


while game:
    clock.tick(FPS)
    window.blit(background, (0, 0))
    window.blit(Blu, (x1, y1))
    window.blit(Red, (x2, y2))



    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP]:
        y2 -= 5
    if keys_pressed[K_DOWN]:
        y2 += 5
    if keys_pressed[K_RIGHT]:
        x2 += 5
    if keys_pressed[K_LEFT]:
        x2 -= 5
    if keys_pressed[K_s] and y2 < 395:
        y1 += 5
    if keys_pressed[K_w] and y2 < 395:
        y1 -= 5
    if keys_pressed[K_d] and y2 < 395:
        x1 += 5
    if keys_pressed[K_a] and y2 < 395:
        x1 -= 5

    display.update()





