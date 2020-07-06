import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.titlesize']=20
mpl.rcParams['xtick.labelsize']=16
mpl.rcParams['ytick.labelsize']=16
mpl.rcParams['axes.labelsize']=16
mpl.rcParams['xtick.major.size']=0
mpl.rcParams['ytick.major.size']=0

speed_map = {
    'A':(69216,'#FFE4E1'),
    'B':(97737,'#FFC1C1'),
    'C':(30108,'#2E8ECE'),
    'D':(3541,'#40D47E'),
    'E':(155,'#E98B39')
    }

fig=plt.figure('cups')

ax=fig.add_subplot(121)
ax.set_title('bar')

xticks=np.arange(5)
bar_width = 0.4

cups = speed_map.keys()

peoples = []
colors = []
for x in speed_map.values():
    peoples.append(x[0])
    colors.append(x[1])

bars = ax.bar(xticks,peoples,width=bar_width,edgecolor='none')

ax.set_ylabel('people')

ax.set_xticks(xticks+bar_width/2)
ax.set_xticklabels(cups)
ax.set_xlim([bar_width/2-0.5,5-bar_width/2])

ax.set_ylim([0,100000])

for bar,color in zip(bars,colors):
    bar.set_color(color)

ax = fig.add_subplot(122)
ax.set_title('pie')

total = sum(peoples)
percents=[]
for x in peoples:
    print(x/total)
    percents.append(round(100*x/total,2))

labels=['{}\n{}%'.format(cup,percent) for cup,percent in zip(cups,percents)]

ax.pie(percents,labels=labels,colors=colors)

plt.show()