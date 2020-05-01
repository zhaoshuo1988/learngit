class Base:
    def __init__(self,basename):
        self.basename = '基类'
        self.__name=basename

    def base_func(self):
        print("基类，父类函数")


class Sub(Base):
    def __init__(self,baseneme,su):
        super().__init__(basename)    #调用父类方法 初始化父类参数。除此方法外不能调用父类私有属性
        self.subname='派生类'
        self.basename='子类属性，覆盖父类属性'

    def sub_func(self):
        super().base_func()  #调用父类方法,PYthon 没有方法重载，不会发生父类重名 
        print('派生类，子类')

    def base_func(self):
        print("方法重写，重新定义base_func函数")

class Ssub(Sub):
    pass


if __name__="__main__":
    b=Base()
    print(b.basename)
    b.base_func()


    s=Sub()
    print(s.basename)
    s.base_func()
    super(Sub,s).base_func()   #类外调用父类方法
