
import socket
from pathlib import *

HOST = 'localhost'
PORT = 10000


def file_server():

    '''file Server 的Server端'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #对象s绑定到指定的主机和端口上
    s.bind((HOST,PORT))
    #只接受1个连接
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')       
        p = Path(__file__)
        pyfile_path = p.resolve().parent
        file_path = pyfile_path.joinpath('recv_file')
        if not file_path.is_dir():
            Path.mkdir(file_path)
        file_name = file_path.joinpath('b.txt')
        with open(file_name, 'wb+') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        conn.close()

if __name__ =='__main__':
    file_server()