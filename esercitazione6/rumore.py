import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as opt
from scipy import fft

data1=pd.read_csv('data_sample1.csv')
data2=pd.read_csv('data_sample2.csv')
data3=pd.read_csv('data_sample3.csv')


'''print(data1)
print(data2)
print(data3)'''

plt.plot(data1['time'],data1['meas'],color='darkblue')
plt.plot(data2['time'],data2['meas'],color='crimson')
plt.plot(data3['time'],data3['meas'],color='limegreen')

plt.show()

ffts1=fft.fft(data1['meas'].values)
ffts2=fft.fft(data2['meas'].values)
ffts3=fft.fft(data3['meas'].values)

fftfreqs1=fft.fftfreq(len(ffts1),d=1)
fftfreqs2=fft.fftfreq(len(ffts2),d=1)
fftfreqs3=fft.fftfreq(len(ffts3),d=1)

plt.plot(fftfreqs1[0:len(fftfreqs1)//2],np.abs(ffts1[0:len(fftfreqs1)//2])**2,'o',color='darkblue')
plt.plot(fftfreqs2[0:len(fftfreqs2)//2],np.abs(ffts2[0:len(fftfreqs2)//2])**2,'o',color='crimson')
plt.plot(fftfreqs3[0:len(fftfreqs3)//2],np.abs(ffts3[0:len(fftfreqs3)//2])**2,'o',color='limegreen',)
plt.xscale('log')
plt.yscale('log')
plt.show()


def funz(x,a,b):
    return a/(x**b)


pstart1=np.array([1,0])
params1,params_covar1=opt.curve_fit(funz,fftfreqs1[30:len(fftfreqs1)//2],np.abs(ffts1[30:len(fftfreqs1)//2])**2,p0=pstart1)

print(params1)
print(params_covar1)

pstart2=np.array([-1,1])
params2,params_covar2=opt.curve_fit(funz,fftfreqs2[30:len(fftfreqs2)//2],np.abs(ffts2[30:len(fftfreqs2)//2])**2,p0=pstart1)

print(params2)
print(params_covar2)

pstart3=np.array([-1,2])
params3,params_covar3=opt.curve_fit(funz,fftfreqs3[30:len(fftfreqs3)//2],np.abs(ffts3[30:len(fftfreqs3)//2])**2,p0=pstart1)

print(params3)
print(params_covar3)
plt.plot(fftfreqs1[0:len(fftfreqs1)//2],np.abs(ffts1[0:len(fftfreqs1)//2])**2,'o',color='darkblue')
plt.plot(fftfreqs2[0:len(fftfreqs2)//2],np.abs(ffts2[0:len(fftfreqs2)//2])**2,'o',color='crimson')
plt.plot(fftfreqs3[0:len(fftfreqs3)//2],np.abs(ffts3[0:len(fftfreqs3)//2])**2,'o',color='limegreen',)
plt.plot(fftfreqs1[0:len(fftfreqs1)//2],funz(fftfreqs1[0:len(fftfreqs1)//2],params1[0],params1[1]),color='silver')
plt.plot(fftfreqs2[0:len(fftfreqs2)//2],funz(fftfreqs2[0:len(fftfreqs2)//2],params2[0],params2[1]),color='pink')
plt.plot(fftfreqs3[0:len(fftfreqs3)//2],funz(fftfreqs3[0:len(fftfreqs3)//2],params3[0],params3[1]),color='forestgreen')
plt.xscale('log')
plt.yscale('log')
plt.show()
