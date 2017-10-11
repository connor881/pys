import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=4)
    plt.show()

    keep_running=input("make another walk?(y/n):")

    if keep_running=='n':
        break
