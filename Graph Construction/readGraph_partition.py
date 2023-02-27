from community import community_louvain 
import networkx as nx
from tqdm import tqdm
import pandas as pd
graph = nx.read_weighted_edgelist('hashtage_alhilal.weighted.edgelist',nodetype=int)


edges_less_weight = [(u, v,d) for (u, v, d) in tqdm (graph.edges(data=True)) if d['weight'] == 2]
graph.remove_edges_from(edges_less_weight)
del edges_less_weight
graph.remove_nodes_from(list(nx.isolates(graph)))
print("finishing remove edges...")

partitions = community_louvain.best_partition(graph)
pd.DataFrame(partitions.items(),columns=['id','value']).to_csv('partitions_alhilal_weightMore2.csv' , index=False,mode='w')

print("finishing best partition louvain")