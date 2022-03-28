import pygame as pg
import random

pg.init()
WIDTH, HEIGHT = 330, 175
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Insertion Sort Visualization')

def button_setup():
    rect = []
    rect.append([pg.Rect(15, 100, 90, 50), 'Run'])
    rect.append([pg.Rect(115, 100, 90, 50), 'Random'])
    rect.append([pg.Rect(215, 100, 90, 50), 'Step'])
    return rect

def create(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0,99))
    return arr

def compare(arr, left, right):
    return arr[left] >= arr[right]

def draw(window, arr, index, cur):
    window.fill((255, 255, 255))
    font = pg.font.SysFont('Arial', 20)
    x, y, s = 15, 30, 30
    
    for i in range(len(arr)):
        if index >= len(arr):
            ts = font.render(str(arr[i]), True, (0, 0, 0))
        elif i <= cur and i != index:
            ts = font.render(str(arr[i]), True, (0, 180, 0))
        elif i == index:
            ts = font.render(str(arr[i]), True, (180, 0, 0))
        else:
            ts = font.render(str(arr[i]), True, (0, 0, 0))
        
        if i == index:
            window.blit(ts, (x + s*i, y+y))
        else:
            window.blit(ts, (x + s*i, y))

def draw_button(window, rect, run):
    font = pg.font.SysFont('Arial', 20)
    
    for r in rect:
        pg.draw.rect(window, (0, 0, 0), r[0], 3)
        if run and r[1] == 'Step':
            ts = font.render('Stop', True, (0, 0, 0))
            window.blit(ts, (r[0].x+15, r[0].y+15))
        else:
            ts = font.render(r[1], True, (0, 0, 0))
            window.blit(ts, (r[0].x+15, r[0].y+15))

def swap(arr, left, right):
    return arr[right], arr[left]

def step(arr, index, cur, run):
    if 0 < index < len(arr):
        if compare(arr, index-1, index):
            arr[index], arr[index-1] = swap(arr, index, index-1)
            index -= 1
        else:
            cur += 1
            index = cur
    elif index >= len(arr):
        run = False
    else:
        cur += 1
        index = cur
    return arr, index, cur, run
    
def main(window):
    running = True
    clock = pg.time.Clock()
    frame, fps = 0, 60
    SIZE = 10
    arr = create(SIZE)
    index, cur = SIZE, SIZE
    rect = button_setup()
    run = False

    while running:
        clock.tick(fps)
        x, y = pg.mouse.get_pos()

        draw(window, arr, index, cur)
        draw_button(window, rect, run)

        if run:
            if frame >= fps:
                arr, index, cur, run = step(arr, index, cur, run)
                frame = 0
            else:
                frame += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect[0][0].collidepoint(x, y):
                    run = True
                    frame, index, cur = 0, 0, 0
                if rect[1][0].collidepoint(x, y):
                    arr = create(SIZE)
                    run = False
                    frame, index, cur = 0, SIZE, SIZE
                if rect[2][0].collidepoint(x, y):
                    if run:
                        run = False
                    else:
                        arr, index, cur, run = step(arr, index, cur, run)

        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main(window)