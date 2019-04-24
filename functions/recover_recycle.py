#Purpose: 	Copy all of the contents of the Recycle Bin to a destination folder
#		perserving the dir structure and filename.
#		Not meant as a forensically sound aquistion tool. Just a means to an end.
#This hack job of a python script does:
#1. Looks for $I files
#2. Checks to see if the corresponding $R file exists
#3. Parses $I files to get the original filename and path
#4. Copies the $R file to the output folder recreating the original dir structure
# Example:
# c:\test\subdir\uselessfile.txt gets deleted.
# This script will copy the file out of the Recycle Bin to c:\Temp\Root\Test\subdir\uselessfile.txt.
# If one already exists there, it will keep trying make a unique name ex: uselessfile12345.txt

#ref = http://jon.glass/blog/mass-undelete-from-the-recycle-bin/

import os
import random
import codecs
from os.path import exists
RecBin = 'C:\\$Recycle.Bin'
DestFolder = 'C:\\Users\\tlchong\\Desktop\\uncategorized_1\\'

def look4ifiles(ext, dirname, names):
	for name in names:
		if (name.lower().startswith('$i')):
			check4rfile(dirname, name)
			
def check4rfile(ifiledirname, ifilename):
	rfilename = ifilename.lower().replace('$i','$r')
	if exists(os.path.join(ifiledirname, rfilename)):
		parseifile(ifiledirname, ifilename, rfilename)
	else:
		print("Can not find " + rfilename + " for " + os.path.join(ifiledirname, rfilename))
	os.system('echo f |del \"' + ifilename + '\"')
		

def parseifile(ifiledirname, ifilename,rfilename):
	dest_path = ''
	ifile = os.path.join(ifiledirname, ifilename)
	with open(ifile,"rb") as f:
		f.seek(28)
		file_path = str(f.read(1))
		
		while file_path != "b''":
			if file_path != r"b'\x00'":#int(codecs.encode(file_path, "hex"),16) != 0:
				dest_path += file_path[2:-1]
			file_path = str(f.read(1))
			
		#input(dest_path)
	extractfromrecbin(ifiledirname, rfilename, dest_path)

def extractfromrecbin(ifiledirname, rfilename, dest_path):
	rfile = ifiledirname + '\\' + rfilename
	outputlocation = finduseabledestinationfilepath(DestFolder, dest_path.split('\\')[-1])
	if '.' in rfilename:
		os.system('echo f |xcopy /Y \"' + rfile + '\" \"' + str(outputlocation) + '\"')
	else:
		os.system('echo f |xcopy /Y /I \"' + rfile + '\" \"' + str(outputlocation) + '\"')
	os.system('echo f |del \"' + rfile + '\"')

def finduseabledestinationfilepath(a,b):
	final_dest_path = a + b
	#input('{} {}'.format(a,b))
	if exists(final_dest_path) and b.find('.') != -1:
		fileName, fileExtension = os.path.splitext(b)
		b = str(fileName + str(random.randint(0,10)) + fileExtension)
		print (a, b)
		return finduseabledestinationfilepath(a, b)
		
	elif exists(final_dest_path):
		b = str(b + str(random.randint(0,10)))
		print (a, b)
		return finduseabledestinationfilepath(a, b)
		
	else:
		return final_dest_path
		
#os.path.walk(RecBin, look4ifiles, exten)
for root, dirs, files in os.walk("c:\\$recycle.bin", topdown=False):
	for name in files:
		if (name.lower().startswith('$i') == True):
			print(name)
			check4rfile(root, name)