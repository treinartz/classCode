def setup():
    size(400, 400)
    img = load_image("me3.jpg")
    img.load_pixels()
    pixel = img.pixels
    for i in range(len(pixel)):
        c = pixel[i]
        gray = int(red(c) * 0.3 + green(c) * 0.59 + blue(c) * 0.11)
        pixel[i] = color(gray, gray, gray)
    img.update_pixels()
    image(img, 0, 0)
    #print(len(img.pixels))
    #print(pixel[200])
    grayscale("me3.jpg")


def grayscale(image_path):
    push()
    translate(200, 0)
    # Load the image
    imag = load_image(image_path)
    # Get the pixels of the image as a list
    pixel = imag.pixels
    # Loop through each pixel in the image
    for x in range(3):
        for y in range(3):
            # Get the color of the current pixel
            c = imag.get_pixels(x, y)
            # Convert the color to grayscale
            color_mode(RGB)
            grey = int(0.299 * red(c) + 0.587 * green(c) + 0.114 * blue(c))
            new_color = color(grey, grey, grey)
            # Set the modified color in the new image
            index = x + y * imag.width
            #print(index)
            pixel[index] = new_color
    # Update the pixels in the new image
    imag.update_pixels()
    image(imag, 0, 0)
    pop()


def grayscale2(image_path):
    push()
    translate(200, 0)
    # Load the image
    imag = load_image(image_path)

    # Create a new image with the same dimensions as the original
    new_image = create_image(imag.width, imag.height, RGB)

    # Get the pixels of the new image as a list
    pixel = new_image.pixels

    # Loop through each pixel in the image
    for x in range(imag.width):
        for y in range(imag.height):
            # Get the color of the current pixel
            c = imag.get(x, y)

            # Convert the color to grayscale
            color_mode(RGB)
            grey = int(0.299 * red(c) + 0.587 * green(c) + 0.114 * blue(c))
            new_color = color(grey, grey, grey)

            # Set the modified color in the new image
            index = x + y * imag.width
            pixel[index] = new_color

    # Update the pixels in the new image
    new_image.update_pixels()

    # Display the modified image
    image(new_image, 0, 0)

    pop()
