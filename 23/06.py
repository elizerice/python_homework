from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color=(117,187,253), snow_color=(255,250,250), trunk_color=(165,90,82), needls_color=(1,121,111), sun_color=(255,219,0)):

    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    #sky
    draw.rectangle(((0, 0), (width, height)), (sky_color))

    #snow
    draw.rectangle(((0, height * 0.8), (width, int(height))), fill=snow_color)

    #sun
    sun_radius = min(width, height) // 10
    sun_center_x = width - sun_radius * 2
    sun_center_y = sun_radius * 2
    draw.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)

    #trunk
    draw.polygon([(0.45 * width, 0.9 * height),(0.55 * width, 0.9 * height),(0.55 * width, 0.70 * height) ,(0.45 * width, 0.70 * height),
                  ], fill=trunk_color)

    #needls
    draw.polygon([(0.5 * width, 0.1 * height),(0.4 * width, 0.3 * height), (0.6 * width, 0.3 * height)],
                 fill=needls_color)
    draw.polygon([(0.5 * width, 0.2 * height),(0.35 * width, 0.5 * height), (0.65 * width, 0.5 * height)],
                 fill=needls_color)
    draw.polygon([(0.5 * width, 0.3 * height),(0.30 * width, 0.7 * height), (0.7 * width, 0.7 * height)],
                 fill=needls_color)

    image.save(file_name)


picture('test.bmp', 1000, 800)
