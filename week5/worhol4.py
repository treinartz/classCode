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
            loc = pixel_list[x + y * img.width]  # convert 2 rows/cols to 1 row

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

            # 5--Convert the color to grayscale--picture4
            color_mode(RGB)
            grey = int(0.299 * red(loc) + 0.587 * green(loc) + 0.114 * blue(loc))
            new_color = color(grey, grey, grey)

            # Set the modified color in the new image
            index = x + y * img.width
            picture4[index] = new_color

            # 6--Remove the red component of the color--picture4
            color_mode(RGB)
            r, gr, b = red(loc), green(loc), blue(loc)
            new_color = color(0, gr, b)

            # Set the modified color in the new image
            index = x + y * img.width
            picture4[index] = new_color

            # 7--sepia tone--Convert the color to Sepia Tone--picture4
            color_mode(RGB)
            r, gr, b = red(loc), green(loc), blue(loc)
            tr = int(0.393 * r + 0.769 * gr + 0.189 * b)
            tg = int(0.349 * r + 0.686 * gr + 0.168 * b)
            tb = int(0.272 * r + 0.534 * gr + 0.131 * b)
            new_color = color(min(tr, 255), min(tg, 255), min(tb, 255))

            # Set the modified color in the new image
            index = x + y * img.width
            picture4[index] = new_color

    # Display the four new images side-by-side
    image(img1, 0, 0)
    image(img2, img.width, 0)
    image(img3, 0, img.height)
    image(img4, img.width, img.height)

    save("final_output2.jpg")
