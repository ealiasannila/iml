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
		print movie_dictionary[co[order[i]]], "Jaccard:", round(order[i],3) 
	

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
	for	rating in ratings:
		if not rating[1] in seen:
			seen[rating[1]] = {}
		seen[rating[1]][rating[0]]=rating[2]


	users1 = set(seen[id].keys())
	for movie in item_ids:
		users2 = set(seen[movie].keys())
		seenBoth = users1 & users2
		if len(seenBoth) < 3:
			continue
		scores = []
		users = []
		for user in seenBoth:
			scores = np.append(scores, seen[id][user])
			scores = np.append(scores, seen[movie][user])
			users = np.append(users, user)
			users = np.append(users, user)		

		coef = 	np.corrcoef(scores, users)[0][1]				
		corcoefs[coef] = movie

	order = sorted(corcoefs, reverse=True)
	print movie_dictionary[id], id
	print "-----"
	for i in range(1, 6):
		print movie_dictionary[corcoefs[order[i]]], "Correlation coefficient:", round(order[i],3) 


id1 =  reader.give_me_movie_id('toy', movie_dictionary)[0][0]
id2 =  reader.give_me_movie_id('little big', movie_dictionary)[0][0]

#corCoef(id1, id2)
corCoefOne(id1)
