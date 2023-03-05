# Annotation is performed based on two criteria.
## First, categorizing the retweeter groups based on their behaviors in retweeting on hashtag. 
If the retweeter group is retweeting a large number of retweets, the group is labeled as malicious. This feature can be measured by computing weighted degree from retweeter graph. When the weighted degrees between retweeters in group are high, this evidence to malicious retweeting behavior among them.<br />

download [read_Tweets](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/annotation/read_Tweets.py>) <br>
In line 17, set your file name
```
with open("your_File_Name.json",'r') as reader:
```
In line 28, set your database name
```
red_text_tweet(group_id,members_id ,'your_Database_Name.db')
```
## Second, categorizing the retweeter groups by looking at the content of the retweets. 
Twitter rules and policies were used as a reference for labeling process. The group is labeled as malicious if their tweets content shows one of the following: <br />
+ Multiple posts with similar promotions or similar tweet content.
+ Their tweets’ content composite from text, hashtag, mention, URL, and
image.
+ Their tweets contains similar URL to drive traffic to websites.
+ Their tweets contains mentions of similar accounts.

download [read_Tweets](<https://github.com/MarwahJawas/detect_Fake_Retweeters/blob/master/annotation/read_Tweets.py>) <br>
In line 17, set your file name
```
with open("your_File_Name.json",'r') as reader:
```
In line 28, set your database name
```
red_text_tweet(group_id,members_id ,'your_Database_Name.db')
```
