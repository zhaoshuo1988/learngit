class HouseIterm:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return('{}占地面积{:.2f}'.format(self.name,self.area))
   
   
class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        
        self.free_area=area
        self.item_list=[]
    def __str__(self):
        return('户型：{}\n总面积:{:.2f}\n剩余面积{:.2f}\n家具:{}'
                .format(self.house_type,self.area,self.free_area,self.item_list))
    def add_item(self,item):
        if self.free_area< item.area:
            print("房间剩余面积{}，{}占用{}，放不下！！！"
                    .format(self.free_area,item.name,item.area))
            return

        self.item_list.append(item.name)
        self.free_area = self.free_area- item.area

if __name__ =='__main__':
    bed= HouseIterm('梦宝',4)
    chest = HouseIterm('衣柜',2)
    table = HouseIterm('餐桌',1.5)

    print(bed,chest,table)
    h= House('三室一厅',210)
    print(h)
