import threading
from threading import Thread
from time import sleep
import json

fil = "C:/Fernando/open_model_zoo_jsons/teste.json"
arr = [["a", 1], ["b", 2]]

with open(fil, "w") as f:
    json.dump(arr, f)
f.close()
quit()


class ThreadWithReturnValue(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def teste1(p1):
    sleep(10 / p1)
    return 'Kobinha ' + str(p1)
    
def teste2(p1):
    sleep(5 / p1)
    print( 'Kobinha ' + str(p1) )
    
def thread_teste1():
    cnt = 1
    limite = 1000
    
    threads = []
    while cnt <= limite:
        print("Contador: " + str(cnt))
        print(threading.active_count())
        t = ThreadWithReturnValue(target=teste1, args=(cnt,))
        t.start()
        threads.append(t)
        cnt  =cnt+1
    
    for t in threads:
        var1 = t.join()
        print(var1)
        
def thread_teste2():
    cnt = 1
    limite = 1000
    
    while cnt <= limite:
        print("Contador: " + str(cnt))
        print(threading.active_count())
        t = ThreadWithReturnValue(target=teste2, args=(cnt,))
        t.start()
        cnt  =cnt+1
     
def transforma_matrizes():
    comando = "python face_recognition_demo_2.py -i c:\Fernando\open_model_zoo_videos\\teste2.mp4 -m_fd C:\Fernando\open_model_zoo\open_model_zoo\demos\\face_recognition_demo\python\intel\\face-detection-retail-0004\FP32\\face-detection-retail-0004.xml -m_lm C:\Fernando\open_model_zoo\open_model_zoo\demos\\face_recognition_demo\python\intel\landmarks-regression-retail-0009\FP32\landmarks-regression-retail-0009.xml -m_reid C:\Fernando\open_model_zoo\open_model_zoo\demos\\face_recognition_demo\python\intel\\face-reidentification-retail-0095\FP32\\face-reidentification-retail-0095.xml --verbose -fg C:\Fernando\open_model_zoo_fotos_original2 -d_fd GPU -d_lm GPU -d_reid GPU"
    print(comando)
        
#thread_teste2()        
transforma_matrizes()