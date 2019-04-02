import os

dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
f = open(dir_path + "\\list\\result.txt", "r")
count = 0

content = f.read()
content = content.split('\n')
#content.sort()

for x in content:
  count += 1
  print('{0}: {1}'.format(count,x))
  if ( count < 0):
    continue
	
  os.system('start chrome "https://www.google.com/search?q='+ x.replace(' ','+') +'&tbm=isch"')
  input("Press Enter to continue...")
  
	
	
f.close()
print('Done')

print('\nHere is the result.')
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
	
