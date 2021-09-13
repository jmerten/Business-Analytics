import json
import math

def getData():
    f = open('binpack.json','r')
    x = json.load(f)
    f.close()
    for i in range(len(x)):
        myData = x[i]['data']
        x[i]['data'] = {}
        for j in range(len(myData)):
            x[i]['data'][j] = myData[j]
    return x

probData = getData()
problems = range(len(probData))

items_list = [(k,v) for k,v in probData[5]['data'].items()]
items_list.sort(key=lambda x:x[1],reverse=True)
print(len(items_list))
print(items_list)
# for i in items_list:
#     print(i[0],'\n',i[1])

bins = {}
cap = probData[3]['cap']
num_bin = math.ceil(sum(probData[3]['data'].values()) / cap)

for i in range(1,num_bin):
    new_items = []
    item_val = []
    # print(items_list)
    for j in items_list:
        # print(len(items_list))
        # print(sum(item_val)+j[1])
        print(items_list.index(j))
        if items_list.index(j) == 0:
            item_val.append(j[1])
            new_items.append(j[0])
            items_list.remove(j)
        elif sum(item_val) + j[1] <= cap:
            item_val.append(j[1])
            new_items.append(j[0])
            items_list.remove(j)
    print(item_val,new_items)
    bins[i] = (sum(item_val),new_items)


# print('cap: ',cap,'; Est. # bin: ',num_bin,'; Act # bins: ',len(bins))
print(items_list)
print(bins)