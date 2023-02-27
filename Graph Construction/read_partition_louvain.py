#read as dictionary
import pandas as pd

partition = {row[0] : row[1] for _, row in pd.read_csv("aletihad_ alhilal.csv").iterrows()}

for com in set(partition.values()):
    
    list_nodes_retweeter = [nodes for nodes in partition.keys()if partition[nodes] == com]
    print("com number: ",com,  "member # ",len(list_nodes_retweeter))