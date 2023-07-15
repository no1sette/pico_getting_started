from picounicorn import PicoUnicorn
import utime,urandom, time


picounicorn = PicoUnicorn()

#imports the height and with
w = picounicorn.get_width()
h = picounicorn.get_height()

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q
    
def lightup():
        #sets random location on board
        x = urandom.randint(0,w-1)
        y = urandom.randint(0,h-1)
        #sets random brightness for each R G B
        r = urandom.randint(0,50)
        g = urandom.randint(0,50)
        b = urandom.randint(0,50)
        #sets board color with previous setup
        picounicorn.set_pixel(x,y,r,g,b)
        utime.sleep(0.01)
    
def clear():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)
def rainbow():
        t = time.ticks_ms() / 3600
        for x in range(w):
            for y in range(h):
                r, g, b = [int(c * 50) for c in hsv_to_rgb(t + ((x + y) / w / 4), 1.0, 1.0)]
                picounicorn.set_pixel(x, y, r, g, b)
        time.sleep(1.0 / 60)
    
while True:
    if picounicorn.is_pressed(picounicorn.BUTTON_A) or picounicorn.is_pressed(picounicorn.BUTTON_Y):
        clear()
        while not (picounicorn.is_pressed(picounicorn.BUTTON_X) or picounicorn.is_pressed(picounicorn.BUTTON_B)):
            lightup()
    elif picounicorn.is_pressed(picounicorn.BUTTON_B) or picounicorn.is_pressed(picounicorn.BUTTON_X):
        clear()
        while not (picounicorn.is_pressed(picounicorn.BUTTON_A) or picounicorn.is_pressed(picounicorn.BUTTON_Y)):
            rainbow()

        