1. 学习笔记

  1. Git
     $ git config --global http.proxy "XXX"

  2. windows check path
     where python
     where pip

  3. .pyc文件保存的python解释器py文件的目标代码pyc

     将源代码转换成目标代码直接运行

     python3 -m venv venv1

     venv是python3自带的一个模块

     python3 -m就是告诉python在执行的时候加载这个模块venv

     venv1是虚拟环境的目录名称，是自定义的，可以自定义目录或者文件名

  4. Linux

     /表示根目录。~表示home家目录

  5. Linux下venv

     python3 -m venv venv006		-----> 会新建一个vevn006的文件夹

     bin 	include	lib		pyvenv.cfg

     source venv006/bin/activate		------> 会进入虚拟环境

     （venv006）****$

     deactivate		-------->会退出虚拟环境

  6. 更新pip 安装源

     cd ~

     pws

     /User/username

     mkdir .pip

     cd .pip

     vim pip.conf

     [global]

     index-url = https://pypi.tuna.tsinghua.edu.cn/simple

  7. pip3 freeze     ------> 查看pip已经安装了哪些模块及其版本

     一般会保存到一个文件 pip3 freeze > requirements.txt

     不同虚拟环境之间，如果想把venv1的环境部署到venv2上，

     先pip3 freeze > requirements.txt		------>可以在venv1的同级目录下面run，只要是在虚拟环境里面

     新建虚拟环境venv2 	python3 -m venv venv2

     进入虚拟环境venv2     source /bin/activate

     (venv2)***$pip install -r ./requirements.txt     ------>在虚拟环境venv2下面安装venv1的模块

  8. 进制表示

     十进制100------->100

     二进制0b10----->2

     八进制0o10------>8

     十六进制0x10-----> 16

     浮点数转换整数int(5.8)------->5

     字符串转换成整数int("123")------->123

  9. python 中==比较两个对象的内容是否相等，is比较两个对象的id的值是否相等，比较是否是同一个对象，是否指向同一个内存地址

  10. python中单引号双引号三引号都会被认为是单引号

      ‘abc’	"abc"	'''abc'''------------>都会输出为'abc'

  11. 字符串有很多内置的方法，upper(),find(),isdigit()....

  12. 列表用[]表示，列表有内置方法，append(),copy()....

  13. 元组用()表示，不可变，不可加不可减，有内置方法。

  14. 这三个都是序列类。

  15. python之禅  import this

  16. 字典dict,用{}表示，dict1 = {'k1':'v1','k2':'v2'}

      dict1['k1'] = 'v1' 通过键查看值

  17. .py文件可以被看做是一个模块被导入，很多个py文件组成的文件夹被称为是包被导入

  18. 三种格式化输出

      a.占位符%

      print(''%d,%s" % (10,'abc'))	------> 10,abc

      b.format位置{0}{1}{2}

      "{0},{1}".format()

      print("{1},{0}".format(10,'abc')	----->abc,10

      c. python3.6之后的语法f""

      name = xiaohong

      print(f"{name}")

      
