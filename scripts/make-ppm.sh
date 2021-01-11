#!/bin/bash
#
# Create a gray, 24-bits per pixel, ppm image.
#
# File format
#
# Magic number (always P6)
# Width Height
# Maximum pixel value (<256 implies 8-bits per channel)
# Binary pixel data
#
width=128
height=128

#
# Write the ascii header
#
echo P6
echo ${width} ${height}
echo 255

#
# Write the binary pixel data.
#
for y in `seq ${height}`
do
    for x in `seq ${width}`
    do
        echo -n -e '\x80\x80\x80'
    done
done

