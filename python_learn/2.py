# new day,new diff
# written in: 2020/10/31 9:37
class student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def age(self):
        return self.age
    def score(self):
        return max(self.score)
p1=student('张三',18,[99,66,33])
print (p1.get_name())
