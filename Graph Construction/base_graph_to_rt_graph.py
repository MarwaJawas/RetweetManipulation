import sqlite3 
import sys
#from combinations 
from itertools import combinations
#for network creation
import networkx as nx
from collections import Counter
import time
from tqdm import tqdm
from community import community_louvain
import pandas as pd


# Initial Variables
#base graph is directed graph
base_graph = nx.DiGraph()

#retweeter graph is undirected graph
retweeter_graph = nx.Graph()

    
def load_from_db(db,q):
    try:
        sqliteConnection = sqlite3.connect(db)
        cursor = sqliteConnection.cursor()
        
        for record in cursor.execute(q):
            if record!=None:
                base_graph.add_edge(record[0],record[1], weight=1)
                
    except Exception as e:
        print (e )      
    return True
    
def gen_rt_graph():
    for node,deg in tqdm(base_graph.out_degree(base_graph)):
        if deg==0:
            retweeters_nodes=(node for node in base_graph.predecessors(node))
            for v in combinations(retweeters_nodes,2):
                if retweeter_graph.has_edge(v[0],v[1]):
                    retweeter_graph[v[0]][v[1]]['weight']+= 1     
                else:
                    retweeter_graph.add_edge(v[0],v[1],weight=1)
    return True
    
def clean_rt_graph():
    edges_less_weight = [(u, v,d) for (u, v, d) in tqdm(retweeter_graph.edges(data=True)) if d['weight'] < 3]
    retweeter_graph.remove_edges_from(edges_less_weight)
    del edges_less_weight
    retweeter_graph.remove_nodes_from(list(nx.isolates(retweeter_graph)))
    return True
    
def write_edgelist(file_name):
    nx.write_weighted_edgelist(retweeter_graph, '%s.weighted.edgelist' %(file_name))
    return True
    
def partition(graph, name, to_csv=True):
    #file_name='%s.csv' % (name)
    partitions = community_louvain.best_partition(graph)
    if to_csv:
        pd.DataFrame(partitions.items(),columns=['id','value']).to_csv('%s.csv' % (name), index=False,mode='w')
    return True


#1) load Data
db = 'yourDataBaseName.db'
q = '''SELECT retweeter_id, tweet_id FROM retweet where retweeter_id IN
    (SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(*)>2)'''

if load_from_db(db,q): print ('Data were successfully loaded...')

#2) generate retweeter_graph
if gen_rt_graph(): print ('Retweeter Graph was generated: ','#Nodes:',retweeter_graph.number_of_nodes(),' #Edges:',retweeter_graph.number_of_edges())

#3) clean retweeter_graph
if clean_rt_graph(): print ('Retweeter graph was cleaned (weight with less than 3 were removed)','#Nodes:',retweeter_graph.number_of_nodes(),' #Edges:',retweeter_graph.number_of_edges())

#4) Write edge list to a file (for later use)
if write_edgelist('aletihad_ alhilal'): print ('Edge list was exported to file..')

#5) Generate parition based on Louvain algorithm (and export to CSV)
if partition(retweeter_graph,'aletihad_ alhilal',to_csv=True): print ('Partitions were generated and key-value list was exported to csv file')
