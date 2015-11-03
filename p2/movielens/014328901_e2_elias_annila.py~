from __future__ import division
import sys, ast
import loadmovielens as reader
import numpy as np

"""
============================================
DO NOT FORGET TO INCLUDE YOUR STUDENT ID
============================================
"""
student_ID = '014328901'


"load the data into python"
ratings, movie_dictionary, user_ids, item_ids, movie_names = reader.read_movie_lens_data()

def my_info():
    """
    :return: DO NOT FORGET to include your student ID as a string, this function is used to evaluate your code and results
    """
    return student_ID


def Jaccard_Coefficient(movie_id_1, movie_id_2):
	seen1 = set([])
	seen2 = set([])
	for	rating in ratings:
		if rating[1] == movie_id_1:
			seen1 = seen1.union([rating[0]])
		if rating[1] == movie_id_2:
			seen2 = seen2.union([rating[0]])
	seenBoth = seen1.intersection(seen2)
	seenEither = seen1.union(seen2)

	return round(len(seenBoth)/len(seenEither), 3)


def Correlation_Coefficient(movie_id_1, movie_id_2):
	"""
	:param movie_id_1: (integer) id regarding the first movie
	:param movie_id2: (integer) id regarding the second movie
	:return: (float) Correlation_Coefficient regarding these movies based on the given movie IDs.
	ROUND OFF TO THREE DECIMAL DIGITS
	"""
	seen = {}
	for	rating in ratings:
		if not rating[1] in seen:
			seen[rating[1]] = {}
		seen[rating[1]][rating[0]]=rating[2]

	users1 = set(seen[movie_id_1].keys())
	users2 = set(seen[movie_id_2].keys())

	seenBoth = users1 & users2

	scores1 = []
	scores2 = []

	for user in seenBoth:
		scores1 = np.append(scores1, seen[movie_id_1][user])
		scores2 = np.append(scores2, seen[movie_id_2][user])
	coef = np.corrcoef(scores1, scores2)[0, 1]
	return round(coef, 3) 


def main():
    """
    DO NOT TOUCH THIS FUNCTION. IT IS USED FOR COMPUTER EVALUATION OF YOUR CODE
    """
    test_cases = ast.literal_eval(sys.argv[1])
    results = str(my_info()) + '\t\t'
    for test_case in test_cases:
        mode = test_case[0]
        id_1 = int(test_case[1])
        id_2 = int(test_case[2])
        if mode == 'jc':
            results += str(Jaccard_Coefficient(id_1, id_2)) + '\t\t'
        elif mode == 'cc':
            results += str(Correlation_Coefficient(id_1, id_2)) + '\t\t'
        else:
            exit('bad command')
    print results + '\n'

if __name__ == '__main__':
    main()


