class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def __str__(self):
        return  'Vector({},{})'.format(self.x,self.y)
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

if __name__=='__main__':
    v1=Vector(10,20)
    print(v1)

    v2 = Vector(20,30)
    print(v2)
    print(v1+v2)
