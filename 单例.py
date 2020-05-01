class Singole:
    instance = None  #创建类属性，定义为None
    @classmethod
    def __new__(cls,*arges,**kwargs):
        if cls.instance is None:  #判断是否创建过类
            cls.instance = super().__new__(cls)  #创建内存空间
        else:
            print('已创建,不允许重复创建')
        return cls.instance  #返回内存空间

if __name__== '__main__':
    s1= Singole()
    print(s1)

    s2= Singole()
    print(s2)
