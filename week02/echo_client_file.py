
import socket
from pathlib import *

HOST = 'localhost'
PORT = 10000

def file_client():
    '''File Server 的Client端'''
    #创建一个IPv4,TCP的套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 通过connect方法连接到指定的服务器和端口
    s.connect((HOST,PORT))

    while True:
        p = Path(__file__)
        pyfile_path = p.resolve().parent
        file_path = pyfile_path.joinpath('send_file')
        if not file_path.is_dir():
            Path.mkdir(file_path)
        file_name = file_path.joinpath('a.txt')
        # 发送数据到服务端
        if file_name.is_file() and file_name.exists():
            with open(file_name, 'rb') as f:
                data1 = f.read()
                s.sendall(data1)
                print("文件已传")
                break
        else:
            print("文件不存在")
            break
    s.close()

if __name__ == '__main__':
    file_client()