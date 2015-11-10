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



def my_info():
    """
    :return: DO NOT FORGET to include your student ID as a string, this function is used to evaluate your code and results
    """
    return student_ID


def KNN():
    """
    Implement the classifier using KNN and return the confusion matrix
    :return: the confusion matrix regarding the result obtained using knn method
    """
    knn_conf_matrix = ''
    return knn_conf_matrix


def simple_EC_classifier():
	"""
	Implement the classifier based on the Euclidean distance
	:return: the confusing matrix obtained regarding the result obtained using simple Euclidean distance method
	"""

	trX = X[0:2500]
	trY = y[0:2500]

	teX = X[2500:5000]
	teXf = [x.flatten() for x in teX]
	teY = y[2500:5000]
	cfm = np.zeros((10,10), dtype = int)
	digitn = [0]*10


	trd = np.zeros((10,28*28), dtype = int)

	def imgSum(digit, img):
		trd[digit] = np.sum([trd[digit], img], axis = 0)

	def imgDiv(digit, n):
		trd[digit] = np.divide(trd[digit], n)

	def imgAvg():
		for	i in xrange(0,len(trX)):
			digit = trY[i]
			digitn[digit] += 1
			img = trX[i].flatten()
			imgSum(digit, img)
		for	d in xrange(0, len(trd)):
			imgDiv(d, digitn[d])


	def verify(n, xs, ys):
		for i in random.sample(range(0,len(xs)), n):
			print ys[i]
			mnist.visualize(xs[i])

	
	imgAvg()

	dm = cdist(teXf, trd,'euclidean')

	for	a in range(0,len(dm)):
		pred = np.argmin(dm[a])
		cfm[teY[a]][pred] += 1	



	simple_EC_conf_martix = cfm
	return simple_EC_conf_martix




def main():
    """
    DO NOT TOUCH THIS FUNCTION. IT IS USED FOR COMPUTER EVALUATION OF YOUR CODE
    """
    results = my_info() + '\t\t'
    results += np.array_str(np.diagonal(simple_EC_classifier())) + '\t\t'
    #results += np.array_str(np.diagonal(KNN()))
    print results + '\n'

if __name__ == '__main__':
    main()
