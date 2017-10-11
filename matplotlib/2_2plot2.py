#同时有了输入输出数据

import matplotlib.pyplot as plt

input_values=[1,2,3,4,5] #add
squares=[1,4,9,16,25]

#plt.plot(squares,linewidth=5)
plt.plot(input_values,squares,linewidth=5)


plt.title("square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)  #axis轴线tick刻度=both，字体大小

plt.show()
