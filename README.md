# Detect fake retweeters on Twitter's network!


This repository contains the source code of my master's thesis :mortar_board: titled (Structures of Retweets Manipulation on Twitter: Case Study of Trending Topics in Saudi Arabia), 
 you can find it in this link in [Thesis](<https://kausp.sa/Details/Thesis/146506/>)

Thesis has been proposed a new method that detects fake retweeter's based on their Twitter's connection and some features. It consists of 4 components:<br>
1. collecting data Using Twitter API 
2. extracting data and building a database 
3. building a graph based on user's retweeting activity 
4. extract some features: temporal, profile,  connection in the network 

Finally, that results in predict fake retweeters based on top important feature. \
All code with Python \
[![Python](https://img.shields.io/badge/Python-3.7-green)](https://www.python.org/) 
[![sklearn](https://img.shields.io/badge/sklearn-1.0.2-orange)](<https://scikit-learn.org/1.0/>)
[![tweepy](https://img.shields.io/badge/Tweepy-3.7.0-red)](<https://docs.tweepy.org/en/stable/changelog.html#version-3-7-0-2018-11-27>)
[![json](https://img.shields.io/badge/json-2.0.9-blue)](<https://docs.python.org/3/library/json.html>)
[![networkx](https://img.shields.io/badge/networkx-2.4-lightgrey)](<https://networkx.org/>)
[![tqdm](https://img.shields.io/badge/tqdm-4.36.1-yellowgreen)](<https://tqdm.github.io/>)
[![community](https://img.shields.io/badge/community%20-0.13-orange)](<https://pypi.org/project/communities/>)
[![pandas](https://img.shields.io/badge/pandas%20-0.25.2-brightgreen)](<https://pandas.pydata.org/>)

# Getting Started
## Collecting Twitter's data
### Installing
install tweepy and json packages that can be installed using pip:

```
pip install tweepy
pip install json
```
### Download and run  
download [Twitter keys](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/Collecting-Tweets/twitter_keys_access.py>) <br>
set your own Twitter's access keys

```
CONSUMER_KEY = ""
CONSUMER_SECRET =  ""
```

set key authentication

```
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
```
if you don't have developer account , you can sign up from [here](<https://developer.twitter.com/en/support/twitter-api/developer-account#faq-developer-account>) 


download [cursor search](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/Collecting-Tweets/CursorSearch_Rest.py>) and set hashtag name inside list
```
search_words=["#  ",
           "#  " ,
             "# "]  
```
## Storting row data in a database


### Download and run  
download [create database](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/createSqLiteDatabaes/create-Table.py>) to create sqLite database\
set your database name
```
con = lite.connect('yourDataBaseName.db')
```
download [insert data](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/createSqLiteDatabaes/insert-Data.py>) 
set name of the database
```
con = lite.connect('yourDataBaseName.db')
  
```
set file's name
```
with open('yourJsonName.json','r') as fh:
```
## Constructing graph
install many packages that can be installed using pip:
``` 
pip install networkx
pip install tqdm
pip install community 
pip install pandas
```
download [construct graph](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/Graph%20Construction/base_graph_to_rt_graph.py>)
set your database name in line 66:
```
db = 'yourDataBaseName.db'
```
set your file name in line 79:
```
if write_edgelist('yourName'): print ('Edge list was exported to file..')
```
set your file name in line 82:
```
if partition(retweeter_graph,'yourName',to_csv=True): print ('Partitions were generated and key-value list was exported to csv file')
```
## Extracting features
install many packages that can be installed using pip:
```
pip install dateutil.parser
pip install datetime
```
download [extracting features](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/feature%20engineering/all_features.py>)
and set your file name in line 397:
```
G=nx.read_weighted_edgelist("yourName.weighted.edgelist")
```
set your file name in line 400:
```
name_database='yourDataBaseName.db'
```
set your file name in line 401:
```
with open('yourJsonName.json','r') as reader:
```
set your file name in line 438:
```
df3.to_csv('yourNameFile.csv', sep=',', encoding='utf-8',index=False)
```
## predict the fake group of retweeters
install
```
pip install sklearn
pip install numpy
```
download [machine learning test](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/feature%20engineering/classification.py>) 

