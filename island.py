from noise import generate_noise
from mask import generate_mask
from PIL import Image
import numpy as np
from sys import argv

WIDTH = 512
HEIGHT = 512
MAX_BYTE_VAL = 255

if __name__ == '__main__':
    count = 6
    if len(argv) > 1:
        count = int(argv[1])
    data = generate_noise(WIDTH, HEIGHT, octaveCount=count)
    mask = generate_mask(WIDTH, HEIGHT)
    data *= mask
    img = Image.fromarray(np.uint8(data * MAX_BYTE_VAL))
    img.save('out.png')
