import bs4 as bs
import urllib
import pandas as pd 
import pickle


def sec_dataframe():

	source = urllib.urlopen('https://www.sec.gov/help/foiadocsinvafoiahtm.html').read()
	soup = bs.BeautifulSoup(source,'lxml')
	table = soup.table

	urls = []
	date = []
	name = []

	for url in table.find_all('a'):
		
		urls.append('https://www.sec.gov/'+url.get('href'))
		x = url.get('href').split('/')[-1]
		dat = "20"+x[6:8]+"-"+x[2:4]+"-"+x[4:6]
		name.append(url.text)
		date.append(dat)


	df1 = pd.DataFrame(urls)
	df1['Date'] = pd.DataFrame(date)
	df1['Name'] = pd.DataFrame(name)
	df1.columns = ['File_Url','Date','Name']
	df1['Type'] = ''
	for i in range(0,df1.shape[0]):
		x = 'Exempt'
		if x in df1.Name[i]:
			df1['Type'][i] = 'exempt'
		else:
			df1['Type'][i] = 'Non-exempt'
	del df1['Name']
	return df1

df = sec_dataframe() 
df.to_pickle('fun1.pickle') 