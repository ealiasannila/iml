from __future__ import division
import numpy as np
import mnist_load_show as mnist
import random as random



'''
use pdis in order to find the the distance
'''
from scipy.spatial.distance import cdist

"""
============================================
DO NOT FORGET TO INCLUDE YOUR STUDENT ID
============================================
"""
student_ID = '014328901'


X, y = mnist.read_mnist_training_data(5000)

trX = X[0:2500]
trXf = [x.flatten() for x in trX]
trY = y[0:2500]

teX = X[2500:5000]
teXf = [x.flatten() for x in teX]
teY = y[2500:5000]


def my_info():
    """
    :return: DO NOT FORGET to include your student ID as a string, this function is used to evaluate your code and results
    """
    return student_ID

def doKNN(k):
	dm = cdist(teXf, trXf,'euclidean')
	cfm = np.zeros((10,10), dtype = int)
	for	a in range(0,len(dm)):
		knn = np.argpartition(dm[a], k)[:k]
		preds = trY[knn]
		counts = np.bincount(preds)
		pred = -1
		if len(counts)>=2:
			top2 = np.argpartition(-counts, 1)	
			if counts[top2[0]] == counts[top2[1]]:
				d = 99999
				for i in xrange(0,len(knn)):
					val = dm[a][i]
					if val < d:
						d = dm[a][i]
						pred = trY[knn[i]]
			else:		
				pred = top2[0]
		else:
			pred = 0
		#print pred
		#mnist.visualize(teX[a])
		cfm[teY[a]][pred] += 1
	#print cfm
	#print "ER: ", 1 - np.sum(np.diagonal(cfm))/np.sum(cfm)
	
	return cfm


def KNN():
	"""
	Implement the classifier using KNN and return the confusion matrix
	:return: the confusion matrix regarding the result obtained using knn method
	"""
	return doKNN(3)



def verify(n, xs, ys):
	for i in random.sample(range(0,len(xs)), n):
		print ys[i]
		mnist.visualize(xs[i])

#verify(5, teX, teY)


def simple_EC_classifier():
	"""
	Implement the classifier based on the Euclidean distance
	:return: the confusing matrix obtained regarding the result obtained using simple Euclidean distance method
	"""

	cfm = np.zeros((10,10), dtype = int)
	digitn = [0]*10
	avgImg = np.zeros((10,28,28))
	
	trd = np.zeros((10,28*28), dtype = int)
	for	i in xrange(0,len(trX)):
		digit = trY[i]
		digitn[digit] += 1
		avgImg[digit] = np.sum([avgImg[digit], trX[i]], axis = 0)
	for	d in xrange(0, len(trd)):
		avgImg[d] = np.divide(avgImg[d], digitn[d])
	avgFlat = np.zeros((10,28*28), dtype = int)
	for i in xrange(0, len(avgImg)):
		avgFlat[i] = avgImg[i].flatten()
	dm = cdist(teXf, avgFlat,'euclidean')
	for	a in range(0,len(dm)):
		pred = np.argmin(dm[a])
	
		cfm[teY[a]][pred] += 1	
	#mnist.visualize(avgImg[0:10])
	#print cfm
	#print "ER: ", 1 - np.sum(np.diagonal(cfm))/np.sum(cfm)
	#print ""
	return cfm




def main():
    """
    DO NOT TOUCH THIS FUNCTION. IT IS USED FOR COMPUTER EVALUATION OF YOUR CODE
    """
    results = my_info() + '\t\t'
    results += np.array_str(np.diagonal(simple_EC_classifier())) + '\t\t'
    results += np.array_str(np.diagonal(KNN()))
    print results + '\n'

if __name__ == '__main__':
    main()
