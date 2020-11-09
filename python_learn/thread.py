# new day,new diff
# written in: 2020/11/1 15:02
import threading
def fun1():
    for i in range(10):
        print(threading.current_thread().getName(),i)
        if i==5:
            thread2 = threading.Thread(target=fun2,name="线程二")
            thread2.start()
            thread2.join()
def fun2():
    for i in range(65,76):
        print(threading.current_thread().getName(),chr(i))
thread1 = threading.Thread(target = fun1,name = "线程一")
thread1.start()
