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

print(f'{os.cpu_count()} logical threads available')
# Canvas
canvas_pixels = 500
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
    print(f'render(): start = {n[0]}, stop = {n[1]}')
    pixels = []
    count = 0
    t0 = time.time()
    for y in range(n[0], n[1]):
        world_y = half - pixel_size * y
        for x in range(0, canvas.width):
            world_x = -half + pixel_size * x
            position = Point([world_x, world_y, wall_z])
            r = Ray(ray_origin, normalize(position - ray_origin))
            xs = shape.intersect(r)
            count += 1
            if (xs):
                pixels.append([255, 0, 0])
                # canvas.write_pixel(x, y, Color(1, 0, 0))
            else:
                pixels.append([0, 0, 0])

    print(f'elapsed thread time = {time.time() - t0}, count = {count}')
    print(f'finished render(): start = {n[0]}, stop = {n[1]}')
    return pixels

def main():

    num_threads = 1
    l = []
    chunk = canvas_pixels // num_threads
    for i in range(num_threads):
        start = i * chunk
        end = start + chunk
        l.append([start, end])   
    
    print(f'Running with {num_threads} threads.')
    p = Pool(num_threads)
    t0 = time.time()
    pixels = p.map(render, l, chunksize=1)
    p.close()
    p.join()

    print(f'elapsed = {time.time() - t0}')

    # print(f'map output: pixels = {pixels}')
    write_pixels(canvas_pixels, canvas_pixels, pixels)
    # canvas.canvas_to_ppm()

if __name__ == '__main__':

    main()