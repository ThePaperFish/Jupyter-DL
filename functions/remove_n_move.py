import os
path = 'C:\\Users\\tlchong\\Downloads\\'
destination_path = r'C:\vs2015shareddata\dataset\MY Profiles\temp'

exts = ['.jpg','.png','.gif','jpeg']
list = os.listdir(path)

os.system("cls")
#
# Section 1: Remove unwanted files.
#

count = 0

for x in list:
	if '.' in x:
		if x[-5:] == ".webp":
			#convert
			os.system('dwebp "' + path + x + '" -o "' + path + x[:-5] + '.png">NULL')
			#delete
			os.remove(path + x)
			print("--'" + x + "' Converted!")
		elif x[-4:] not in exts:
			os.remove(path + x)
			print("--'" + x + "' Removed!")
			count+= 1
	elif '(1)' in x:
		os.remove(path + x)
		print("'" + x + "' Removed!")
	
print('[INFO] Total {0} Files Removed.'.format(count))

list = os.listdir(path)
print('\n[INFO] There are now {0} Files in the directory.'.format(len(list)))
if (input(">Proceed to move?(y/n):").lower() != "y"):
	exit()

#
# Section 2: find and make directory(depend on first item).
#

start = list[0].find('_')
end = list[0].find('_',start + 1)

name = list[0][start + 1:end]
destination_path += '\\' + name + '\\'

try:
    os.stat(destination_path)
except:
    os.mkdir(destination_path)

print('\n[INFO] Directory = {}'.format(name))

#
# Section 3: Move files.
#

count2 = 0
for x in list:
	os.rename(path + x,destination_path + x)
	count2 += 1
	
print('[INFO] Total {} Files move to {}.' .format(count2,name))