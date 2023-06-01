import numpy as np
import matplotlib.pyplot as plt

def GenNormallyDistributedArray(mean = 100 ,std_dev =15,size = 100  ):
    numbers = np.random.normal(mean, std_dev, size)

    numbers = np.round(numbers).astype(int)
    plt.hist(numbers)
    plt.show()
    return numbers