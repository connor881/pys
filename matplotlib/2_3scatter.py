#scatter（）散点图

import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)

plt.title("square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)  #axis轴线tick刻度=both，字体大小

plt.show()
