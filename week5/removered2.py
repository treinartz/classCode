def setup():
    size(200, 200)


def draw():
    background(55)
    remove_red("me3.jpg")

def remove_red(image_path):
    # Load the image
    img = load_image(image_path)

    # Create a new image with the same dimensions as the original
    new_image = create_image(img.width, img.height, RGB)

    # Get the pixels of the new image as a list
    pixel_list = new_image.pixels

    # Loop through each pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            # Get the color of the current pixel
            loc = img.get_pixels(x, y)

            # Remove the red component of the color
            color_mode(RGB)
            r, gr, b = red(loc), green(loc), blue(loc)
            new_color = color(0, gr, b)

            # Set the modified color in the new image
            index = x + y * img.width
            pixel_list[index] = new_color

    image(new_image, 0, 0)

    # Save the modified image to a new file
    save("output.jpg")