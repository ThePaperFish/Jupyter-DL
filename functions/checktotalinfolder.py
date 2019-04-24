#Test Empty
import os 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path to folder")
args = vars(ap.parse_args())
	
dir_path = args['path']

list = os.listdir(dir_path)
count = 0
for x in list:
	count += 1
	content = os.listdir(os.path.sep.join([dir_path, x]))
	
	lvl = 'S'
	if (len(content) > 200):
		lvl = 'M'
	if (len(content) > 500):
		lvl = 'L'			
	print("{}. {} - {} - {}".format(count, lvl, len(content), x))
	
#input("\npress enter to continue...")