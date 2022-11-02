import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import pandas as pd
data= pd.read_csv('fit_data.csv')

def lognorm(dati,media,sigma,A):
     return A*np.exp(-(np.log(dati)-media)**(2)/(2*sigma**2))

pstart=np.array([np.log(100),np.log(50),120])
err=np.sqrt(data['y'])
params, params_covariance=optimize.curve_fit(lognorm,data['x'],data['y'],p0=[pstart],sigma=err,absolute_sigma=True)
print ('params', params)
print ('params_cov', params_covariance)
print ('errori params', np.sqrt(params_covariance.diagonal()))

plt.errorbar(data['x'],data['y'],yerr=err,xerr=None,ecolor='green',color='blue',label='Dati')
plt.plot(data['x'],lognorm(data['x'],params[0],params[1],params[2]),color='red',label='Fit')
plt.xscale("log")
plt.legend(fontsize=10,loc= "upper right")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gaussiana")
plt.show()

Xq=np.sum((lognorm(data['x'],params[0],params[1],params[2])-data['y'])**2/(data['y']))
ridotto=len(data['x'])-len(pstart)
print(Xq/ridotto)



