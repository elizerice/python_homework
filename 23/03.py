from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color=(135, 206, 235), ocean_color=(1, 123, 146), boat_color=(135, 69, 53),
            sail_color=(255, 255, 255), sun_color=(255, 207, 64)):

    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    #sky
    draw.rectangle(((0, 0), (width, height)), (sky_color))

    #ocean
    draw.rectangle(((0, height * 0.8), (width, int(height))), fill=ocean_color)

    #sun
    sun_radius = min(width, height) // 10
    sun_center_x = width - sun_radius * 2
    sun_center_y = sun_radius * 2
    draw.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)

    #bottom
    draw.polygon([(0.70 * width, 0.85 * height),
                  (0.30 * width, 0.85 * height),
                  (0.25 * width, 0.65 * height),
                  (0.75 * width, 0.65 * height)],
                 fill=boat_color)
    draw.polygon([(0.51*width,0.3*height),(0.49*width,0.3*height),( 0.49*width,0.75*height) , (0.51*width,0.75*height)], fill=boat_color)

    #sail
    draw.polygon([(0.51*width,0.3*height),(0.51*width,0.60*height),(0.65*width,0.45*height)], fill=sail_color)

    image.save(file_name)

picture('test.bmp', 1000, 800)
