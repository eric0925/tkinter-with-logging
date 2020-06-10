# coding=utf-8
import tkinter as tk
import logging
import time

class log():

    def __init__(self):
        self.log_name="eric_test"
        self.level = "DEBUG"
        
        #print("type(self.logger),type(self.handler):",type(self.logger),type(self.handler))
    def make_log (self):
        print("--------------make log--------------")
        var = e.get()
        global logger 
        logger = logging.getLogger(self.log_name)
        handler = logging.FileHandler('log_file/'+'%s_%s'%(var,time.strftime('%M%S\n', time.localtime(time.time()))),'w','utf-8',delay=0)

        logger.setLevel(self.level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

        handler.setFormatter(formatter)      

        logger.addHandler(handler)

        print(logger.handlers[:])
        print("len(logger.handlers[:]):",len(logger.handlers[:]))
        print("now time:",time.strftime('%m%d-%H%M%S\n', time.localtime(time.time())))
        for x in range(10):
            logger.debug("hello")
            #time.sleep(0.1)
        
    def close_log(self):
        if len(logger.handlers[:]) <1:
            print("warning! No log to close.")
        else:
            print("----------close log------------------")
            #getattr(make_log(self), 'self.logger')  
            #print(type(logging.FileHandler(handler)))    #global method : type(handler):<class 'logging.FileHandler'>
            print(type(logger))     #global method : type(handler):<class 'logging.Logger'>
            print("self.handler:",logger.handlers[-1])
            #print("handler:",handler)
            logger.handlers[-1].close()
            print("all handlers:",logger.handlers[:])
            logger.removeHandler(logger.handlers[-1])
            print("len(logger.handlers[:]):",len(logger.handlers[:]))


window = tk.Tk()
window.title('my window')

window.geometry('400x200')

e = tk.Entry(window,width=15)#,show='*')
e.pack()

b1 = tk.Button(window,text="make log",width=15,height=6,command=log().make_log)
b1.pack()#side = tk.LEFT)

b1 = tk.Button(window,text="delete log",width=15,height=6,command=log().close_log)
b1.pack()#side = tk.LEFT)

#b2 = tk.Button(window,text="START",command=insert_end)
#b2.pack()#side = tk.LEFT)



window.mainloop()