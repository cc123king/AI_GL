from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation
if __name__=='__main__':
    fig,ax=plt.subplots()
    x=np.arange(0,2*np.pi,0.01)
    line, =ax.plot(x,np.sin(x))

    def update(i):
        line.set_ydata(np.sin(x+i/10))
        return line,
    
    def init():
        line.set_ydata(np.sin(x))
        #print(type(line,))
        return line,
    print(type(init()))
    ani=animation.FuncAnimation(fig=fig,func=update,init_func=init,interval=10,blit=False,frames=200)
    plt.show()