import os

def sub_directory(path):
	list = os.listdir(path)
	list = [os.path.sep.join([path,x]) for x in list]
	list = [x for x in list if os.path.isdir(x)]
	return list
	
def sub_files(path):
	list = os.listdir(path)
	list = [os.path.sep.join([path,x]) for x in list]
	list = [x for x in list if not os.path.isdir(x)]
	return list
	
def sub_images(path):
	list = os.listdir(path)
	list = [os.path.sep.join([path,x]) for x in list]
	list = [x for x in list if not os.path.isdir(x) and x.endswith('.jpg')]
	return list
	
def getsub(list):
	if len(list) == 0:
		return []
	else:
		element = list.pop()
		return sub_directory(element) + getsub(list)


def loop_dir(path , layer = 1):

	list = [path]
	for i in range(layer):
		list = getsub(list)	
	
	return list
	
def loop_files(path , layer = 1):

	list = loop_dir(path, layer)
	result = []
	for i in list:
		result += sub_files(i)
	
	return result
	
def loop_images(path , layer = 1):

	list = loop_dir(path, layer)
	result = []
	for i in list:
		result += sub_images(i)
	
	return result