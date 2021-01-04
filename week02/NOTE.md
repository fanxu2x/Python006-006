学习笔记



1. s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

   ###### #AF_INET IPv4地址	 SOCK_STREAM	TCP协议

2. 0文件描述符-标准输入

   1					 标准输出

   2					 错误输出

   继续加载文件就是依次往后排fd = 3，4，5，6，7

3. 常见的异常类型主要有：

   a. LookupError下的indexError和KeyError

   b. IOError

   c. NameError

   d. TypeError

   e. AttributeError

   f. ZeroDivisionError

4. pip install pretty_errors美化异常输出

5. 魔术方法

6. Fn+F12 网页快速调试方式

7. Socket API

   socket()

   bind()

   listen()

   accept()

   recv()

   send()

   close()

8. 建立socket套接字 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   s.sendall(data.encode()), s.sendall()要求发送的数据是binary

   data = s.recv(1024)

   print(data.decode('utf-8')), 接收的数据也是binary类型，解码

9. with open(filename,'w') as f:

   ‘w’    会创建filename（a.txt）

   with open(filename,'rb') as f:

   'rb'   不会创建filename