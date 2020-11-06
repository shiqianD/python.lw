# new day,new diff
# written in: 2020/10/31 22:36
class listinfo:
    def __init__(self,list):
        self.list = list
    def add(self,ad):
        self.list.append(ad)
        return self.list
    def get(self,key):
        return self.list[key]
    def update(self,list1):
        self.list.extend(list1)
        return self.list
    def pop(self):
        self.list.pop(-1)
        return self.list

list_info = listinfo([44,222,111,333,454,'sss','333'])
l=list_info.add(3)
l1=list_info.get(3)
l2=list_info.update([303,404])
l3=list_info.pop()
print(l)
print(l1)
print(l2)
print(l3)
