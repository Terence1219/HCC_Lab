#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time


host = '192.168.183.132'
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

#please fill UAV IP address
tello_address1 = ('192.168.183.230', 8889)#TD8
tello_address2 = ('192.168.183.39', 8889)#HCC02

message1=["command","battery?", "takeoff", "forward 170","up 10","left 70","forward 120", "land","end"]
message2=["command","battery?", "takeoff", "forward 170","down 20","left 70","forward 110", "land","end"]
delay=[3,3,10,5,5,5,5,2,2]

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print("{} : {}".format(server,data.decode(encoding="utf-8")))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


for i in range(0,len(message1)):
    msg1=message1[i]
    msg2=message2[i]
    sock.sendto(msg1.encode("utf-8"), tello_address1)
    sock.sendto(msg2.encode("utf-8"), tello_address2)
    time.sleep(delay[i])


