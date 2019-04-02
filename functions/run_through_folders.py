import sub_direct 
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--command", type=str, required=True,
	help="command for every folder (`path` for path location, `#` = Second command)")
ap.add_argument("-p", "--path", required=True,
	help="path")
ap.add_argument("-l", "--layer", type=int, default=1,
	help="amount of layer")
args = vars(ap.parse_args())

list = sub_direct.loop_dir(args["path"], args['layer'])

if args['mode'] == 1:
	print('\n'.join(list))
	exit()

command = args['command']
command = command.split('#')

print()
for i in command:
	print("[Command] {}".format( i))


input("Amount of sub folders: {}.".format(len(list)))

for x in list:		
	
	print("\n" * 3 + "=" * 10 + x + "=" * 10)	
	
	for i in command:
		os.system(i.replace('path',x))