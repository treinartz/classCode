def setup():
    size(200, 200)
    grayscale("me3.jpg")


def grayscale(image_path):
    # load the image
    img = load_image(image_path)
    # get the pixels as a list
    pixel_list = img.pixels
    for x in range(img.width):
        for y in range(img.height):
            # get each pixel
            loc = img.get_pixels(x, y)
            # change value to gray
            gray = int(0.3 * red(loc) + 0.6 * green(loc) + 0.11 * blue(loc))
            new_color = color(gray, gray, gray)
            index = x + y * img.width
            # assign gray to each pixel
            pixel_list[index] = new_color
    # display the image
    image(img, 0, 0)
    # Save the modified image to a new file
    save("output2.jpg")
