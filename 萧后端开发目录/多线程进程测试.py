import time
import os
from multiprocessing import Process
from multiprocessing import Pool, cpu_count
import threading
#######################################################
# 单进程运算
# import time
# def long_time_task():
#     print('当前进程: {}'.format(os.getpid()))
#     time.sleep(2)
#     print("进程：{} 运行结果: {}".format(os.getpid(), 8 ** 20))
#
#
# if __name__ == "__main__":
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     for i in range(2):
#         long_time_task()
#
#     end = time.time()
#     print("用时{}秒".format((end-start)))

#######################################################
# 多进程运行结果  6核cpu
# import time
# import os
# from multiprocessing import Process
# def long_time_task(i):
#     print('子进程: {} - 任务{} 开始'.format(os.getpid(), i))
#     time.sleep(2)
#     print("子进程：{} 任务{} 的运行结果: {}".format(os.getpid(), i, 8 ** 20))
#
#
# if __name__=='__main__':
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     p1 = Process(target=long_time_task, args=(1,))
#     p2 = Process(target=long_time_task, args=(2,))
#     p3 = Process(target=long_time_task, args=(3,))
#     p4 = Process(target=long_time_task, args=(4,))
#     p5 = Process(target=long_time_task, args=(5,))
#     p6 = Process(target=long_time_task, args=(6,))
#     print('等待所有子进程完成。')
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
#     p6.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     p6.join()
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))

#######################################################
# 使用Pool类创建多进程。
# import time
# import os
# from multiprocessing import Pool, cpu_count

# def long_time_task(i):
#     print('子进程: {} - 任务{} 开始'.format(os.getpid(), i))
#     time.sleep(2)
#     print("子进程：{} 任务{} 的运行结果: {}".format(os.getpid(), i, 8 ** 20))
#
#
# if __name__=='__main__':
#     print("CPU内核数:{}".format(cpu_count()))
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     p = Pool(6)
#     for i in range(7):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有子进程完成。')
#     p.close()
#     p.join()
#     end = time.time()
#     print('当前最后处理进程: {}'.format(os.getpid()))
#     print("总共用时{}秒".format((end - start)))

#######################################################
# 多进程间的数据共享与通信 queue
# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process {} to write'.format(os.getpid()))
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process {} to read'.format(os.getpid()))
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
#######################################################
# 多线程编程
# import time
# import os
# import threading

# def long_time_task(i):
#     print('当前子进程: {} - 任务{} 开始'.format(os.getpid(), i))
#     print('当前子线程: {} 任务{}'.format(threading.current_thread().name, i))
#     time.sleep(2)
#     print("当前子进程: {} 子线程{} 任务{} 运算结果: {}".format(os.getpid(), threading.current_thread().name, i, 8 ** 20))
#     print(time.time(), i)
#
# if __name__=='__main__':
#     start = time.time()
#     print('当前母进程: {}'.format(os.getpid()))
#     print('这是主线程：{}'.format(threading.current_thread().name))
#     thread_list = []
#     for i in range(1, 3):
#         t = threading.Thread(target=long_time_task, args=(i, ))
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.start()
#
#     for t in thread_list:
#         t.join()
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))


################################################################
# 继承thread类重写run方法来创建线程
# import time
# import threading

# def long_time_task(i):
#     time.sleep(2)
#     return 8**20
#
#
# class MyThread(threading.Thread):
#     def __init__(self, func, args, name='', ):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.args = args
#         self.name = name
#         self.result = None
#
#     def run(self):
#         print('开始子线程{}，{},传入参数是{}'.format(self.name, threading.current_thread().name,self.args[0]))
#         self.result = self.func(self.args[0])
#         print("子线程{}运行结果: {}".format(self.name, self.result))
#         print('结束子线程{}'.format(self.name))
#
#
# if __name__ == '__main__':
#     start = time.time()
#     threads = []
#     for i in range(1, 3):
#         t = MyThread(long_time_task, (i,), str(i))
#         threads.append(t)
#
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))
############################################################
# 线程的数据安全 数据共享
# 利用线程锁
# import threading

# class Account:
#     def __init__(self):
#         self.balance = 0
#
#     def add(self, lock):
#         # 获得锁
#         lock.acquire()
#         for i in range(0, 100000):
#             self.balance += 1
#         # 释放锁
#         lock.release()
#
#     def delete(self, lock):
#         # 获得锁
#         lock.acquire()
#         for i in range(0, 100000):
#             self.balance -= 1
#             # 释放锁
#         lock.release()
#
#
# if __name__ == "__main__":
#     account = Account()
#     lock = threading.Lock()
# # 创建线程
#     thread_add = threading.Thread(target=account.add, args=(lock,), name='Add')
#     thread_delete = threading.Thread(target=account.delete, args=(lock,), name='Delete')
# # 启动线程
#     thread_add.start()
#     thread_delete.start()
# # 等待线程结束
#     thread_add.join()
#     thread_delete.join()
#
#     print('The final balance is: {}'.format(account.balance))

#########################################################################
# 使用queue队列通信
from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            print("{} is producing {} to the queue!".format(self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            val = self.queue.get()
            print("{} is consuming {} in the queue.".format(self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())


def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')


if __name__ == '__main__':
    main()
