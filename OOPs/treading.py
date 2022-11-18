from threading import *
from time import sleep


class hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)

class GM(Thread):
    def run(self):
        for i in range(5):
            print('Good Morning')
            sleep(1)



t1=hello()
t2=GM()

print(t1.start())
sleep(0.2)
print(t2.start())
t1.join()
t2.join()

print('Bye')