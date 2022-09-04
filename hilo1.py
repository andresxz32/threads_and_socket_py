import threading
import time


#h= número de hilos
#n= cuanto se desea contar
#t= tiempo de espera

def contar (h,n,t):
    i = 0
    while i < n:
        time.sleep(t)
        print('Hilo',h,'Cuenta número:',i, '\n')
        i +=1

t1 = threading.Thread(target=contar,args=(1,4,0.9)) 
t2 = threading.Thread(target=contar,args=(2,6,1.3)) 
t3 = threading.Thread(target=contar,args=(3,6,1.3))

t1.start()
t2.start()
t3.start()