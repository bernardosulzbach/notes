import socket
import time
import common

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((common.TCP_IP, common.TCP_PORT))
    s.listen(1)
    connection, address = s.accept()
    common.receive(connection)
    common.send(connection, 10)
    time.sleep(0.1)
    common.receive(connection)
    common.receive(connection)
    common.send(connection, 90)
    time.sleep(0.1)
    common.send(connection, 50)
    time.sleep(0.1)
    s.close()
