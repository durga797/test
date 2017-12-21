import pickle
import pandas as pd 
import numpy as np 
import url_download as urlz
import numpy as np 
from matplotlib import pyplot as plt
df1 = pd.read_pickle('fun2.pickle')
df = pd.DataFrame()
for i in df1.File_Url:
	z = urlz.dlfile(i)
	xl = pd.read_excel(z)
	df = df.append(xl,ignore_index=True)
	

tf = pd.DataFrame()
tf['Main Office City'] = df['Main Office City'] 
tf['Main Office State']=  df['Main Office State']
tf['5A'] = df['5A']
for i in range(0,tf.shape[0]):
	if pd.isnull(tf['Main Office State'][i])==True:
		tf['Main Office State'][i] = 'other'

tf = tf.sort_values('5A',ascending=False)
ts1 = tf.groupby('Main Office State').sum()
#ts1.sort_values('5A',ascending=False,inplace=True)
ts1['5A'].plot()
plt.show()