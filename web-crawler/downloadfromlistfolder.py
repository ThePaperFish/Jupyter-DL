# import the necessary packages
#from imutils import paths
import argparse
import requests
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to folder containing file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of directory of images")
ap.add_argument("-l", "--loop", type=int,default=-1,
	help="get all or not")
args = vars(ap.parse_args())

#READ FOLDER
urllistlist = os.listdir(args["urls"])

#LOOP IT
for urllist in urllistlist:

	destination_path = os.path.sep.join([args["output"], urllist[:-4]])
	#CREATE DIRECTORY
	try:
		os.stat(destination_path)
	except:
		os.mkdir(destination_path)
		
	#PASS ARGUMENTS
	
	# grab the list of URLs from the input file, then initialize the
	# total number of images downloaded thus far
	rows = open(os.path.sep.join([args["urls"], urllist])).read().strip().split("\n")
	rows = rows[:args['loop']]
	print("Total Urls: {}".format(len(rows)))
	total = 0
	total_download_error = 0
	total_file_error = 0
	
	# loop the URLs
	for url in rows:
		try:
			# try to download the image
			r = requests.get(url, timeout=60)

			# save the image to disk
			p = os.path.sep.join([destination_path, "{}.jpg".format(
				str(total).zfill(6))])
			f = open(p, "wb")
			f.write(r.content)
			f.close()

			# update the counter
			#print("[INFO] downloaded: {}".format(p))
			total += 1

		# handle if any exceptions are thrown during the download process
		except:
			print("[INFO] error downloading {}...skipping".format(p))
			total_download_error += 1
			

	# loop over the image paths we just downloaded
	imagelist = os.listdir(destination_path)
	for imagePath in imagelist:
		imagePath = os.path.sep.join([destination_path,  imagePath])
		# initialize if the image should be deleted or not
		delete = False
	 
		# try to load the image
		try:
			image = cv2.imread(imagePath)
	 
			# if the image is `None` then we could not properly load it
			# from disk, so delete it
			if image is None:
				delete = True
	 
		# if OpenCV cannot load the image then the image is likely
		# corrupt so we should delete it
		except:
			#print("Except")
			delete = True
	 
		# check to see if the image should be deleted
		if delete:
		
			print("[INFO] deleting {}".format(imagePath))
			os.remove(imagePath)
			total_file_error += 1
	
	print("\nRESULT {} :".format(urllist[:-4]))
	print("\tTotal Success       : {}".format(total - total_file_error))
	print("\tTotal Failed        : {}".format(total_download_error))
	print("\tTotal Image Broken  : {}".format(total_file_error))
	
	#input("\npress enter to continue...")
	








		
