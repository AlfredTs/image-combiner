import os
from tqdm import tqdm
import random
from PIL import Image, ImageDraw, ImageFilter


directory = sorted(os.listdir())
layers = []

#read all the files
for f in directory:
	if os.path.isdir(f):
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
	for f in comb[1:]:
		mix = Image.alpha_composite(mix,Image.open(f))
	
	mix.save('output_'+str(hash('-'.join(comb)))+'.png',format='png')




