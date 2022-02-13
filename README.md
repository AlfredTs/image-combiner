# image-combiner
The tool randomly picks one image from each folder it finds in its work directory and composits them together. Usefull for building variations of jpegs that are sold for imaginary money.

All images have to be of identical resolution.

# Hue variations
If you want for the randomizer to shift hue for some of the images add "_hue" suffix to their names. You can also add that suffix to the whole folder in order to enable hue shift randomizations for all of the images in the folder.
Note that hue shifting takes a little longer than simply compositing the layers together.

# Installation

pip install tqdm Pillow numpy
