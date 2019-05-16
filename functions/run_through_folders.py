import sub_direct 
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--command", type=str, required=True,
	help="command for every folder (`[path]` for path location, `#` = Second command)")
ap.add_argument("-p", "--path", required=True,
	help="path")
ap.add_argument("-l", "--layer", type=int, default=1,
	help="amount of layer")
ap.add_argument("-w", "--wait", type=int, default=1,
	help="1 to confirm operation, 0 for no confirm")
args = vars(ap.parse_args())

list = sub_direct.loop_dir(args["path"], args['layer'])

command = args['command']
command = command.split('#')

print()
for index, i in enumerate(command):
	i = i.replace('path', 'PATH')
	i = i.replace('[', '\"' )
	i = i.replace(']', '\"' )
	print("[Command {}] {}".format(index + 1,i))

if args['wait'] == 1:
	input("Amount of sub folders: {}.".format(len(list)))
else:
	print("Amount of sub folders: {}.".format(len(list)))

for x in list:		
	
	print("\n" * 3 + "=" * 10 + x + "=" * 10)	
	
	for i in command:
		i = i.replace('path', x )
		i = i.replace('[', '\"' )
		i = i.replace(']', '\"' )
		os.system(i)