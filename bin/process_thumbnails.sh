#!/bin/bash

mkdir images-sm

ORIGINALS=images0/*
COPIES=images-sm/*

# copy files
for file in $ORIGINALFILES; do
	cp -p $file ./images-sm
done

# find center of the image
# from the center crop a 100 by 100 pixel square
# sharpen by 0.5 pixel and output acno.tile.jpg
for file in $COPIES; do
	convert $file -gravity Center \
	-crop 100x100+0+0 -sharpen 0x0.5 \
	`basename $file .jpg`.tile.jpg
done