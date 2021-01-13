#
# Make an ascii ppm image file for testing.
#
f = open('tmp.ppm', 'w')
f.write('P3\n')
f.write('128 128\n')
f.write('255\n')

pixels = 0
for y in range(128):
    for x in range(128):
        if (pixels > 5):
            f.write('\n')
            pixels = 0
        f.write('128 128 128 ')
        pixels += 1

f.close()
