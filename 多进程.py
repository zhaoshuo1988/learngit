#from multiProcess import Process   #多进程
import threading    #多线程
import os

class MyTread(threading.Thread):
    def __init__(self,beg,end):
        super().__init__()
        self.__beg=beg
        self.__end=end
    def __IsPrim(self,n):
        for i in range(2,n):
            if n%i ==0:
                return False
        else:
            return True
    def run(self):
        for x in range(self.__beg,self.__end):
            if self.__IsPrim(x):
                print('{}进程的{}线程:{}是素数'.format(os.getpid(),threading.current_thread().name,x))
                    
if __name__ =='__main__':
    p1= MyTread(3,1001)

    p2= MyTread(1000,2001)
    p3= MyTread(2000,3001)
    p3.start()
    p2.start()
    p1.start()
