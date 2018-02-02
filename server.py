import socket
import os


def receive_file():
    filename = sock.recv(1024).decode('utf-8')
    if not filename:
        print('receive file failed')
        return
    with open(filename, 'wb') as f:
        while 1:
            byte = sock.recv(1024)
            if byte:
                f.write(byte)
            else:
                break
    print('receive file success')


def send_file():
    file = input('which file: ')
    if not os.path.exists(file):
        print('file not exists')
        return

    filename = os.path.basename(file)
    sock.send(filename.encode('utf-8'))
    with open(file, 'rb') as f:
        while 1:
            byte = f.read(1024)
            if byte:
                sock.send(byte)
            else:
                break
    print('send file success')


os.chdir(r'C:\Users\Administrator\Desktop')
s = socket.socket()
s.bind(('', 3155))
s.listen(1)
print('server ip is {0}'.format(socket.gethostbyname(socket.gethostname())))

while 1:
    sock, addr = s.accept()
    print('connected by {0}:{1}'.format(addr[0], addr[1]))

    tp = sock.recv(1024).decode('utf-8')
    if tp in ('s', 'send'):
        receive_file()
    elif tp in ('r', 'receive'):
        send_file()
    sock.close()
    if input('quit?(y or n): ') in ('y', 'yes'):
        break

s.close()
