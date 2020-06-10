# coding=utf-8
import tkinter as tk
import logging
import time


class log():   

    def __init__(self):
        self.log_name="log_test"
        self.level = "DEBUG"
        self.logger = logging.getLogger("log_test")
    def make_log (self):
        print("------------------make log------------------")
        try:
            var = e.get()

            self.handler = logging.FileHandler('log_file/'+'%s'%(time.strftime('%M%S\n', time.localtime(time.time()))),'w','utf-8',delay=0)

            self.logger.setLevel("DEBUG")
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

            self.handler.setFormatter(formatter)      

            self.logger.addHandler(self.handler)

            print(self.logger.handlers[:])
            print("len(logger.handlers[:]):",len(self.logger.handlers[:]))
            print("now time:",time.strftime('%m%d-%H%M%S\n', time.localtime(time.time())))
            for x in range(10):
                self.logger.debug("hello")
        except Exception as e:
            print(str(e))
            
    def close_log(self):
        if len(self.logger.handlers[:]) <1:
            print("warning! No log to close.")
        else:
            print("------------------close log------------------")
            try:
                self.logger.handlers[-1].close()
                self.logger.removeHandler(self.logger.handlers[-1])
                print("all handlers:",self.logger.handlers[:])
                print("len(logger.handlers[:]):",len(self.logger.handlers[:]))
            except Exception as e:
                print(str(e))

if __name__ == "__main__":
    window = tk.Tk()
    window.title('my window')
    window.geometry('400x200')

    e = tk.Entry(window,width=15)
    e.pack()

    b1 = tk.Button(window,text="make log",width=15,height=6,command=log().make_log)
    b1.pack()

    b1 = tk.Button(window,text="close log",width=15,height=6,command=log().close_log)
    b1.pack()

    window.mainloop()
