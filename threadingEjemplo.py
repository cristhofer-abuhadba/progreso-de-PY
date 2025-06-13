
    
import threading 

def contar():
    contador=0
    while contador<100:
       contador+=1
       print('hilo:',
       threading.current_thread().getName(),
              '\ncon identificador:',
            threading.current_thread().ident,
            '\nContador:',contador)

hilo1 = threading.Thread(target=contar)
hilo2 = threading.Thread(target=contar)

hilo1.start()
hilo2.start()


