import os

# read all files in specified directory and output number of lines
strFileIn = 'c:/alexey_workspace/sauder/coursera.org/coursera.org.machine-learning-002/mlclass-ex1/alexey/code-python/code/'

for filename in os.listdir(strFileIn):
	reader = open(strFileIn + filename,'r')
	lines = reader.readlines()
	print "::", filename,"-",len(lines),"lines"
	
	reader.close()