from threading import *
import time

# def dsp():
#     for i in range(1,10):
#         print("child thread")
# t=Thread(target=dsp)
# t.start()
# for i in range(1,10):
#     print("Main Thread")
# def dsp1():
#     start_time=time.perf_counter()
#     for i in range(1,10):
#         print(2**i)
#     end_time=time.perf_counter()
#     print(f"execution time for 2 power :{end_time-start_time:.4f}seconds")    
# t=Thread(target=dsp1) 
# t.start()       
# def dsp2():
#     start_time=time.perf_counter()
#     for i in range(1,10):
#         print(5**i)
#     end_time=time.perf_counter()
#     print(f"execution time for 5 power :{end_time-start_time:.4f}seconds")     
# t=Thread(target=dsp2)
# t.start()
l=Lock()
def wish(name):
    l.acquire()
    for i in range(5):
        print("Good Morning",end="")
        time.sleep(2)
        print(name)
    l.release()    
t1=Thread(target=wish,args=("kartikey",))
t2=Thread(target=wish,args=("drakster",))
t1.start()
t2.start()
