import os

def find_closest_file (ctime, directory = "/home/s/sievers/hans1/orbcomm_tles"):
	tle_files = [f for f in os.listdir(directory) if (f[:13] == "orbcomm_tles_")]
	#ctimes = []
	#for f in tle_files:
	#	ctimes.append(f[13:-4])
	
	if len(tle_files) == 0:
		print("No tle files found in directory which start with 'orbcomm_tles_'")
		return ""
	else:
		currentBest = 0
		currentBestIdx = 0
		for i in range(len(tle_files)):
			if ((i == 0) or (abs(float(tle_files[i][13:-4]) - ctime) < currentBest)):
				currentBest = abs(float(tle_files[i][13:-4]) - ctime)
				currentBestIdx = i
		
		return tle_files[currentBestIdx]
