from noise import generate_noise
from PIL import Image
import numpy as np
from sys import argv

WIDTH = 256
HEIGHT = 256
MAX_BYTE_VAL = 255

if __name__ == '__main__':
    data = generate_noise(WIDTH, HEIGHT, octaveCount=int(argv[1]))
    img = Image.fromarray(np.uint8(data * MAX_BYTE_VAL))
    img.save('out.png')
