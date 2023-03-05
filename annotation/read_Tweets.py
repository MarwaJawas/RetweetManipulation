import sqlite3 
import json

def red_text_tweet(group_id,list_retweeters , name_db):
    sqliteConnection = sqlite3.connect(name_db)
    cursor = sqliteConnection.cursor()
    tuple_set_retweeter=tuple(list_retweeters)
    q="SELECT text from tweet where tweet_id IN (select tweet_id FROM retweet WHERE retweeter_id IN %s)" % (tuple_set_retweeter,)
    
    print("group_id:  ",group_id)
    for q in cursor.execute(q):
        print(q)
    print("\n\n\n")
    return
	
#set your file name	
with open("your_File_Name.json",'r') as reader:
        
    for line in reader:
        #skip empty line
        if line.strip():
            
            retweeter_group_read=json.loads(line)
            group_id=retweeter_group_read["group_id"]
            members_id=retweeter_group_read["members_id"]
            label=retweeter_group_read["label"]
            #set your database name  
            red_text_tweet(group_id,members_id ,'your_Database_Name.db')
                  
        else:
            continue
                