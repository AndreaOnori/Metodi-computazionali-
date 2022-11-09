import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd

a=0
b=10
def input(t):
    if int(t)%2==0:
        return 1
    elif int(t)%2==1:
        return-1
def fode(v,t,input,rc):
    return 1/rc*(input(t)-v)

n=1010
h=(b-a)/n
tt=np.arange(a,b,h)
vi=np.zeros(len(tt))
for i in range(len(tt)): 
    vi[i]=input(tt[i])
vo=np.zeros(len(tt))
RC=[1,0.1,0.02]
for i in range(len(RC)):
    vo=integrate.odeint(fode,0,t=tt,args=(input,RC[i]))
    plt.plot(tt,vi)
    plt.plot(tt,vo,color='darkblue')
    plt.xlabel('t')
    plt.ylabel('V')
    plt.show()















    

