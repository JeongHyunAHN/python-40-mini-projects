from threading import Thread
import time

# def task():
#     while True:
#         print("Thread 1 ongoing")
#         time.sleep(1.0) 
        
# new_thread = Thread(target=task)
# new_thread.daemon = True
# new_thread.start()

# while True:
#     print("Main function")
#     time.sleep(2.0)

def sum(name, value):
    for i in range(0,value):
        print(f"{name} : {i}")
        
t1 = Thread(target=sum,args=('Thread n°1',10))
t2 = Thread(target=sum,args=('Thread n°2',10))

t1.start()
t2.start()

print("Main thread")

# practical case presented : https://www.pythontutorial.net/python-concurrency/python-threading/

