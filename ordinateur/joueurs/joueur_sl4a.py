import socket
from threading import Thread
import time
class _Broadcast(Thread):
    def __init__(self,msg):
        self.msg=msg
        self._cont=1
        Thread.__init__(self)
    def run(self):
        self._cont=1
        while self._cont:
            socket.socket(2,2).sendto(msg,("192.168.1.255",20183))
            time.sleep(5)
    def stop(self):
        self._cont=0
class joueur:
    def __init__(self,port):
        a=_Broadcast(b"TELECOMMANDE SL4A "+str(port).encode())
        a.start()
        cnx_p=socket.socket()
        cnx_p.bind("",port)
        cnx_p.listen(1)
        self.cnx,infos_cnx=cnx_p.accept()
        a.stop()
    def ask(self,titre,choix):
        self.cnx.send(b"\x81".join([titre.encode()]+[x.encode() for x in choix])
        return self.cnx.recv(1024)[0]
