import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi,np.pi,256,endpoint=True)
(C,S,T)=np.cos(X),np.sin(X),np.tan(X)
fig = plt.figure(figsize=(10,6),dpi=80)

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$', r'$-\pi/2$',  r'$0$', r'$\pi/2$',r'$+\pi$'])
plt.yticks([-1,0,1])

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

t=2*np.pi/3

plt.plot([t,t],[0,np.cos(t)],"b--")
plt.scatter([t,],[np.cos(t),],50,color='b')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',xy=(t,np.cos(t)),xycoords='data',
             xytext=(-90,-50),textcoords='offset points',fontsize=16,
           arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.plot([t,t],[0,np.sin(t)],"r--")
plt.scatter([t,],[np.sin(t),],50,"r")
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)), xycoords='data',
            xytext=(+10, +30), textcoords='offset points', fontsize=16,
           arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot(X,C,'b-',label='cos')
plt.plot(X,S,'--r',lw=3,label='sin')
plt.legend(loc='upper left')

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='w',edgecolor='None',alpha=0.4))

plt.show()