from __future__ import division
import loadmovielens as reader
import numpy as np

ratings, movie_dictionary, user_ids, item_ids, movie_names = reader.read_movie_lens_data()

def jaccard(id1, id2):
	seen1 = set([])
	seen2 = set([])
	for	rating in ratings:
		if rating[1] == id1:
			seen1 = seen1.union([rating[0]])
		if rating[1] == id2:
			seen2 = seen2.union([rating[0]])
	seenBoth = seen1.intersection(seen2)
	seenEither = seen1.union(seen2)
	print len(seenBoth)/len(seenEither)


def jaccardForOne(id):
	seen = {}
	for	rating in ratings:
		if not rating[1] in seen:
			seen[rating[1]] = set()	
		seen[rating[1]].add(rating[0])

	co = {}
	for	movie in item_ids:
		seenEither = seen[id].union(seen[movie])
		seenBoth = seen[id].intersection(seen[movie])
		jac = len(seenBoth)/len(seenEither)
		co[jac] = movie
		
	order = sorted(co, reverse=True)
	print movie_dictionary[id], id
	print "-----"
	for i in range(1, 6):
		print movie_dictionary[co[order[i]]], "Jaccard:", round(order[i],3),  len(seen[co[order[i]]])
	

def corCoef(id1, id2):
	seen = {}
	for	rating in ratings:
		if not rating[1] in seen:
			seen[rating[1]] = {}
		seen[rating[1]][rating[0]]=rating[2]

	users1 = set(seen[id1].keys())
	users2 = set(seen[id2].keys())

	seenBoth = users1 & users2
	

	scores1 = []
	scores2 = []

	
	for user in seenBoth:
		scores1 = np.append(scores1, seen[id1][user])
		scores2 = np.append(scores2, seen[id2][user])
	
	print np.corrcoef(scores1, scores2)

def corCoefOne(id):
	seen = {}
	corcoefs = {}
	n = {}
	for	rating in ratings:
		if not rating[1] in seen:
			seen[rating[1]] = {}
		seen[rating[1]][rating[0]]=rating[2]


	users1 = set(seen[id].keys())
	print len(users1)//5
	for movie in item_ids:
		users2 = set(seen[movie].keys())
		seenBoth = users1 & users2
		
		if len(seenBoth)<len(users1)//5:
			continue		

		
		scores1 = []
		scores2 = []
		for user in seenBoth:
			scores1 = np.append(scores1, seen[id][user])
			scores2 = np.append(scores2, seen[movie][user])
		
		if np.std(scores1) == 0 or np.std(scores2)==0:
			continue
		coef = 	np.corrcoef(scores1, scores2)[0][1]				
	
		corcoefs[coef] = movie
		n[coef] = len(seenBoth)

	order = sorted(corcoefs, reverse=True)
	print movie_dictionary[id], id
	print "-----"
	for i in range(1, 6):
		print movie_dictionary[corcoefs[order[i]]], "Correlation:", round(order[i],3), len(seen[corcoefs[order[i]]])


id1 =  reader.give_me_movie_id('Three colors', movie_dictionary)[0][0]


jaccardForOne(id1)
corCoefOne(id1)
