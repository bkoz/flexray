#
# Chapter 6 - Lit and shaded sphere
#
from Point import Point
from Vector import *
from Canvas import *
from Matrix import *
from Color import *
from Sphere import *
from PointLight import *
import os
from multiprocessing import Pool
import time
import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info(f'logical threads available = {os.cpu_count()}')

# Globals
canvas_pixels = 400
canvas = Canvas(canvas_pixels, canvas_pixels)
color = Color(1, 0, 0)
ray_origin = Point([0, 0, -5])
wall_z = 10
wall_size = 7
pixel_size = wall_size / canvas_pixels
half = wall_size / 2
shape = Sphere()

# Add a material
shape.material = Material()
shape.material.color = Color(1, 0.2, 1)

# Create a point light source.
light_position = Point(-10, 10, -10)
light_color = Color(1, 1, 1)
light = PointLight(light_position, light_color)


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
    logger.info(f'render(): pid = {os.getpid()}, thread [{n[0]}, {n[1]}]')
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
                # Find the closest hit point
                xs.t.sort(reverse=False)
                hitPoint = r.position((xs.t)[0])
                normal = shape.normal_at(hitPoint)
                eye = -r.direction
                color = lighting(shape.getMaterial(), light, hitPoint, eye, normal)
                pixels.append([round(color.red*255), round(color.green*255), round(color.blue*255)])
            else:
                pixels.append([0, 0, 0])

    logger.info(f'render(): thread [{n[0]}, {n[1]}] finished, elapsed time = {time.time() - t0:.3f} seconds.')
    return pixels

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="default = 400", default=400)
    parser.add_argument("-t", "--threads", help="default = 1", default=1)
    args = parser.parse_args()

    canvas_pixels = int(args.size)
    num_threads = int(args.threads)
    logger.info(f'canvas = {canvas_pixels}x{canvas_pixels}, running with {num_threads} threads.')

    num_threads = int(args.threads)
    l = []
    chunk = canvas_pixels // num_threads
    for i in range(num_threads):
        start = i * chunk
        #
        # The last thread works on any remaining scan lines.
        # This handles the special case when chunk does not divide evenly.
        #
        if (i == num_threads - 1):
            end = canvas_pixels
        else:
            end = start + chunk
        
        l.append([start, end])   
    
    p = Pool(processes=num_threads)
    t0 = time.time()
    pixels = p.map(render, l, chunksize=1)
    p.close()
    p.join()

    logger.info(f'Total elapsed time = {time.time() - t0:0.3f} seconds')

    write_pixels(canvas_pixels, canvas_pixels, pixels)

if __name__ == '__main__':

    main()
