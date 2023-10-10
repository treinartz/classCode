
def setup():
    size(200, 200)

def draw():
    background(55)
    get_filter_color("me3.jpg")
    
# This function is where the magic happens!
# It takes the original r, g, b, color
# and uses that to calculate a "filter" color.
def get_filter_color(image_path):
    # load the image
    img = load_image(image_path)
    # get the pixels as a list
    pixel_list = img.pixels
    for y in range(img.height):
        for x in range(img.width):
            # Gets the original color
            img_color = img.get_pixels(x, y)

            # Try using the r, g, b values to make a new color!
            # Some things to try:
            # xFilter = 255; (increase or decrease a specific color)
            # xFilter = 255 - x; (bright becomes dark, dark becomes bright)
            # xFilter = r; (rearrange r, g, b into a different order)

            r_filter = 55 - red(img_color) + 100
            g_filter = green(img_color)
            b_filter = blue(img_color) + 100

            new_color = color(r_filter, g_filter, b_filter)
            index = x + y * img.width
            # assign gray to each pixel
            pixel_list[index] = new_color
    # display the image
    image(img, 0, 0)
    # Save the modified image to a new file
    save("output2.jpg")

