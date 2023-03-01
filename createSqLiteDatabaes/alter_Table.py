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
