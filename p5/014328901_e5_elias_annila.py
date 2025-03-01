from __future__ import division
import numpy as np
import matplotlib.pyplot as plt



def f(x):
	return 2+x-0.5*(x**2)

def drawPoints(n):
	def drwaYs(x):
		return f(x)+np.random.normal(0, 0.4)
		
	xs = np.random.uniform(-3,3,n)
	xs = np.sort(xs)
	ys = [ drwaYs(x) for x in xs]
	
	return [xs, ys]	


def plotData(xs, ys, pxs, pys):
	plt.scatter(xs, ys)
	plt.plot(pxs, pys, color = 'red')
	plt.axis([-3,3,-6,6])
	plt.show()

def fitPolynomial(deg, xs, ys):
	coefficients = np.polyfit(xs,ys, deg)
	return np.poly1d(coefficients)

def plotCurves(xs, ys):
	for d in xrange(0,11):
		print d
		poly = fitPolynomial(d,xs,ys)
		xplot = np.arange(-3,3,0.1)
		plotData(xs, ys ,xplot, poly(xplot))
		
def r2(ys, yhats):
	avg = np.mean(ys)
	ssres = np.sum([ (ys[i] - yhats[i])**2 for i in xrange(0,len(ys))])
	sstot = np.sum([ (ys[i] - avg)**2 for i in xrange(0,len(ys))])
	return 1-(ssres/sstot)

def plotR2(xs, ys):
	r2s = np.ndarray(11)
	for d in xrange(0,11):
		poly = fitPolynomial(d,xs,ys)
		yhats = poly(xs)
		r2s[d] = r2(ys, yhats)
	plt.plot(np.arange(0,11,1), r2s)
	plt.show()

def cv(xs,ys):
	errorsums = np.zeros(11)
	bestdeg = 0

	
	def sqerror(y, yhat):
		return (y-yhat)**2

	segment = len(xs)/10
	for d in xrange(0,11): #each K
		for i in xrange(0,10): #each segment
			trp = 0 #points next position in train arrays
			tep = 0 #points next position in test arrays
			tsi = segment*i #Testdata start index
			xtrain = np.ndarray(len(xs)-segment)
			ytrain = np.ndarray(len(xs)-segment)
			xtest = np.ndarray(segment)
			ytest = np.ndarray(segment)
			for j in xrange(0,len(xs)): #divide data
				if j<tsi or j>=tsi+segment:
					xtrain[trp] = xs[j]
					ytrain[trp] = ys[j]
					trp+=1
				else:
					xtest[tep] = xs[j]
					ytest[tep] = ys[j]
					tep+=1
			polynomial = fitPolynomial(d, xtrain, ytrain)
			for k in xrange(0, len(ytest)):
				errorsums[d] += sqerror(ytest[k], polynomial(xtest[k]))
		if errorsums[d] < errorsums[bestdeg]:
			bestdeg = d
	return [bestdeg,errorsums]

def plotSqErSum(errorsums):
	plt.plot(np.arange(0,11,1), errorsums)
	plt.show()

def printCoef(d, xs, ys):
	print "best fitting polynommial was of", d,"nd degree"
	print "coefficients: ", fitPolynomial(d,xs,ys)
	
def main():
	points = drawPoints(30)
	cvres = cv(points[0], points[1])
	plotSqErSum(cvres[1])
	printCoef(cvres[0], points[0], points[1])
	plotCurves(points[0], points[1])
	plotR2(points[0], points[1])
	
main()

