import os

dir_path = r'C:\Users\tlchong\Downloads'
txts = os.listdir(dir_path)
contents = []

for txt in txts:
	f = open(dir_path + "\\" + txt , "r")
	try:
		content = f.read()
		content = content.split('\n')
		contents += content 
	except: 
		pass
	f.close()

contents.sort()
count = 0

new_contents = [contents.pop()]
for content in contents:
	if content != new_contents[-1]:
		new_contents += [content]
		continue
	count += 1

input(count)
print(len(new_contents))		
f = open(dir_path + "\\result" , "w")
f.write('\n'.join(new_contents))
f.close()
