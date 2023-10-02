img=None

def setup():
    size(200, 200)
    global img
    img = load_image('stolaf5.jpg')
    no_loop()
  
def draw():
    # This code looks at every pixel in the image,
    # gets the color of the pixel and
    # calculates the new color based on our filter logic.
    img.load_pixels()
    for y in range(img.height):
        for x in range(img.width):

            # Gets the original color
            img_color = img.get_pixels(x, y)

            # Gets the filter color
            filter_color = get_filter_color(red(img_color), green(img_color), blue(img_color))

            # Draws a pixel with the filter color
            stroke(filter_color)
            point(x, y)

# This function is where the magic happens!
# It takes the original r, g, b, color
# and uses that to calculate a "filter" color.
def get_filter_color(r, gr, b):

    # Try using the r, g, b values to make a new color!
    # Some things to try:
    # xFilter = 255; (increase or decrease a specific color)
    # xFilter = 255 - x; (bright becomes dark, dark becomes bright)
    # xFilter = r; (rearrange r, g, b into a different order)

    r_filter = 55 - r+100
    g_filter = gr
    b_filter = b+100

    return color(r_filter, g_filter, b_filter)

