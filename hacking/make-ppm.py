#
# Make an ascii ppm image file for testing.
#
width = 16
height = 16
f = open('tmp.ppm', 'w')
f.write('P3\n')
f.write('{0} {1}\n'.format(width, height))
f.write('255\n')

color = (128, 128, 128)
pixels = 0
for y in range(width):
    for x in range(height):
        if (pixels > 5):
            f.write('\n')
            pixels = 0
        f.write('{0} {1} {2} '.format(color[0], color[1], color[2]))
        pixels += 1

f.close()
