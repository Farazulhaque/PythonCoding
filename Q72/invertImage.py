from images import Image


def invert(image):
    pass


def balckAndWhite(image):
    # Converts an image to black and white
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)


def grayscale(image):
    # Converts an image to grayscale
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


def main():
    # filename = input("Enter the image file name: ")
    filename = "Q72\cat.JPG"
    image = Image(filename)
    # Invert Image
    invert(image)
    image.draw()
    # Convert image to grayscale then draw
    grayscale(image)
    invert(image)
    image.draw()
    # Convert image to black and white then invert
    balckAndWhite(image)
    invert(image)
    image.draw()


if __name__ == "__main__":
    main()
