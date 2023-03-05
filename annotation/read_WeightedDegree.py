import networkx as nx
from networkx.algorithms import bipartite
import sqlite3 
import json

def create_graph(group_id,list_retweeters , name_db):
    sqliteConnection = sqlite3.connect(name_db)
    cursor = sqliteConnection.cursor()
    bipartite_graph = nx.Graph()
   
    bipartite_graph.add_nodes_from(list_retweeters, bipartite=0)
    #print (tuple(set_retweeter))
    
    tuple_set_retweeter=tuple(list_retweeters)
    #print(tuple_set_retweeter)
    
    cursor.execute("SELECT retweeter_id, tweet_id FROM retweet WHERE retweeter_id IN %s" % (tuple_set_retweeter,))
    retweeter_tweet_ids_records = cursor.fetchall()
    set_tweet=[]
    set_tweet=[row[1] for row in retweeter_tweet_ids_records]
    bipartite_graph.add_nodes_from(set_tweet, bipartite=1)
    
    
    set_edges=[]
    for row in retweeter_tweet_ids_records:
        set_edges.append((row[0], row[1])) 
    bipartite_graph.add_edges_from(set_edges)
    
    retweeter_nodes = {n for n, d in bipartite_graph.nodes(data=True) if d['bipartite']==0}
    retweeter_group_graph = bipartite.weighted_projected_graph(bipartite_graph, retweeter_nodes,ratio=False)
    
    edges_less_weight = [(u, v,d) for (u, v, d) in retweeter_group_graph.edges(data=True) if d['weight'] < 3 ]
    retweeter_group_graph.remove_edges_from(edges_less_weight)
    
    
    #data  = graph_features(retweeter_group_graph,len(user_id), label , sn)
    
    print("group_id:  ",group_id)
    print(retweeter_group_graph.degree(weight='weight'))
    #data  = graph_features(retweeter_group_graph,len(list_retweeters) , group_id)
    #bipartite_graph.clear()
    return 
	
#set your file name
with open('your_File_Name.json','r') as reader:
        
    for line in reader:
        #skip empty line
        if line.strip():
            
            retweeter_group_read=json.loads(line)
            group_id=retweeter_group_read["group_id"]
            members_id=retweeter_group_read["members_id"]
            #set your file name
            create_graph(group_id,members_id ,'your_File_Name.db')
            print("\n")
            print("\n")
            print("\n")    
        else:
            continue