import socket
import time
import common

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((common.TCP_IP, common.TCP_PORT))
    common.send(s, 50)
    time.sleep(0.1)
    common.receive(s)
    common.send(s, 20)
    time.sleep(0.1)
    common.send(s, 30)
    time.sleep(0.1)
    common.receive(s)
    common.receive(s)
    s.close()
