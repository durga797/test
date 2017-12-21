import pickle
import pandas as pd 
import numpy as np 
import url_download as urlz
import numpy as np 


df1 = pd.read_pickle('fun2.pickle')
df = pd.DataFrame()
for i in df1.File_Url:
	z = urlz.dlfile(i)
	xl = pd.read_excel(z)
	df = df.append(xl,ignore_index=True)
	

tf = df.loc[df['1O']=='Y']
top = pd.DataFrame()
top['Organization CRD#'] = tf['Organization CRD#']
top['1O'] = tf['1O']
top['number'] = tf['1O - If yes, approx. amount of assets']

top.number = top.number.replace({"$10 billion - $50 billion": "25", "$1 billion - $10 billion": "5",'More than $50 billion':'50',np.NaN:'2'})

top.sort_values('number',inplace=True,ascending=False)
print top.head(15)
