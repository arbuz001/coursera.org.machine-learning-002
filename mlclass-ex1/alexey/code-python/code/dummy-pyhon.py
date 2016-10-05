'''
Read all files in specified directory and output number of lines
'''

import numpy as np
import os
import pandas as pd
import paths

# strFileIn = 'c:/alexey_workspace/sauder/coursera.org/coursera.org.machine-learning-002/mlclass-ex1/alexey/code-python/data/'
# # strFileIn = paths.prj_path

# for filename in os.listdir(strFileIn):
	# reader = open(strFileIn + filename,'r')
	# lines = reader.readlines()
	# print "::", filename,"-",len(lines),"lines"
	
	# reader.close()
	
tol = 1e-5

strFileIn = 'c:/alexey_workspace/sauder/coursera.org/coursera.org.machine-learning-002/mlclass-ex1/alexey/code-python/data/ex1data1.txt'

data = pd.read_csv(strFileIn, sep=',',header=0)
# data = pd.read_csv(strFileIn)

# X = fnRemoveFeatures(data,['y'])

# g = fnSigmoid(X)

# strFileIn = paths.prj_path + '/utils/test/data-cases/data-case-7.csv'

# out2 = pd.read_csv(strFileIn, sep=',',header=0)

# assert np.amax(abs(g - out2.values)) < tol, "FAILURE in 'fnPredictFunction_test': test case-2 failed!"

print "DONE: test '" + "fnSigmoid_test" + "' completed!";