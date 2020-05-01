class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def eat(self):
        print("{}正在吃饭".format(self.name))

    def __func(self):
        print("私有方法")



if __name__='__main__':
    zhangs = person('zhang3',23)

    print(zhangs.name)
    zhangs.eat()
