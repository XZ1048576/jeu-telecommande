import socket
import sl4a
droid=sl4a.Android()
a=socket.socket(2,2)
a.bind(("",20183))
continuer=1
while continuer:
    msg,addr=a.recvfrom(1024)
    if msg[:17]==b"TELECOMMANDE SL4A":
        continuer=0
cnx=socket.socket()
cnx.connect((addr[0],int(msg.split(b" ")[2])))
while 1:
    msg=cnx.recv(1024)
    if msg=b"\x82":
        break
    choix=msg.split(b"\x81")
    titre=choix.pop(0)
    droid.dialogCreateAlert(titre.decode())
    droid.dialogSetItems([x.decode() for x in choix])
    droid.dialogShow()
    result=droid.dialogGetResponse().result
    if "item" in result:
        cnx.send(bytes([result["item"]]))
    else:
        cnx.send(b"canceled")