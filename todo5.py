import pickle
import pandas as pd 
import numpy as np 
import url_download as urlz
import numpy as np 
from matplotlib import pyplot as plt

url='https://doppler.finra.org/doppler-lookup/api/v1/search/firms?hl=true&nrows=99000&query=Blackstone&r=2500&wt=json'
# Load the first sheet of the JSON file into a data frame
df = pd.read_json(url, orient='columns')

# View the first ten rows

 
df1= df.results
df= df1.BROKER_CHECK_FIRM
df1 = pd.DataFrame.from_dict(df, orient="columns")
df1 = pd.DataFrame.from_dict(df1.results, orient="columns")
df1 = pd.DataFrame.from_dict(df1, orient="columns")
df2= df1.results
df1 = pd.DataFrame.from_dict(df2, orient="columns")
list1=[]
for i in df1.results:
	list1.append(i.values())
df = pd.DataFrame(list1)

print df.head()