# Detect fake retweeters on Twitter's network


This repository contains the source code of my master's thesis :mortar_board: titled (Structures of Retweets Manipulation on Twitter: Case Study of Trending Topics in Saudi Arabia), 
 you can find it in this link in [Thesis](<https://kausp.sa/Details/Thesis/146506/>)

I developed a new method that detects fake retweeter's based on their Twitter's connection and some features. It consists of 4 components:<br>
1. collecting data Using Twitter API 
2. extracting data and building a database 
3. building a graph based on user's retweeting activity 
4. extract some features: temporal, profile,  connection in the network 

Finally, that results in predict fake retweeters based on top important feature. \
All code with Python \
[![Python](https://img.shields.io/badge/Python-3.7-green)](https://www.python.org/) 
[![Tweepy](https://img.shields.io/badge/Tweepy-3.3.7-blue)](<https://docs.tweepy.org/en/stable/getting_started.html>)

# Getting Started
## Collecting Twitter's data
### Installing
install tweepy packages that can be installed using pip:

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
4. download [create database](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/createSqLiteDatabaes/create-Table.py>) to create sqLite database
5. download [insert data](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/createSqLiteDatabaes/insert-Data.py>) and set name of the database
6. download [construct graph](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/Graph%20Construction/base_graph_to_rt_graph.py>)
7. download [extracting features](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/feature%20engineering/all_features.py>)
8. download [machine learning test](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/feature%20engineering/classification.py>) 

```
pip install tweepy
pip install combinations
pip install sqlite3 
pip install networkx
pip install community
pip install pandas
```
