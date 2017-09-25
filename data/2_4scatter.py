#scatter（）散点图 含有输入输出数据

import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]


plt.scatter(x_values,y_values,s=100)

'''
plt.title("square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)  #axis轴线tick刻度=both，字体大小
'''

plt.show()
