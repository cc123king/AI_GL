import functools 
import time
def zs(fun):
    @functools.wraps(fun)
    def x(*args,**kwargs):
        starttime=time.time()
        print("start in %s" % starttime)
        fun(*args,**kwargs)
        stoptime=time.time()
        print("stop in %s"% stoptime )
        print(stoptime-starttime)
    return x


def fib(x):
    n,a,b=0,0,1
    while n < x:
        yield b
        a,b=b,a+b
        n = n + 1
    return 'end'

@zs
def time1():
    time.sleep(4)    

if __name__=='__main__':
    f=fib(10)
    for item in f:
        print(item)
    time1()
    #print(type(fib(10)))
    #for i in fib(4):
    #    print(i)
    #print(type(f))
    #for item in f:
     #   print(item)