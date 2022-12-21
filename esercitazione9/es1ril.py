import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import reco as rc

def imm(mod,sens,time):
    for i in range(len(mod)):
        ril[i]=rc.Hit(mod[i],sens[i],time [i])
    return ril

data0=pd.read_csv('hit_times_M0.csv')
data1=pd.read_csv('hit_times_M1.csv')
data2=pd.read_csv('hit_times_M2.csv')
data3=pd.read_csv('hit_times_M3.csv')


print (data0)

'''plt.hist(data0['hit_time'],bins=50)
plt.show()


diff=np.diff(data0['hit_time'].values)
pippo=diff>0
difflog=np.log10(diff[pippo])

plt.hist(difflog,bins=50)
plt.show()'''

#mod_id  det_id   hit_time


ril0=imm(data0['mod_id'].values,data0['det_id'].values,data0['hit_time'].values)
ril1=imm(data1['mod_id'].values,data1['det_id'].values,data1['hit_time'].values)
ril2=imm(data2['mod_id'].values,data2['det_id'].values,data2['hit_time'].values)
ril3=imm(data3['mod_id'].values,data3['det_id'].values,data3['hit_time'].values)

hits=np.append(ril0,ril1)
hits=np.append(hits,ril2)
hits=np.append(hits,ril3)


np.sort(hits)
diffhits=np.diff(hits)
pluto=diffhits>0
loghits=np.log10(diffhits[pluto])

plt.hist(loghits,bins=50)

plt.show()


