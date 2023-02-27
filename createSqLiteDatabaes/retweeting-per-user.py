
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('hashtag_abdulaziz.db')
    cursor = sqliteConnection.cursor()
    
    
    #cursor.execute(''' SELECT  count (*) FROM retweet group by retweeter_id ''')
    cursor.execute('''
                 SELECT  count (*)  FROM retweet group by retweeter_id HAVING COUNT(* )>0
                    ''')
    records = cursor.fetchall()
    #print(len(records))
    ret_abdulaziz=[item[0] for item in records]
    print(len(ret_abdulaziz))

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
48202
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
    
    
    cursor.execute('''
                 SELECT  count (*)  FROM retweet group by retweeter_id HAVING COUNT(* )>0
                    ''')
    records = cursor.fetchall()
    
    rts_alheila=[item[0] for item in records]
    
    

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    #sqliteConnection = sqlite3.connect('Retweet_manipulation3.db')
    #sqliteConnection = sqlite3.connect('amar_malki.db')
    sqliteConnection = sqlite3.connect('amar_malki.db')
    cursor = sqliteConnection.cursor()
    
    
    cursor.execute('''
                 SELECT  count (*)  FROM retweet group by retweeter_id HAVING COUNT(* )>0
                    ''')
    records = cursor.fetchall()
    
    rts_amar_malki=[item[0] for item in records]
  

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
The SQLite connection is closed
from collections import Counter 
c = Counter(ret_abdulaziz)
#print(c)                
p=[(i, c[i] / len(ret_abdulaziz) * 100.0) for i in c]
print(p)

from collections import Counter 
c = Counter(rts_alheila)
#print(c)                
p=[(i, c[i] / len(rts_alheila) * 100.0) for i in c]
print(p)

from collections import Counter 
c = Counter(rts_amar_malki)
#print(c)                
p=[(i, c[i] / len(rts_amar_malki) * 100.0) for i in c]
print(p)

 
import plotly.graph_objects as go

import numpy as np
x0 = rts_alheila
x1 = rts_amar_malki

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=x0,
    histnorm='percent',
    name='control', # name used in legend and hover labels
    xbins=dict( # bins used for histogram
        start=1,
        end=90,
        size=1
    ),
    marker_color='#EB89B5',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='experimental',
    xbins=dict(
        start=1,
        end=90,
        size=1
    ),
    marker_color='#330C73',
    opacity=0.75
))

fig.update_layout(
    title_text='Sampled Results', # title of plot
    xaxis_title_text='number of retweeting', # xaxis label
    yaxis_title_text='user', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)

fig.show()
#fig.savefig('persent retweeting.png')
import plotly.graph_objects as go

import numpy as np
x0 = np.random.randn(500)
x1 = np.random.randn(500) + 1

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=x0,
    histnorm='percent',
    name='control', # name used in legend and hover labels
    xbins=dict( # bins used for histogram
        start=-4.0,
        end=3.0,
        size=0.5
    ),
    marker_color='#EB89B5'
))
fig.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='experimental',
    xbins=dict(
        start=-3.0,
        end=4,
        size=0.5
    ),
    marker_color='#330C73'
))

fig.update_layout(
    title_text='Sampled Results', # title of plot
    xaxis_title_text='Value', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)

fig.show()
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
x0 = np.random.randn(500)
x1 = np.random.randn(500)+1

trace1 = go.Histogram(
    x=x0,
    histnorm='percent',
    name='control',
    xbins=dict(
        start=-4.0,
        end=3.0,
        size=0.5
    ),
    marker=dict(
        color='#FFD7E9',
    ),
    opacity=0.75
)
trace2 = go.Histogram(
    x=x1,
    name='experimental',
    xbins=dict(
        start=-3.0,
        end=4,
        size=0.5
    ),
    marker=dict(
        color='#EB89B5'
    ),
    opacity=0.75
)
data = [trace1, trace2]

layout = go.Layout(
    title='Sampled Results',
    xaxis=dict(
        title='Value'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.2,
    bargroupgap=0.1
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='styled histogram')
