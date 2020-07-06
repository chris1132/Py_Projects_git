import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
titanic
survived       891 non-null int64
pclass         891 non-null int64
sex            891 non-null object
age            714 non-null float64
sibsp          891 non-null int64
parch          891 non-null int64
fare           891 non-null float64
embarked       889 non-null object
class          891 non-null category
who            891 non-null object
adult_male     891 non-null bool
deck           203 non-null category
embark_town    889 non-null object
alive          891 non-null object
alone          891 non-null bool
'''
titanic=sns.load_dataset('titanic')
tips=sns.load_dataset('tips')
iris = sns.load_dataset('iris')
#tips = pd.read_csv("../csv-data/tips.csv")

#sns.stripplot(x='who',y='age',data=titanic,jitter=True)
#sns.swarmplot(x='who',y='age',data=titanic,hue='sex')
#sns.boxplot(x='who',y='age',data=titanic,hue='sex')
#sns.violinplot(x="total_bill",y="day",hue="time",data=tips)
#sns.barplot(x="sex",y="survived",hue="class",data=titanic)
#sns.countplot(x="deck", hue="class",data=titanic, palette="Greens_d")
#sns.factorplot(x="time", y="total_bill", hue="smoker",col="day", data=tips, kind="box", size=4, aspect=.5)
sns.factorplot(x="time", y="total_bill", hue="smoker",col="day", data=tips, kind="swarm")
plt.show()