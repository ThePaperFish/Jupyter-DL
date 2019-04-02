import os
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path")
ap.add_argument("-i", "--input", required=True,
	help="from name")
ap.add_argument("-o", "--output", required=True,
	help="to name")
args = vars(ap.parse_args())

ori_path = args["path"]
ori_name = args["input"]
go_name = args["output"]

list = os.listdir(ori_path)

for x in list:		
	y = x
	
	x = x.replace(ori_name,go_name)
	if(x.find('(') + x.find(')') != -2):
		x = x[:x.find('(') - 1] + x[x.find(')') + 1:]
	
	os.rename(os.path.sep.join([ori_path,y]) ,os.path.sep.join([ori_path,x]) )