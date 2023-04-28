# txt文档处理
import pandas as pd
import numpy as np
import re

# read file and index
f = open("test01_uedata")
line = f.readline()
print(line)
bandwidth = []
jitter = []
packetloss = []

# remove pre 5 unstable lines
for i in range(5):
    test = f.readline()
    print(test)
    
# read parameter
for i in range(295):
    data = f.readline()
    data = re.findall(r"\d+\.?\d*",data) #filter the number in str
    l = len(data)
    bandwidth.append(data[4])
    jitter.append(data[5])
    packetloss.append(data[8])

    print(bandwidth[i],jitter[i],packetloss[i])

f.close()
print(type(bandwidth))
print(type(jitter))

print(np.array(bandwidth).shape)
result = [bandwidth, jitter, packetloss]
result = list(zip(*result)) # Row-column interchange
print(np.array(result),shape)

name = ['bandwidth','jitter','packet_loss']
ue_data = pd.DataFrame(columns=name, data=result)
print(ue_data.head(10))
ue_data.to_csv('../ue_data.csv',encoding='gbk', index = False)
