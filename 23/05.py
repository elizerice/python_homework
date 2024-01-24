from PIL import Image, ImageDraw


def board(num, size):
    width =num * size
    height = num * size
    image = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(image)
    for i in range(num):
        for j in range(num):
            x = j * size
            y = i * size
            if (i + j) % 2 == 0:
                draw.rectangle([x, y, x + size, y + size], fill="black")
            else:
                draw.rectangle([x, y, x + size, y + size], fill="white")
    image.save("res.png")


board(8, 50)
