import pickle
import pandas as pd 
import numpy as np 
import urllib2

def get_sec_zip_by_period(is_exempt,only_most_recent):
	df = pd.read_pickle('fun1.pickle')
	exempt = ''
	if is_exempt==False:
		exempt = 'Non-exempt'
	else:
		exempt = 'exempt'
	tf = df[df.Type== exempt]
	if only_most_recent == True:
		tf.index = tf['Date']
		del tf['Date']
		tf.sort_index(ascending=False,inplace=True)
		tf1 = tf.head(1)
	else:
		tf1 = pd.DataFrame()
		for i in only_most_recent:
			tf1 = tf1.append(tf.loc[tf['Date'].str.contains(i)])
			
	return tf1

df = get_sec_zip_by_period(False,True)
df.to_pickle('fun2.pickle')