import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()        #num_points个点的数据全部载入


    point_numbers=list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)#c颜色深浅，越大越深，cmap为色系,c和cmp联用


    plt.show()



    keep_running=input("make another walk?(y/n):")
    if keep_running=='n':
        break
