import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("mpg_ggplot2.csv")
data = data[["class","hwy"]]

# matplotlib
plt.figure(figsize=(6.4,4.8),dpi=200)
X=[]
Y=[]
for c in data["class"].unique():
    X.append(c)
    Y.append(data[data["class"]==c]["hwy"].values)

plt.violinplot(
    dataset=Y,
    widths=0.9
    )
plt.xlabel("class")
plt.ylabel("hwy")
plt.xticks(ticks=range(1,len(X)+1),labels=X)
plt.savefig("pic01.png")


# seaborn
plt.figure(figsize=(6.4,4.8),dpi=200)
sns.violinplot(
    x="class",
    y="hwy",
    data=data,
    notch=False
    )
plt.savefig("pic02.png")

