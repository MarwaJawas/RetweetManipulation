
#create table in sqlite3
import sqlite3 as lite
import sys
 
try:
    
    con = lite.connect('yourDataBaseName.db')
    cur = con.cursor()
    cur.execute('''
                CREATE TABLE tweet
                (tweet_id BIGINT PRIMARY KEY ,text TEXT,created_time TEXT ,
                source TEXT, retweet_count INT,favorite_count INT )
                           
                 ''')
    
    cur.execute('''
                CREATE TABLE tweeter
                (tweeter_id BIGINT PRIMARY KEY ,created_time TEXT)     
                 
                 ''')
    
    cur.execute('''
                CREATE TABLE retweeter
                (retweeter_id BIGINT PRIMARY KEY, secreen_name TEXT,user_name TEXT, description TEXT,
                followers_count INT,friends_count INT, listed_count INT, favourites_count INT, statuses_count INT,
                created_time TEXT, profile_image BOOLEAN )
                 
                 ''')
    
    
    
    cur.execute('''
                CREATE TABLE retweet
                (retweet_id BIGINT PRIMARY KEY , retweet_text TEXT, created_time TEXT,
                tweet_id BIGINT ,retweeter_id BIGINT,
                 FOREIGN KEY (tweet_id) REFERENCES tweet(tweet_id),
                 FOREIGN KEY (retweeter_id) REFERENCES retweeter(retweeter_id))
                 ''')
    
    cur.execute('''
                CREATE TABLE URL
                (tweet_id BIGINT  , URL_id INTEGER PRIMARY KEY AUTOINCREMENT ,
                 url TEXT , expanded_url TEXT, display_url TEXT,
                 FOREIGN KEY (tweet_id) REFERENCES tweet(tweet_id))
                 
                 ''')
    
    cur.execute('''
                CREATE TABLE hashtage
                (tweet_id BIGINT  , hashtage_id INTEGER PRIMARY KEY AUTOINCREMENT , text_hashtage TEXT,
                 FOREIGN KEY (tweet_id) REFERENCES tweet(tweet_id))
                 
                 ''')
    
    cur.execute('''
                CREATE TABLE mention
                (tweet_id BIGINT , mention_id INTEGER PRIMARY KEY AUTOINCREMENT ,
                 id_user_mention BIGINT ,name_mention TEXT, screen_name_mention TEXT,
                 FOREIGN KEY (tweet_id) REFERENCES tweet(tweet_id))
                 ''')
    
    con.commit()
            
except e:
    if con:
        con.rollback()
    
    print("Unexpected error %s:" % e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()
#alter table in sqlite3
import sqlite3 as lite
import sys
 
try:
    con = lite.connect('yourDataBaseName.db')
    cur = con.cursor()
    
    #con.execute("PRAGMA foreign_keys = 1")
    #con.execute("PRAGMA foreign_keys")
    
   
    

    #cur.executescript("DROP TABLE if exists URL")
    """
    cur.execute('''
                CREATE TABLE URL
                (tweet_id BIGINT NOT NULL  , url TEXT NOT NULL, expanded_url TEXT, display_url TEXT,
                
                 FOREIGN KEY (tweet_id) REFERENCES tweet(tweet_id),
                 
                 PRIMARY KEY(tweet_id,url))
                 ''')
    con.commit()
    """
    """
    cur.execute('''
                ALTER TABLE retweeter
                ADD COLUMN group_id INTEGER
                ''')
    con.commit()
    """
    """
    cur.execute("SELECT tweet_id, count (*) from retweet group by tweet_id HAVING COUNT(* )>4 ")
    #cursor.execute("SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>0"
    records = cur.fetchall()
    f=[item for item in records]
    print(f)
    """
            
except e:
    if con:
        con.rollback()
    
    print("Unexpected error %s:" % e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()

conn.execute("PRAGMA foreign_keys = 1")
cur=conn.cursor()

