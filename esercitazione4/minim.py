import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
data= pd.read_csv('fit_data.csv')
print (data)

plt.plot(data['x'],data['y'],color='blue')
plt.xscale("log")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gaussiana") 
plt.show()
