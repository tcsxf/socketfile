import socket
import os


def send_file():
    file = input('which file: ')
    if not os.path.exists(file):
        print('file not exists')
        return

    filename = os.path.basename(file)
    s.send(filename.encode('utf-8'))
    with open(file, 'rb') as f:
        while 1:
            byte = f.read(1024)
            if byte:
                s.send(byte)
            else:
                break
    print('send file success')


def receive_file():
    filename = s.recv(1024).decode('utf-8')
    if not filename:
        print('recevie file failed')
        return
    with open(filename, 'wb') as f:
        while 1:
            byte = s.recv(1024)
            if byte:
                f.write(byte)
            else:
                break
    print('receive file success')


serverip = input('please input server ip: ')
port = input('whick port')
tp = input('send or receive: ')
s = socket.socket()
s.connect((serverip, port))
s.send(tp.encode('utf-8'))
if tp in ('s', 'send'):
    send_file()
elif tp in ('r', 'receive'):
    receive_file()
s.close()
