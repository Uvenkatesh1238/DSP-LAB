import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,0.01,100)
f=input("f:")
fs=input("fs:")
y=np.sin(2*np.pi*f*x)
plt.plot(x,y)
plt.show()
z=np.sin(2*np.pi*fs*x)
plt.plot(x,z)
plt.show()
c=y+z
plt.plot(x,c)
plt.show()