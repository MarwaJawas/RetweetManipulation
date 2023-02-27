#%matplotlib inline
#import matplotlib.pyplot as plt
#from mediaviz.draw import draw_forceatlas2_network
#from mediaviz.viz_parser import parse_colors, parse_size
from itertools import combinations
#from tqdm import tqdm
from community import community_louvain
from networkx.algorithms.clique import find_cliques 
import networkx as nx
#from networkx.algorithms import bipartite
import sqlite3 
import sys
#import time
import uuid
import pandas as pd
import json
import numpy
from tqdm import tqdm

# Initial Variables
count_group=0

def candidate_rt_graph(list_nodes_retweeter,name_db):
   
    #base graph is directed graph
    base_graph = nx.DiGraph()

    #retweeter graph is undirected graph
    candidate_rt_graph = nx.Graph()
    
    tuple_set_retweeter=tuple(list_nodes_retweeter)
    
    with sqlite3.connect(name_db) as conn:
        cursor = conn.cursor()    
        q="SELECT retweeter_id, tweet_id FROM retweet WHERE retweeter_id IN %s" % (tuple_set_retweeter,)
        #cursor.execute("SELECT retweeter_id, tweet_id FROM retweet WHERE retweeter_id IN %s" % (tuple_set_retweeter,))
        for record in cursor.execute(q):
            if record!=None:
                base_graph.add_edge(record[0],record[1], weight=1)
        
    for node,deg in tqdm(base_graph.out_degree(base_graph)):
        if deg==0:
            retweeters_nodes=(node for node in base_graph.predecessors(node))
            for v in combinations(retweeters_nodes,2):
                if candidate_rt_graph.has_edge(v[0],v[1]):
                    candidate_rt_graph[v[0]][v[1]]['weight']+= 1     
                else:
                    candidate_rt_graph.add_edge(v[0],v[1],weight=1)
        
    #Cleaning the Garbage        
    #base_graph.clear()
    del base_graph
    #edges_less_weight = [(u, v,d) for (u, v, d) in candidate_rt_graph.edges(data=True) if d['weight'] < 3]
    candidate_rt_graph.remove_edges_from([(u, v,d) for (u, v, d) in candidate_rt_graph.edges(data=True) if d['weight'] < 3])
    #del edges_less_weight
    candidate_rt_graph.remove_nodes_from(list(nx.isolates(candidate_rt_graph)))
    print("Graph was created..")
    
    return candidate_rt_graph

def prune_candidate_graph(candidate_rt_graph):
    #list_connected_component=[]
    list_connected_component=list(c for c in nx.connected_components(candidate_rt_graph) if len(c)>2)
    #print(len(list_connected_component))
    for cc in list_connected_component:
    #for cc in list( nx.connected_components(candidate_retweeter_group)):
        #connected_component= Get_retweeter_groups.subgraph(cc).copy()
        connected_component= candidate_rt_graph.subgraph(cc)
         #[G.subgraph(c).copy() for c in connected_components(G)]
        
        #cliques = sorted (list(frozenset(c) for c in nx.find_cliques(connected_component) if len(c)>2 ) , key=len, reverse=True)
        cliques = [c for c in tqdm(nx.find_cliques(connected_component)) if len(c)>2 ] 
        cliques.sort( key=len , reverse=True)
        print("finding the cliques of graph was finished..")
        
        #print(len(cliques))
        #remove overlapping cliques
        for c1, c2 in tqdm(combinations(cliques, 2)):
            
            if len(set(c1).intersection(set(c2))) >0:
                if c2 in cliques:
                    cliques.remove(c2)
        #print(cliques)
        print("remove overlapping cliques was done..")
        
        for cur_community in cliques:
            #sub_group+=1
            #print ("sub group: ", sub_group)
            #cur_community=list(cl)
            neighborList=[]
            growing_threshold=len(cur_community) * 0.7
            #print(cur_community)
            
            
            for node in cur_community:
                neighborList.extend(list(n for n in connected_component.neighbors(node)))
                
            
            candidates_nodes =set (neighborList).difference(set(cur_community))
            
            neighborList.clear()
            
            
            #candidates_nodes = set(n for n in connected_component.nodes()).difference(set(cur_community))
            
            growingList = cur_community
            
            for n in list(candidates_nodes):
                #print(n)
                incomingEdgeCount=set(cur_community).intersection(set(n for n in connected_component.neighbors(n)))
                if len(incomingEdgeCount)>= growing_threshold:
                    growingList.append(n)
                   
            #print(growingList)       
            #saveing new cur_community to database
            global count_group
            count_group+=1
            if write_Filejson(growingList):
                print("Retweeter group ",count_group ," was written to json file...")
            
            #Generate sub retweeter graph (and export to CSV)
            """
            if save_csv(connected_component , growingList ,count_group): 
                print ('sub retweeter graph ',count_group ,' was generated and its data was exported to csv file')
            
            """
            #Generate sub retweeter graph (and export to CSV)
            #draw_subGraph(connected_component , growingList ,count_group)
            
    return True
    

def convert(o):
    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError

#save id of retweeter group in json file    
def write_Filejson(retweeters_ids): 
    id_group = uuid.uuid4()
    json_data = {}
    json_data["group_id"]=id_group.hex
    json_data["members_id"]=retweeters_ids
    json_data["label"]=False
    #json.dumps({'value': numpy.int64(42)}, default=convert)
    json.dump(json_data, output, default=convert)
    #json.dump(json_data, output)
    output.write('\n')
    return True

def save_csv(connected_component , finall_retweeters_ids,count_group):
    
    sub = connected_component.subgraph(finall_retweeters_ids)
    graph_information = pd.DataFrame(sub.edges.data())
    graph_information2 = pd.DataFrame(columns = ["source", "target","type" ,"weight"]) 
    graph_information2["source"]=graph_information[0].apply(lambda x: x)
    graph_information2["target"]=graph_information[1].apply(lambda x: x)
    graph_information2["weight"]=graph_information[2].apply(lambda x: x['weight'])
    graph_information2["type"]="Undirected"
    #file_name='%s_%s.csv' % ('Network_structure_group', time.strftime('%Y%m%d-%H%M%S'))
    file_name='%s_%s.csv' % ('Network_structure_group', count_group)
    graph_information2.to_csv(file_name,index=False,mode='w')
    return True

def save_csv_version2(graph ,file_name):
    
    
    graph_information = pd.DataFrame(graph.edges.data())
    graph_information2 = pd.DataFrame(columns = ["source", "target","type" ,"weight"]) 
    graph_information2["source"]=graph_information[0].apply(lambda x: x)
    graph_information2["target"]=graph_information[1].apply(lambda x: x)
    graph_information2["weight"]=graph_information[2].apply(lambda x: x['weight'])
    graph_information2["type"]="Undirected"
    graph_information2.to_csv('%s.csv' % (file_name), index=False,mode='w')
    return True

"""
def draw_subGraph(connected_component , finall_retweeters_ids,count_group):
    sub = connected_component.subgraph(finall_retweeters_ids)
    #draw_forceatlas2_network(sub,node_color='purple',with_labels=True, adjust_labels=True, node_size=10, edge_color='gray')    
    network="Network structure of group: "
    draw_forceatlas2_network(sub,node_color='purple', title="%s%s" % (network, count_group), edge_color='black')     
    nx.draw(sub,with_labels=True)  
    plt.show()
    return True
"""



# 1)open json file
output  = open("aletihad_alhilal_com1.json","w")

#2) read parition of base graph based on Louvain algorithm
dict_partition = {row[0] : row[1] for _, row in pd.read_csv("aletihad_alhilal_com1.csv").iterrows()}



for com in set(dict_partition.values()):
    
    list_nodes_retweeter=[]
    list_nodes_retweeter = [nodes for nodes in dict_partition.keys()if dict_partition[nodes] == com]
    
    candidate_graph=candidate_rt_graph(list_nodes_retweeter,'aletihad_alhilal.db')
    
    # 3)prune candidate retweeter graph
    if prune_candidate_graph(candidate_graph):
        print("Pruning of the candidate group ", com," has been completed   ... ")
"""
com_list=[1,2,3]

for com in set(dict_partition.values()):
    
    
    if not com in com_list:
        list_nodes_retweeter=[]
        list_nodes_retweeter = [nodes for nodes in dict_partition.keys()if dict_partition[nodes] == com]
    
        candidate_graph=candidate_rt_graph(list_nodes_retweeter,'Retweet_manipulation3.db')
    
        # 3)prune candidate retweeter graph
        if prune_candidate_graph(candidate_graph):
            print("Pruning of the candidate group ", com," has been completed   ... ")
            
 
    #count_group+=1
list_nodes_retweeter=[]
list_nodes_retweeter = [nodes for nodes in dict_partition.keys()if dict_partition[nodes] == 31]

candidate_graph=candidate_rt_graph(list_nodes_retweeter,'Retweet_manipulation3.db')
save_csv_version2(candidate_graph ,"begin graph31")
#partitions = community_louvain.best_partition(candidate_graph, resolution=1.0)
#print("modularity:  ", community_louvain.modularity(partitions , candidate_graph))
#pd.DataFrame(partitions.items(),columns=['id','value']).to_csv('partitions_alhilal_aziz_com1.csv' ,index=False,mode='w')
#print(nx.graph_number_of_cliques(candidate_graph))
# 3)prune candidate retweeter graph
#if prune_candidate_graph(candidate_graph):
    #print("Pruning of the candidate group 1 has been completed   ... ")


partitions = community_louvain.best_partition(candidate_graph, weight='weight',resolution=3.0)
#print("modularity:  ", community_louvain.modularity(partitions , candidate_graph))
pd.DataFrame(partitions.items(),columns=['id','value']).to_csv('partitions_alhilal_com2.csv' , index=False,mode='w')
print("finishing best partition louvain")

#if save_csv_version2(candidate_graph ,"candidate_graph0"):
    #print("finish")
# 3)prune candidate retweeter graph
#if prune_candidate_graph(candidate_graph):
    #print("Pruning of the candidate group 4 has been completed   ... ")
"""         
   
output.close()             