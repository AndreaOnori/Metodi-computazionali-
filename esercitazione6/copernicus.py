import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

datac=pd.read_csv('copernicus_PG_selected.csv')

print(datac)

gg=datac['date'].values
comean=datac['mean_co_ug/m3'].values
plt.plot(gg,comean,color='red')
plt.show()

tf=fft.fft(comean)
f=fft.fftfreq(len(comean),d=1)

plt.plot(np.abs(f[:len(f)//2])**2,np.abs(tf[:len(f)//2])**2,color='cyan')
plt.xscale('log')
plt.yscale('log')
plt.show()
