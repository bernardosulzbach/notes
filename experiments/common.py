TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024


def send(communication_object, n):
    communication_object.send(bytes([0] * n))
    print("Sent {} byte{}.".format(n, "" if n == 1 else "s"))


def receive(communication_object):
    data = communication_object.recv(BUFFER_SIZE)
    if not data:
        return
    print("Received {} byte{}.".format(len(data), "" if len(data) == 1 else "s"))
