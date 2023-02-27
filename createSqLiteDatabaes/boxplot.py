
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('hashtag_abdulaziz.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_abdulaziz=[item[0] for item in records]
    
    median_value= st.median(fer_abdulaziz)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  1.8821210738143646
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_alheila=[item[0] for item in records]
    
    median_value= st.median(fer_alheila)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('amar_malki.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_amar_malki=[item[0] for item in records]
    
    median_value= st.median(fer_amar_malki)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  1.572933590576767
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('aletihad_alhilal.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_aletihad_alhilal=[item[0] for item in records]
    
    median_value= st.median(fer_aletihad_alhilal)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1
average value ferquency of retweets   :  2.4671685002895196
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('Saudi_Qatar.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_Saudi_Qatar=[item[0] for item in records]
    
    median_value= st.median(fer_Saudi_Qatar)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  1.660197263760738
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('Annual_bonus.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_Annual_bonus=[item[0] for item in records]
    
    median_value= st.median(fer_Annual_bonus)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  2.3119328493647915
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('third_World_War.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_third_World_War=[item[0] for item in records]
    
    median_value= st.median(fer_third_World_War)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  1.2635556248052353
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('jeddah.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    fer_jeddah=[item[0] for item in records]
    
    median_value= st.median(fer_jeddah)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  1.5412481299422953
The SQLite connection is closed
# identify outliers with interquartile range

import numpy as np
#from numpy import percentile
# seed the random number generator
#seed(1)
# generate univariate observations
#data = 5 * randn(10000) + 50

data=ferquency_ret_for_rts
#dataset=sorted(data)
# calculate interquartile range
#q1, q3= percentile(dataset,[25,75])
#iqr = q3 - q1
q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
#print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
#print('Percentiles: 25th=%s , 75th=%s , IQR=%s' % (q1, q3, iqr))
print('Percentiles: 25th=%s , 75th=%s , IQR=%s' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
print('lower limit =%s , upper limit =%s' %(lower, upper))
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
#print('outliers values (outliers retweeters): %s' % outliers)
print('Identified outliers (outliers retweeters): %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations (normal retweeters): %d' % len(outliers_removed))

import numpy as np
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots( figsize=(9, 9))
ax1.set_title('boxplot: frequency of retweets for each retweeter ')
#green_diamond = dict(markerfacecolor='g', marker='D')
green_diamond = dict(markerfacecolor='r')
ax1.boxplot(ferquency_ret_for_rts_abdulaziz,flierprops=green_diamond )
ax1.yaxis.grid(True)
#ax1.set_yticks([y for y in range(len(ferquency_retweets_for_retweeters))])
#ax1.set_xlabel('retweeter id')
ax1.set_ylabel('retweeting frequency ')
plt.savefig('boxplot_hashtage_alhilal.png', dpi=800)
import matplotlib as mpl
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
import arabic_reshaper

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt
## combine these different collections into a list    
#data_to_plot = [fer_alheila, fer_abdulaziz, fer_amar_malki]
data_to_plot = [fer_alheila, fer_abdulaziz, fer_amar_malki,fer_Annual_bonus,fer_aletihad_alhilal,fer_Saudi_Qatar,fer_third_World_War,fer_jeddah]
# Create a figure instance
fig = plt.figure(1, figsize=(12, 12))

# Create an axes instance
ax = fig.add_subplot(111)


# Create the boxplot
bp = ax.boxplot(data_to_plot, showfliers=False)
## Custom x-axis labels
reshaped_text = arabic_reshaper.reshape(u'#الهلال_اوراوا_ذهاب_ابطال_اسيا')
hashtage_alhilal= get_display(reshaped_text)

reshaped_text2 = arabic_reshaper.reshape(u'#عبدالعزيز_الفغم')
hashtage_abdulaziz= get_display(reshaped_text2)

reshaped_text3 = arabic_reshaper.reshape(u'#امر_ملكي')
hashtage_amar_malki= get_display(reshaped_text3)

reshaped_text4 = arabic_reshaper.reshape(u'#العلاوة_السنوية10')
hashtage_Annual_bonus= get_display(reshaped_text4)

reshaped_text5 = arabic_reshaper.reshape(u'#الاتحاد_الهلال_الدوري')
hashtage_aletihad_alhilal= get_display(reshaped_text5)

reshaped_text6 = arabic_reshaper.reshape(u'#السعودية_قطر')
hashtage_Saudi_Qatar= get_display(reshaped_text6)

reshaped_text7 = arabic_reshaper.reshape(u'#الحرب_العالمية_الثالثة')
hashtage_third_World_War= get_display(reshaped_text7)

reshaped_text8 = arabic_reshaper.reshape(u'#بجدة')
hashtage_jeddah= get_display(reshaped_text8)

ax.set_xticklabels([hashtage_alhilal, hashtage_abdulaziz , hashtage_amar_malki,hashtage_Annual_bonus,hashtage_aletihad_alhilal,hashtage_Saudi_Qatar,hashtage_third_World_War,hashtage_jeddah],rotation=45)
#ax.set_xticklabels([hashtage_alhilal, hashtage_abdulaziz , hashtage_amar_malki])
#ax.text.x([hashtage_alhilal, hashtage_abdulaziz , hashtage_amar_malki])
#ax.get_xaxis().tick_bottom()
#ax.get_yaxis().tick_left()

ax.set_ylabel('The number of frequency of retweeting per user ')
#ax.set_title('boxplot: frequency of retweeting per user in each hashtage ')
## add patch_artist=True option to ax.boxplot() 
## to get fill color
## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(markerfacecolor='#b967ff')

# Save the figure
#fig.savefig('fig1.png', bbox_inches='tight',dpi=800)
fig.savefig('frequency_retweeting_highResoulation.png', bbox_inches='tight',dpi=2000)
# Need not be sorted, necessarily
#a = (0, 1, 1, 1, 2, 3, 7, 7, 23)

def count_elements(seq):

    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

counted = count_elements(data)
counted

from collections import Counter
#Counter(ferquency_ret_for_rts_abdulaziz).most_common(10)
Counter(ferquency_ret_for_rts_abdulaziz)
#recounted = Counter(ferquency_retweets_for_retweeters)
#recounted

counted.most_common(10)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-9d3326e33938> in <module>
----> 1 counted.most_common(10)

AttributeError: 'dict' object has no attribute 'most_common'
import matplotlib.pyplot as plt


plt.bar(*zip(*counted.items()))
plt.show()

import seaborn as sns

sns.barplot(list(counted.keys()), list(counted.values()))
<matplotlib.axes._subplots.AxesSubplot at 0xb352cf8>

def ascii_histogram(seq):
    """A horizontal frequency-table/histogram plot."""
    counted = count_elements(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))
import random
random.seed(1)

vals = [1, 3, 4, 6, 8, 9, 10]
 # Each number in `vals` will occur between 5 and 15 times.
freq = (random.randint(5, 15) for _ in vals)

data = []
for f, v in zip(freq, vals):
    data.extend([v] * f)

ascii_histogram(data)
    1 +++++++
    3 ++++++++++++++
    4 ++++++
    6 +++++++++
    8 ++++++
    9 ++++++++++++
   10 ++++++++++++
import numpy as np
# `numpy.random` uses its own PRNG.
np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=500)
d[:5]
array([18.406, 18.087, 16.004, 16.221,  7.358])
hist, bin_edges = np.histogram(d)

hist
array([ 13,  23,  91, 261,  80,  21,   7,   2,   1,   1], dtype=int64)
bin_edges
array([ 2.11 ,  5.874,  9.638, 13.402, 17.166, 20.93 , 24.694, 28.458,
       32.222, 35.986, 39.749])

from bidi import algorithm as bidialg
import matplotlib.pyplot as plt
text = bidialg.get_display('مروة')
print(text)
ةورم
from bidi.algorithm import get_display
import matplotlib.pyplot as plt
import arabic_reshaper

reshaped_text = arabic_reshaper.reshape(u'لغةٌ عربيّة')
artext = get_display(reshaped_text)
print(artext)
plt.text(0.25, 0.45, artext , name = 'Times New Roman',fontsize=50)
plt.show()
ﺔﻴﺑﺮﻋ ﺔﻐﻟ


from collections import Counter 
c = Counter(ferquency_ret_for_rts_abdulaziz)
                
p=[(i, c[i] / len(ferquency_ret_for_rts_abdulaziz) * 100.0) for i in c]
print(p)

 