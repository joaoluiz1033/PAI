import pickle
import matplotlib.pyplot as plt
import pickle
import numpy as np
from matplotlib.ticker import MaxNLocator

def load(fileName):
    f = open(fileName, 'rb')
    obj = pickle.load(f)
    f.close()        
    vector = obj[1]
    return vector

if __name__ == "__main__":
    data = load('Simulation02_MediumvsRandom')
    #data2 = [data[6], data[0],data[1],data[2],data[3],data[4],data[5]]
    # Switching to the OO-interface. You can do all of this with "plt" as well.
    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data, width=0.6, align='center',edgecolor='black',zorder = 3)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set(xticks=range(len(data)), xlim=[-0.5, len(data)-1 + 0.5])
    xlocs = range(len(data))
    for i, v in enumerate(data):
        plt.text(xlocs[i] - 0.25, v + 0.01, str(v))
    plt.grid(zorder = 0)
    plt.title('Normal level : AI (w) vs random (b)')
    plt.savefig('Simulation02.png')