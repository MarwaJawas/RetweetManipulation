import json
with open('retweeter_group_alhilal_without1-5.json','r') as reader:
        
    for line in reader:
        #discard empty file
        if line.strip():
            retweeter_group_read=json.loads(line)
            #check item is dict object
            if isinstance(retweeter_group_read, dict):
                #check key "group_id" if exist in dict object
                if "group_id" in retweeter_group_read.keys():
                    group_id=retweeter_group_read["group_id"]
                    
                    print(group_id)
                    print("\n")
                    #print("mmm")
                else:
                    continue
            else: 
                continue
        else:
              continue
    print("wooow")   