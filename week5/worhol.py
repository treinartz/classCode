
def setup():
    size(400, 400)


def draw():
    background(55)
    andy_warhol("stolaf5.jpg")

def andy_warhol(image_path):
    # Load the image
    img = load_image(image_path)

    # Call load_pixels() to access the pixel data of the image
    img.load_pixels()

    # Create four new images with the same dimensions as the original
    img1 = create_image(img.width, img.height, RGB)
    img2 = create_image(img.width, img.height, RGB)
    img3 = create_image(img.width, img.height, RGB)
    img4 = create_image(img.width, img.height, RGB)

    # Get the pixels of the original image as a list
    pixel = img.pixels

    # Get the pixels of the new images as lists
    pixel1 = img1.pixels
    pixel2 = img2.pixels
    pixel3 = img3.pixels
    pixel4 = img4.pixels

    # Loop through each pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            # Get the color of the current pixel
            c = pixel[x + y * img.width]

            # Set the background to black
            pixel1[x + y * img.width] = color(22)

            # Apply thresholding to create a black, gray, and white region--upper left
            if brightness(c) > 100:
                pixel1[x + y * img.width] = color(125, 154, 225, 100)
            elif brightness(c) > 20:
                pixel1[x + y * img.width] = color(128)
            else:
                pixel1[x + y * img.width] = color(200, 20, 200)

            # Apply thresholding to create a red, green, and blue region--upper right
            if red(c) > 28 and green(c) < 28 and blue(c) < 28:
                pixel2[x + y * img.width] = color(255, 0, 0)
            elif red(c) < 28 and green(c) > 128 and blue(c) < 128:
                pixel2[x + y * img.width] = color(0, 255, 0)
            elif red(c) < 28 and green(c) < 28 and blue(c) > 128:
                pixel2[x + y * img.width] = color(0, 0, 255)

            # Apply thresholding to create a bright red region--lower left
            if 50 < x < 200 and 50 < y < 300 and red(c) > 128:
                pixel3[x + y * img.width] = color(255, 0, 255)
            else:
                pixel3[x + y * img.width] = c

            # Apply thresholding to create a black, gray, and white region--lower right
            if brightness(c) > 200:
                pixel4[x + y * img.width] = color(255, 0, 0)
            elif brightness(c) > 100:
                pixel4[x + y * img.width] = color(228)
            else:
                pixel4[x + y * img.width] = c

    # Call update_pixels() to apply the pixel data changes to the images
    img1.update_pixels()
    img2.update_pixels()
    img3.update_pixels()
    img4.update_pixels()

    # Display the four new images side-by-side
    image(img1, 0, 0)
    image(img2, img.width, 0)
    image(img3, 0, img.height)
    image(img4, img.width, img.height)


    save("final_output2.jpg")
