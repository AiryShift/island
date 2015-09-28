import numpy as np
from math import sqrt


def generate_mask(width, height):
    mask = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            distance_x = abs(x - width * 0.5)
            distance_y = abs(y - width * 0.5)
            distance = sqrt(distance_x * distance_x + distance_y * distance_y)

            max_width = width * 0.5 - 5.0
            delta = distance / max_width
            gradient = delta * delta

            mask[x][y] = max(0.0, 1.0 - gradient)
    return mask

if __name__ == '__main__':
    from PIL import Image
    data = generate_mask(128, 128)
    img = Image.fromarray(np.uint8(data * 255))
    img.save('out.png')
