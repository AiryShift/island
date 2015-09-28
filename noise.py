import random
import numpy as np

PERSISTENCE = 0.5


def generate_white_noise(width, height, seed=None):
    random.seed(seed)
    noise = np.zeros((width, height))
    for x in np.nditer(noise, op_flags=['readwrite']):
        x[...] = random.random()
    return noise


def interpolate(x0, x1, alpha):
    return x0 * (1 - alpha) + alpha * x1


def generate_smooth_noise(baseNoise, octave):
    width = len(baseNoise)
    height = len(baseNoise[0])
    smoothNoise = np.zeros((width, height))

    samplePeriod = 2**octave
    sampleFrequency = 1 / samplePeriod

    for i in range(len(baseNoise)):
        sample_i0 = i // samplePeriod * samplePeriod
        sample_i1 = (sample_i0 + samplePeriod) % width
        horizontal_blend = (i - sample_i0) * sampleFrequency

        for j in range(len(baseNoise[i])):
            sample_j0 = j // samplePeriod * samplePeriod
            sample_j1 = (sample_j0 + samplePeriod) % height
            vertical_blend = (j - sample_j0) * sampleFrequency

            top = interpolate(baseNoise[sample_i0][sample_j0], baseNoise[
                              sample_i1][sample_j0], horizontal_blend)
            bottom = interpolate(baseNoise[sample_i0][sample_j1], baseNoise[
                                 sample_i1][sample_j1], horizontal_blend)

            smoothNoise[i][j] = interpolate(top, bottom, vertical_blend)
    return smoothNoise


def generate_perlin_noise(baseNoise, octaveCount):
    width = len(baseNoise)
    height = len(baseNoise[0])

    smoothNoise = []
    for i in range(octaveCount):
        smoothNoise.append(generate_smooth_noise(baseNoise, i))

    perlinNoise = np.zeros((width, height))
    amplitude = 1.0
    totalAmplitude = 0.0

    for octave in range(octaveCount - 1, -1, -1):
        amplitude *= PERSISTENCE
        totalAmplitude += amplitude
        for i in range(width):
            for j in range(height):
                perlinNoise[i][j] += smoothNoise[octave][i][j] * amplitude

    for i in range(width):
        for j in range(height):
            perlinNoise[i][j] /= totalAmplitude

    return perlinNoise


def make_rgb(baseNoise):
    width = len(baseNoise)
    height = len(baseNoise[0])
    rgbNoise = np.zeros((width, height * 3))
    for i in range(width):
        for j in range(height):
            rgbNoise[i][j * 3] = round(baseNoise[i][j] * 255)
            rgbNoise[i][j * 3 + 1] = round(baseNoise[i][j] * 255)
            rgbNoise[i][j * 3 + 2] = round(baseNoise[i][j] * 255)
    rgbNoise = np.array(rgbNoise, dtype='uint8')
    return rgbNoise


def generate_noise(width=4, height=4, octaveCount=5, seed=None):
    noise = generate_perlin_noise(
        generate_white_noise(width, height, seed=seed), octaveCount)
    return make_rgb(noise)


if __name__ == '__main__':
    for i in generate_noise(4, 4, seed=0):
        print(i)
