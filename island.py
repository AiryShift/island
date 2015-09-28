from noise import generate_noise
from PIL import Image
import numpy as np

WIDTH = 128
HEIGHT = 128

if __name__ == '__main__':
    data = generate_noise(WIDTH, HEIGHT, octaveCount=5)
    img = Image.fromarray(data, 'RGB')
    img.save('out.png')
