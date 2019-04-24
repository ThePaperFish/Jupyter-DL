import os
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path")
args = vars(ap.parse_args())

path = args["path"]
list = os.listdir(path)
list = [os.path.sep.join([path,x]) for x in list]
list = [x for x in list]

for x in list:		
	
	if os.path.isdir(x):
		for y in os.listdir(x):
				
			old_ = os.path.sep.join([x ,y])
			new_ = os.path.sep.join([path,y])
			
			os.rename(old_ ,new_ )
				
		os.rmdir(x)
		
	else : 
		os.remove(x)
	