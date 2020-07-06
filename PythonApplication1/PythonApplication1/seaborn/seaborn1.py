import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def sinplot(flip=1,subplot=211):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)

    
with sns.axes_style("darkgrid"):
    plt.subplot(211)
    sinplot()

plt.subplot(212)
sinplot()
plt.show()
