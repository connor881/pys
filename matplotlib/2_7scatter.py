#scatter（）散点图 去除原点轮廓，使用颜色映射定义原点颜色

import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]#**2 2次方, **3 3次方


plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40) #使用颜色映射，数值越小颜色越浅，越大颜色越深

plt.axis=([0,1100,0,1100000])#设置每个坐标轴的的取值范围



'''
plt.title("square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)  #axis轴线tick刻度=both，字体大小
'''

plt.show()
