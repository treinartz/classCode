def setup():
    size(200, 200)


def draw():
    background(55)
    every_other("me3.jpg")


def every_other(image_path):
    img = load_image(image_path)
    new_image = create_image(img.width, img.height, RGB)

    # Get the pixels of the new image as a list
    pixel_list = new_image.pixels

    for x in range(img.width):  # across the columns
        for y in range(img.height):  # down the rows
            # get original pixel color
            orig_color = img.get_pixels(x, y)
            # get index position
            loc = x + y * width
            if x % 2 == 0:
                pixel_list[loc] = color(255)
            else:
                pixel_list[loc] = orig_color

    # Display the modified image
    image(new_image, 0, 0)

    image(new_image, 0, 0)
    save("output.jpg")
