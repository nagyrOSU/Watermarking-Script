******************************************************
* watermark.py / watermark.exe
* Created by: Rene Nagy
******************************************************

A simple script to dynamically resize a logo image and paste it on top of other images. Because it resizes dynamically, it is great for
watermarking many images en masse. Allows user input for the watermark location, opacity, and size.

This repo contains the watermark.py script and the same script converted to a windows executable, both with the same functionality.

The executable only works on windows machines, but requires no dependancies other than the visual c++ redistributable (I think...)

Below are much more in depth instructions. If you are familiar with technology / programming this script's user input instructions should
be sufficient. If more details are necessary, see below.

*************** EXTENDED INSTRUCTIONS ********************


To use it, simply run the executable or python script and it will ask for user input to watermark images as desired

First, it will ask you to enter "custom" to run with custom parameters for logo location, opacity, and size, 
or to enter nothing (just press enter) to continue with default postion, opacity, and logo

Then, it will ask for the path to an image file to be used as the watermark, then path to a folder with images to watermark, whether or not you would like
to watermark subfolders, and finally a path to a folder to save the watermarked images

***A NOTE ABOUT FILE PATHS***
A period ('.') represents the current working directory. This is the directory that the executable is in. 
So if, for example, the logo to be used as a watermark is in the same directory as the executable, a valid filepath is 
'./image_name.png' (file name and .png or .jpg extention are, of course, subject to the name and filetype of the image you would like to use)

As another example, perhaps the current working directory contains this executable, a folder labeled "images" 
containing both the images to be watermarked and the image to be used as a watermark, and a folder labeled "watermarked_pictures"


The proper inputs for the logo file path, image folder path, and saved image folder path would be:
./images/image_name.png
./images
./watermarked_pictures


***IMPORTANT***
As shown above, you must add the extention (i.e. '.png') to the end of the logo filename. 
Otherwise it won't be able to find the file. Yes, image_name WILL NOT WORK. image_name.png or image_name.jpg (depending on the file) will work!


If in custom mode, the program will also ask for a location to add the watermark (the corners or the center, with default of bottomright),
a value for opacity (integer between 0 and 255) and a value for size modifier (a decimal between 0.0 and 1.0)

Opacity of 0 is full transparency, opacity of 255 is fully opaque.

The size modifier is describes how wide the watermark should be, relative to the width of the image to be watermarked.
0.5 will create a watermark with half the width of the image it is applied to. 0.25 will create a watermark with one quarter the width of the image, and so on.
The height of the watermark will then be scaled to give a constant aspect ratio, so the watermark will not be distorted.



***TIPS FOR USE***
This script works best if the logo used is a .png. Although .jpg logos will work, quality will be reduced, 
as the script will attempt to make white backgrounds of .jpg images transparent (it will essentially convert it to a .png).

This has the advantage that it will allow opacity changes to work properly but will:
1: Could cause drops in image quality
2: Will cause .jpg logos with white as part of the logo (not just the background) to look bad

If you have a .jpg logo, please use an online .jpg to .png conversion tool first. Results will likely be better


ANOTHER TIP: 
Since the script dynamically resizes images based on width, logos might look smaller than desired on images that are vertical (much taller than they are wide).
If you find this to be the case, put vertical images in a seperate folder, and run the script with a larger than default size modifier.

This also means wide and short logos (like a string of text) will be smaller by area for a given size modifier compared to a more square logo.

However, the dynamic resizing means it will work will even with images of very varied resolutions!


Thank you for using watermark.exe!

