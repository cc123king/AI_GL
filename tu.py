from matplotlib import pyplot as plt
import numpy as np
if __name__=='__main__':
    x=np.linspace(-1,25,30)
    y=2*x+1
    plt.plot(x,y)
    plt.savefig('static/picture/flash.jpg')
    plt.show()

