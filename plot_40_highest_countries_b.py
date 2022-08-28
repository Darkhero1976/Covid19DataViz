# https://www.geeksforgeeks.org/covid-19-data-visualization-using-matplotlib-in-python/

import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

api_url = 'https://api.covid19api.com/summary'
cov_sum = requests.get(api_url)
cov_sum_as_json = cov_sum.json()
countries = cov_sum_as_json.get('Countries')
countries_df = pd.DataFrame(countries)
countries_df_sorted = countries_df.sort_values(['TotalConfirmed'], ascending=True)
highest_40 = countries_df_sorted.tail(40)

fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
ax.set_facecolor("black")
#ax.yaxis.grid(color='gray', linestyle='dashed')
ax.yaxis.grid(color='white', linestyle='dashed')
total = highest_40['TotalConfirmed']
covid_labels =  highest_40['Country']
plt.xticks(np.arange( 1, len(total)+1 ), covid_labels, rotation=75)
#plt.grid('True')
sns.despine()
plt.title('\nTotal Confirmed Covid-19\nHihgest 40 Countries (Millions)\n')

#https://stackoverflow.com/questions/38840365/pyplot-how-to-explicitly-number-an-axis-in-a-human-readable-way
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)

xdata = np.arange(1, len(total)+1)
for i,j in zip(xdata,total):
    ax.annotate(str(round(j/1000000, 1)),
                xy=(i,j+100),
                color='white',
                size='13', rotation=50)

#plt.bar(np.arange(1, len(total)+1), total, color='#1F77B4')
plt.bar(np.arange(1, len(total)+1), total, color='#1F77E4')
