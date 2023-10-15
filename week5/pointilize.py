pointillize = 10


def setup():
    size(200, 200)
    background(255)


def draw():
    global img
    img = load_image("me3.jpg")
    # Pick a random point
    x = int(random(img.width))
    y = int(random(img.height))
    loc = x + y * img.width

    # Look up the RGB color in the source image
    r = red(img.pixels[loc])
    gr = green(img.pixels[loc])
    b = blue(img.pixels[loc])
    no_stroke()

    # Instead of setting a pixel, we use the color
    # from a pixel to draw a circle.
    fill(r, gr, b, 100)
    ellipse(x, y, pointillize, pointillize)
