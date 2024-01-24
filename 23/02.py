from PIL import Image
image = Image.open("image.jpg")
pixels = list(image.getdata())
sum_r = 0
sum_g = 0
sum_b = 0
for r, g, b in pixels:
    sum_r += r
    sum_g += g
    sum_b += b
num_pixels = len(pixels)
averg_r = sum_r // num_pixels
averg_g = sum_g // num_pixels
averg_b = sum_b // num_pixels
print(averg_r, averg_g, averg_b)
