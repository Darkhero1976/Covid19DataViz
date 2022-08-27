import requests
import json
import pandas as pd
import seaborn as sns

api_url = 'https://api.covid19api.com/summary'
cov_sum = requests.get(api_url)
#print( type(cov_sum) )
#<class 'requests.models.Response'>
cov_sum_as_json = cov_sum.json()

countries = cov_sum_as_json.get('Countries')
#print(type(countries))
#<class 'list'>
countries_df = pd.DataFrame(countries)
#countries_df.head()
countries_df_sorted = countries_df.sort_values(['TotalConfirmed'], ascending=True)
#countries_df_sorted.head(8)

#For plotting 40 highest countries
highest_40 = countries_df_sorted.tail(40)
fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
ax.set_facecolor("black")
#ax.yaxis.grid(color='gray', linestyle='dashed')
ax.yaxis.grid(color='white', linestyle='dashed')
#plt.bar(np.arange(1, len(weights)+1), weights)
total = highest_40['TotalConfirmed']
#plt.bar(np.arange(1, len(total)+1), total, color='#1F77B4')
plt.bar(np.arange(1, len(total)+1), total, color='#1F77E4')
covid_labels =  highest_40['Country']
plt.xticks(np.arange( 1, len(total)+1 ), covid_labels, rotation=75)
#plt.grid('True')
sns.despine()
plt.title('\nTotal Confirmed Covid-19\nHihgest 40 Countries\n')
