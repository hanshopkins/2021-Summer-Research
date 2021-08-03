import urllib.request
import time
import os

while True:
	infile = urllib.request.urlopen("https://www.celestrak.com/NORAD/elements/orbcomm.txt")
	outname = "orbcomm_tles_"+repr(time.time())+".txt"
	outfile = open(outname, "w")
	outfile.write(infile.read().decode('utf-8'))
	infile.close()
	outfile.close()
	
	try:
		tempfile = open("latest.txt", "r")
	except:
		tempfile = open("latest.txt", "w")
		tempfile.close()
		tempfile = open("latest.txt", "r")
	finally:
		outfile = open(outname, "r")
		if tempfile.read() == outfile.read():
			outfile.close()
			tempfile.close()
			os.remove(outname)
		else:
			tempfile.close()
			tempfile = open("latest.txt", "w")
			outfile = open(outname, "r") #I don't know why this line is necessary buit it is
			tempfile.write(outfile.read())
			outfile.close()
			tempfile.close()
	time.sleep(3600)
