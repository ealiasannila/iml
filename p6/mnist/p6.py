import numpy as np
import mnist_load_show as mnist
from sklearn.metrics import confusion_matrix
"""
============================================
DO NOT FORGET TO INCLUDE YOUR STUDENT ID
============================================
"""
student_ID = '014328901'


X, y = mnist.read_mnist_training_data()
xtrain = np.array([X[i] for i in xrange(0,30000)])
ytrain = np.array([y[i] for i in xrange(0,30000)])
xtest = np.array([X[i] for i in xrange(30000,60000)])
ytest = np.array([y[i] for i in xrange(30000,60000)])

def perceptron(xs, ys, t): #xs and ys must be np.arrays
	wp = np.zeros(len(xs[0])) 
	scorep = 0
	w = np.zeros(len(xs[0]))
	score = 0
	
	for epoch in xrange(0,t):
		pocketSame = True
		for i in xrange(0,len(xs)):
			yhat = np.dot(w, xs[i])
			if ys[i]*yhat > 0: #prediction correct
				score += 1
			else:
				if score > scorep:
					wp = w
					scorep = score
					pocketSame = False
				w += ys[i]*xs[i] 
				score = 0
		if pocketSame:
			break
	return wp
"""	
xsimple = np.random.rand(100,2)
ysimple = np.zeros(100)

wtrue = np.array([-1, 1])
for i in xrange(0, len(xsimple)):
	ysimple[i] = np.sign(np.dot(wtrue, xsimple[i]))
wp = perceptron(xsimple, ysimple, 1000000)
print "WP: ",wp
"""

def my_info():
    """
    :return: DO NOT FORGET to include your student ID as a string, this function is used to evaluate your code and results
    """
    return student_ID

def one_vs_all_train():
    ws = np.zeros((10,len(xtrain[0])))
    for digit in xrange(0,10):
    	ysbin = np.zeros(len(ytrain))
    	for i in xrange(0, len(ytrain)):
    		if ytrain[i] == digit:
    			ysbin[i] = 1
    		else:
    			ysbin[i] = -1
    	ws[digit] = perceptron(xtrain, ysbin, 1000000)
    return ws

def one_vs_all_classify(ws):
	yhats = np.zeros(len(ytest))
	for i in xrange(0, len(yhats)):
		bestclass = -1
		bestscore = -float("inf")
		for j in xrange(0, len(ws)):
			score = np.dot(ws[j], xtest[i])
			if score > bestscore:
				bestscore = score
				bestclass = j
		yhats[i] = bestclass
	return yhats

def one_vs_all():
	"""
	Implement the the multi label classifier using one_vs_all paradigm and return the confusion matrix
	:return: the confusion matrix regarding the result obtained using the classifier
	"""
	ws = one_vs_all_train()
	yhats = one_vs_all_classify(ws)
	
	one_vs_all_conf_matrix = confusion_matrix(ytest, yhats)
	print one_vs_all_conf_matrix
	return one_vs_all_conf_matrix

def all_vs_all_train():
	ws = np.zeros((10,10,len(xtrain[0])))
	for d1 in xrange(0,10):
		for d2 in xrange(d1+1, 10):
			ysbin = np.array([])
			xindexes = np.array([])
			for i in xrange(0, len(ytrain)):
				if ytrain[i]==d1:
					ysbin = np.append(ysbin, 1)
					xindexes = np.append(xindexes, i)
				elif ytrain[i]==d2:
					ysbin = np.append(ysbin, -1)
					xindexes = np.append(xindexes, i)
			xsbin = np.zeros((len(ysbin), len(xtrain[0])))
			for i in xrange(0, len(xsbin)):
				xsbin[i] = xtrain[xindexes[i]]
			
			w = perceptron(xsbin, ysbin, 1000000)
			ws[d1][d2] = w
			ws[d2][d1] = -1*w
	return ws
	
def all_vs_all_classify(ws):
	yhats = np.zeros(len(ytest))
	for i in xrange(len(ytest)):
		bestclass = -1
		bestscore = -float("inf")
		for d1 in xrange(0,10):
			score = 0
			for d2 in xrange(0,10):
				score += np.sign(np.dot(ws[d1][d2], xtest[i]))
			if score>bestscore:
				bestscore = score
				bestclass = d1
		yhats[i] = bestclass
	return yhats
		

def all_vs_all():
    """
    Implement the multi label classifier based on the all_vs_all paradigm and return the confusion matrix
    :return: the confusing matrix obtained regarding the result obtained using teh classifier
    """
    
    ws = all_vs_all_train()
    print "train done"
    yhats = all_vs_all_classify(ws)
    print "classification done"
    all_vs_all_conf_matrix = confusion_matrix(ytest, yhats)
    print all_vs_all_conf_matrix
    return all_vs_all_conf_matrix




def main():
    """
    DO NOT TOUCH THIS FUNCTION. IT IS USED FOR COMPUTER EVALUATION OF YOUR CODE
    """
    results = my_info() + '\t\t'
    results += np.array_str(np.diagonal(one_vs_all())) + '\t\t'
    results += np.array_str(np.diagonal(all_vs_all()))
    print results + '\t\t'

if __name__ == '__main__':
    main()
