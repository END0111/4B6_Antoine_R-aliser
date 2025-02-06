import threading
import time
def my_callback():
    print("Finished")
def start_timer(second,callback):
    def timer_thead():
        print("Timer started")
        for timer in range(1, second + 1):
            print(f"{timer} Mississippi")
            time.sleep(1)  
        callback()
    threaad = threading.Thread(target=timer_thead)
    threaad.start()
start_timer(5,my_callback)

                                                                                                                     