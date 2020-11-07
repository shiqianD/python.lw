# new day,new diff
# written in: 2020/10/31 16:28
class person:
    def __init__(self,name):
        self.name=name
    def close(self,alarm):
        alarm.closed(self,self.name)
    def sleep(self):
        print('{}睡着了'.format(self.name))
    def waked(self):
        print('闹钟吵醒了{}'.format(self.name))
class alarm:
    def ring(self):
        print('闹钟响了')
    def wake(self,person):
        person.waked()
    def closed(self,name):
        print('闹钟被{}关了'.format(name))

p = person('张三')
a = alarm()
a.ring()
a.wake(p)
p.close(alarm)
p.sleep()