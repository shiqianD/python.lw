# new day,new diff
# written in: 2020/10/31 10:50
class dictclass(object):
    def __init__(self,dict):
        self.dict=dict
    def get_dict(self,key):
        if key in self.dict :
            return self.dict[key]
        else:
            return 'not found'
    def del_dict(self,key):
        if key in self.dict:
            self.dict.pop(key)
        else:
            return'no that key'
    def get_key(self):
        return self.dict.keys()
    def updata_dict(self,dict2):
        self.dict = dict(self.dict,**dict2)
        return self.dict.values()
a=dictclass({'a':1,'b':2})
print (a.get_dict('c'))
print (a.get_dict('a'))

print (a.del_dict('c'))
print (a.get_key())
print(a.updata_dict({'c':3,'d':4}))


