import urllib.request
import time
import os

while True:
	infile = urllib.request.urlopen("https://www.celestrak.com/NORAD/elements/orbcomm.txt")
	outfile = open("orbcomm_tles_"+repr(time.time())+".txt", "w")
	outfile.write(infile.read().decode('utf-8'))
	infile.close()
	outfile.close()
	#os.system("scp -i ~/.ssh/<public key file> TLEs.txt username@niagara.scinet.utoronto.ca:/home/s/sievers/hans1/TLEs.txt") #this needs to be replaced with whatever key we use to access scinet
	time.sleep(3600)
