import os
import random
import colorsys
import numpy as np
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFilter

#hue shifting stuff
rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

    return new_img


directory = sorted(os.listdir())
layers = []
hueTag = '_hue'

#read all the files
for f in directory:
	if os.path.isdir(f) and f[0]!='.':
		layers.append([f+'/'+x for x in sorted(os.listdir(f))])


if len(layers) != 0:
	print("I see "+str(len(layers))+" folders. With "+str(sum(len(row) for row in layers))+" in total!")
else:
	print("I can't seem to see any folders in my working directory. Am I where I should be? I'm not smart enough to do anything about it, so I'll just go :/")
	exit()

shuffles = int(input("How many combinations would you like me to make out of these? (I only understand numbers)\n"))

if (shuffles!=0):
	print("Let's gooo!")
else:
	print("Mkaaay, bye")
	exit()

#shuffle combinations
combinations = []
for i in range(0,shuffles):
	comb = []
	for l in layers:
		comb.append(l[random.randint(0,len(l)-1)])
	combinations.append(comb)

#composite combinations
for i in tqdm(range(len(combinations))):
	comb = combinations[i]
	mix = Image.open(comb[0])
	shifts = []
	for f in comb[1:]:
		img = Image.open(f)

		if hueTag in f:
			arr = np.array(img)
			hueShift = random.random()
			img = Image.fromarray(shift_hue(arr,hueShift),'RGBA')
			shifts.append(str(hueShift))
		
		mix = Image.alpha_composite(mix,img)
	
	mix.save('output_'+str(hash('-'.join(comb)+'_'.join(shifts)))+'.png',format='png')




