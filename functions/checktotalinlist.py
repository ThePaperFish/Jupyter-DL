#Test Empty
import os 
dir_path = r"C:\Users\tlchong\Downloads"

list = os.listdir(dir_path)
count = 0
for x in list:
	count += 1
	f = open(os.path.sep.join([dir_path,x]), "r")
	content = f.read()
	content = content.split('\n')
	
	lvl = 'S'
	if (len(content) > 200):
		lvl = 'M'
	if (len(content) > 500):
		lvl = 'L'			
	print("{}. {} - {} - {}".format(count, lvl, len(content), x[:-4]))
	f.close()
	
input("\npress enter to continue...")