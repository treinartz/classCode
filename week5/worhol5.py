def setup():
    size(400, 400)


def draw():
    background(55)
    andy_warhol("me3.jpg")


def andy_warhol(image_path):
    # Load the image
    img = load_image(image_path)

    # Get the pixels of the original image as a list
    pixel_list = img.pixels

    # Create four new images with the same dimensions as the original
    img1 = create_image(img.width, img.height, RGB)
    img2 = create_image(img.width, img.height, RGB)
    img3 = create_image(img.width, img.height, RGB)
    img4 = create_image(img.width, img.height, RGB)

    # Get the pixels of the 4 new images as lists
    picture1 = img1.pixels
    picture2 = img2.pixels
    picture3 = img3.pixels
    picture4 = img4.pixels

    # Loop through each pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            # Get the color of the current pixel
            loc = pixel_list[x + y * img.width] #get the value at each pixel index position, and store store in "loc"


            # 1--Apply thresholding to create a black, gray, and white region--upper left
            if brightness(loc) > 140:
                picture1[x + y * img.width] = color(25, 114, 105, 80)
            elif brightness(loc) > 30:
                picture1[x + y * img.width] = color(60)
            else:
                picture1[x + y * img.width] = color(100, 20, 100)

            # 2--Apply thresholding to create a red, green, and blue region--upper right
            if red(loc) > 128 and green(loc) < 128 and blue(loc) < 128:
                picture2[x + y * img.width] = color(255, 0, 0)
            elif red(loc) < 128 and green(loc) > 128 and blue(loc) < 128:
                picture2[x + y * img.width] = color(0, 255, 0)
            elif red(loc) < 1128 and green(loc) < 128 and blue(loc) > 128:
                picture2[x + y * img.width] = color(0, 0, 255)

            # 3--Apply thresholding to create a bright red region--lower left
            if 50 < x < 150 and 50 < y < 300 and red(loc) > 128:
                picture3[x + y * img.width] = color(255, 0, 255)
            else:
                picture3[x + y * img.width] = loc

            # 4--Apply thresholding to create a black, gray, and white region--lower right
            if brightness(loc) > 200:
                picture4[x + y * img.width] = color(255, 200, 0)
            elif brightness(loc) > 100:
                picture4[x + y * img.width] = color(128)
            else:
                picture4[x + y * img.width] = loc

    # Display the four new images side-by-side
    image(img1, 0, 0)
    image(img2, img.width, 0)
    image(img3, 0, img.height)
    image(img4, img.width, img.height)

    save("final_output2.jpg")
