from PIL import Image, ImageDraw


def gradient(color):
    size_x = 512
    size_y = 200
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (size_x, size_y), new_color)
    draw = ImageDraw.Draw(new_image)

    if color.lower() == 'r':
        for i in range(size_x):
            r = int(i / 2)
            draw.line((i, 0, i, size_y), fill=(r, 0, 0), width=2)
    elif color.lower() == 'g':
        for i in range(size_x):
            g = int(i / 2)
            draw.line((i, 0, i, size_y), fill=(0, g, 0), width=2)
    elif color.lower() == 'b':
        for i in range(size_x):
            b = int(i / 2)
            draw.line((i, 0, i, size_y), fill=(0, 0, b), width=2)

    new_image.save('res.png', 'PNG')


gradient("R")
