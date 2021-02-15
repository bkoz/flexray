#
# Chapter 5 - Sillouette of a sphere
#
from Point import Point
from Vector import *
from Canvas import *
from Matrix import *
from Color import *
from Sphere import *
import os
from multiprocessing import Pool
import time
import argparse

print(f'logical threads available = {os.cpu_count()}')

# Globals
canvas_pixels = 100
canvas = Canvas(canvas_pixels, canvas_pixels)
color = Color(1, 0, 0)
ray_origin = Point([0, 0, -5])
wall_z = 10
wall_size = 7
pixel_size = wall_size / canvas_pixels
half = wall_size / 2
shape = Sphere()

def pix_to_char(p):
        c = round(p * 255)
        if (c < 0):
            c = 0
        if (c > 255):
            c = 255
        return c

def write_pixels(width, height, pixels):
        f = open('image{0}x{1}.ppm'.format(width, height), 'w')
        f.write('P3\n')
        f.write('{0} {1}\n'.format(width, height))
        f.write('255\n')
        
        for i in pixels:
            for j in i:
                f.write(f'{j[0]} {j[1]} {j[2]} ')

        f.close()

def render(n):
    print(f'render(): thread [{n[0]}, {n[1]}]')
    pixels = []
    t0 = time.time()
    for y in range(n[0], n[1]):
        world_y = half - pixel_size * y
        for x in range(0, canvas.width):
            world_x = -half + pixel_size * x
            position = Point([world_x, world_y, wall_z])
            r = Ray(ray_origin, normalize(position - ray_origin))
            xs = shape.intersect(r)
            if (xs):
                pixels.append([255, 0, 0])
                # canvas.write_pixel(x, y, Color(1, 0, 0))
            else:
                pixels.append([0, 0, 0])

    print(f'render(): thread [{n[0]}, {n[1]}], elapsed time = {time.time() - t0:.3f} seconds.')
    return pixels

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="default = 100", default=100)
    parser.add_argument("-t", "--threads", help="default = 1", default=1)
    args = parser.parse_args()

    canvas_pixels = int(args.size)
    num_threads = int(args.threads)
    print(f'canvas = {canvas_pixels}x{canvas_pixels}, threads = {num_threads}')

    num_threads = int(args.threads)
    l = []
    chunk = canvas_pixels // num_threads
    for i in range(num_threads):
        start = i * chunk
        end = start + chunk
        l.append([start, end])   
    
    p = Pool(processes=num_threads)
    t0 = time.time()
    pixels = p.map(render, l, chunksize=1)
    p.close()
    p.join()

    print(f'Total elapsed time = {time.time() - t0:0.3f} seconds')

    # print(f'map output: pixels = {pixels}')
    write_pixels(canvas_pixels, canvas_pixels, pixels)
    # canvas.canvas_to_ppm()

if __name__ == '__main__':

    main()
