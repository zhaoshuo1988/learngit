import threading
import time
class shop:
    def __init__(self,name):
        self.__name=name
class user:
    def __init__(self,name):
        self.__name = name
class 秒杀(threading.Thread):
    count =20
    def __init__(self,user):
        super().__init__()

    def run(self):
        while 秒杀.count>0:
            mutex.acquire()   #加锁
            if 秒杀.count>0:
                print('{}抢到了{}号商品'.format(self.name,秒杀.count))
            秒杀.count-=1
            time.sleep(0.01)
            mutex.release()   #解锁
        #else:
            #print('抢没了')
            

if __name__=='__main__':
    count=20
    mutex =threading.Lock()
    for i in range(15):
        p=秒杀(i)
        p.start()

        
