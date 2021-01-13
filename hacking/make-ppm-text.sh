#!/bin/bash
#
# Create a gray, 24-bits per pixel, ppm image (text version)
#
# File format
#
# Magic number (always P3 for ascii?)
# Width Height
# Maximum pixel value (<256 implies 8-bits per channel)
# Text pixel data
#
width=256
height=256

#
# Write the ascii header
#
echo P3
echo ${width} ${height}
echo 255

#
# Write the ascii pixel data. Limit to 70 chars per line for compatibility.
#
for y in `seq ${height}`
do
    for x in `seq ${width}`
    do
        echo -n -e '128 128 128 '
    done
done

