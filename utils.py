import numpy as np
import pickle

def score_prediction(predictions):
	actuals = pickle.load(open('./data/actuals', 'rb'))
	error = np.mean( actuals != predictions )
	if error == 0:
		print("Pass !!")
	else:
		print("Error detected ", error)
