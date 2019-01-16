
# Echo client program
import socket

HOST = '127.0.0.100'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
conn = None
addr = None


def connect(send_it=False):
    """
    used to connect
    :return: only when we connect successfully will stop this function and return True
    """
    global s, conn, addr
    # while True:
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            if send_it is True:
                s.connect(sa)
            else:
                s.bind(sa)
                s.listen(1)
        except OSError as msg:
            s.close()
            s = None
            continue
        break

    if s is not None:
        return True

        # if s is None:
        #     print('could not open socket')
        #     sys.exit(1)


def receive():
    """
    used to get the message from the robot
    :return data: return the message that we get from the robot
    """
    while True:
        t = connect()
        if t:
            break

    global s, conn, addr
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            return data.decode('utf-8')


def send(message):
    """
    used to send message back to the robot
    :param message: string, specific sentence of particular scenario
    :return:
    """
    while True:
        t = connect(True)
        if t:
            break

    global s
    s.sendall(message.encode('utf-8'))  # here we must send byte type


def send_and_receive():
    while True:
        while True:
            t = connect(True)
            if t:
                break
        global s, conn, addr
        message = input('请输入：')
        s.sendall(message.encode('utf-8'))  # here we must send byte type

        while True:
            t = connect()
            if t:
                break
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                print('接受到：' + data.decode('utf-8'))
