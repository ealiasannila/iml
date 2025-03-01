from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist



boundary = (32*np.log(256))/15

def drawPoints(n):

	ys = np.array([], dtype=int)
	xs = np.ndarray((0,2))
	for i in xrange(0,n):
		choice = np.random.choice([0, 1])
		x1 = 99999
		x2 = 99999
		if choice == 0:
			x1 = np.random.normal(0, 1)
			x2 = np.random.normal(0, 1)
			ys = np.append(ys,0)
		else:
			x1 = np.random.normal(0, 16)
			x2 = np.random.normal(0, 16)
			ys = np.append(ys,1)
		xs = np.append(xs, [[x1,x2]],axis = 0)
	return [ys, xs]


def doKNN(k, trxs, trys, texs, teys):
	mistakes = 0
	
	dist = cdist(texs, trxs, 'euclidean')
	knn = np.argpartition(cdist(texs, trxs, 'euclidean'), k-1, axis=1)
	for r in xrange(0, len(knn)):
		row = knn[r]
		pred = [0,0]
		for i in xrange(0, k):
			pred[trys[row[i]]] += 1
		if teys[r]!=np.argmax(pred):
			mistakes +=1
	return mistakes/len(teys)


def decbound(x):
	if x[0]**2+x[1]**2 <boundary: #defined in begining of file as result of problem 3
		return 0
	return 1
	
def bayes(texs, teys):
	mistakes= 0
	for i in xrange(0,len(texs)):
		if(teys[i]!=decbound(texs[i])):
			mistakes +=1
	return mistakes/len(teys)
		

def getErrorates(test, train, kvals):	
	errorates = np.array([])
	for k in kvals:
		errorates = np.append(errorates,doKNN(k, train[1], train[0], test[1], test[0]))
	return errorates

def plotData(data):

	x1s = np.ndarray((0,2))
	x0s = np.ndarray((0,2))

	for i in xrange(0, len(data[0])):
		if data[0][i] == 1:
			x1s = np.append(x1s, [data[1][i]], axis = 0)
		else:
			x0s = np.append(x0s, [data[1][i]], axis = 0)

	plt.gcf().gca().add_artist(plt.Circle((0,0), np.sqrt(boundary), color='black',fill=False))
	plt.scatter(x1s[:,1], x1s[:,0])
	plt.scatter(x0s[:,1], x0s[:,0], color='red')
	minmax = max(np.abs(min(x1s[:,1])),max(x1s[:,1]))
	plt.axis([-minmax,minmax,-minmax,minmax])
	plt.show()


def main():
	train = drawPoints(500)
	test = drawPoints(2000)
	kvals = np.array([1,3,5,7,9,13,17,21,25,33,41,49,57])
	bayesPoints = drawPoints(10000)
	
	bayesError =  bayes(bayesPoints[1], bayesPoints[0])
	#print bayesError
	plotData(train)
	plotData(test)
	erroratesTest = getErrorates(test, train, kvals)
	erroratesTrain = getErrorates(train, train, kvals)

	plt.plot(kvals,erroratesTest)
	plt.plot(kvals,erroratesTrain)
	plt.plot([0,max(kvals)], [bayesError, bayesError])
	plt.show()

if __name__ == '__main__':
    main()
