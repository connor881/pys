import matplotlib.pyplot as plt


squares=[1,4,9,16,25]

plt.plot(squares,linewidth=5)



plt.title("square Numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)  #axis轴线tick刻度=both，字体大小


plt.show()
