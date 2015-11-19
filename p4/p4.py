from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


errors = 0
n = 10000

for i in xrange(0,n):
	choice = np.random.choice([0, 1])
	if choice == 0:
		x1 = np.random.normal(0, 1)
		x2 = np.random.normal(0, 1)		
		if(x1**2 + x2**2)>2.957:
			errors +=1
	else:
		x1 = np.random.normal(0, 16)
		x2 = np.random.normal(0, 16)
		if(x1**2 + x2**2)<2.957:
			errors +=1

errorate =  errors/n



def drawPoints(n):

	y0 = np.ndarray((0,2))
	y1 = np.ndarray((0,2))
	for i in xrange(0,n):
		choice = np.random.choice([0, 1])
		if choice == 0:
			x1 = np.random.normal(0, 1)
			x2 = np.random.normal(0, 1)
			y0 = np.append(y0, [[x1,x2]],axis = 0)
		
		else:
			x1 = np.random.normal(0, 16)
			x2 = np.random.normal(0, 16)
			y1 = np.append(y1, [[x1,x2]], axis =0)
	return [y0, y1]


def doKNN(k, testset):
	mistakes = 0

	
	tey0d = np.argpartition(cdist(testset[0], trainCombined,'euclidean'),k-1,axis=1)
	tey1d = np.argpartition(cdist(testset[1], trainCombined,'euclidean'),k-1,axis=1)
	
	for j in xrange(0, len(tey0d)):
		right = 0
		wrong = 0
		for i in xrange(0, k):
			if tey0d[j][i]<len(train[0]):
				right += 1
			else:
				wrong += 1
		
		if(wrong>=right):
			mistakes+=1
			
	for j in xrange(0, len(tey1d)):
		right = 0
		wrong = 0
		for i in xrange(0, k):
			if tey1d[j][i]>=len(train[0]):
				right += 1
			else:
				wrong += 1
		
		if(wrong>=right):
			mistakes+=1
			
	return mistakes/len(trainCombined)
	



print"----"
train = drawPoints(500)
test = drawPoints(2000)

plt.gcf().gca().add_artist(plt.Circle((0,0), 2.957, color='black',fill=False))
plt.scatter(test[1][:,0],test[1][:,1], color='blue')
plt.scatter(test[0][:,0],test[0][:,1], color='red')


plt.axis([-30,30,-30,30])
plt.show()

kvals = np.array([1,3,5,7,9,13,17,21,25,33,41,49,57])
testError = np.array([])
trainError = np.array([])
trainCombined = np.append(train[0], train[1], axis = 0)
for k in kvals:
	testError = np.append(testError, doKNN(k, test))
	trainError = np.append(trainError, doKNN(k, train))


plt.scatter(kvals, testError, color='red')
plt.scatter(kvals, trainError,color='blue')
plt.plot(kvals, testError, color='red')
plt.plot(kvals, trainError,color='blue')
plt.plot([0, k+1], [errorate,errorate])
plt.axis([0, k+1, 0, max(np.max(testError), np.max(trainError))+0.1])

plt.show()


