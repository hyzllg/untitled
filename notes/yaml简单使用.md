## 一、yaml文件介绍

YAML是一种简洁的非标记语言。其以数据为中心，使用空白，缩进，分行组织数据，从而使得表示更加简洁。

1. ### yaml文件规则

   - 基本规则：
     - 大小写敏感
     - 使用缩进表示层级关系
     - 缩进时不允许使用Tab键，只允许使用空格
     - 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
     - 使用#表示注释
     - 字符串可以不用引号标注

2. ### yaml文件数据结构

   - 对象：键值对的集合（简称 "映射或字典"）
   - 键值对用冒号 “:” 结构表示，冒号与值之间需用空格分隔
   - 数组：一组按序排列的值（简称 "序列或列表"）
   - 数组前加有 “-” 符号，符号与值之间需用空格分隔
   - 纯量(scalars)：单个的、不可再分的值（如：字符串、bool值、整数、浮点数、时间、日期、null等）
   - None值可用null可 ~ 表示

## 二、安装yaml

pip命令： pip install PyYaml

引入：import yaml

用python读取yaml文件如下:

代码：

```python
import yaml
from Common.dir_config import *
```

打开yaml文件

```python
fs = open(os.path.join(caps_dir, "data.yaml"),encoding="UTF-8")
datas = yaml.load(fs,Loader=yaml.FullLoader)  #添加后就不警告了
print(datas)
```

## 三、python中读取yaml配置文件

1. ### 前提条件:

   python中读取yaml文件前需要安装pyyaml和导入yaml模块：

   ```python
   使用yaml需要安装的模块为pyyaml（pip3 install pyyaml）;
   导入的模块为yaml（import yaml）
   ```

2. ### 读取yaml文件数据

   python通过open方式读取文件数据，再通过load函数将数据转化为列表或字典；

   ```python
   import yaml
   import os
   
   def get_yaml_data(yaml_file):
       # 打开yaml文件
       print("***获取yaml文件数据***")
       file = open(yaml_file, 'r', encoding="utf-8")
       file_data = file.read()
       file.close()
   
       print(file_data)
       print("类型：", type(file_data))
   
       # 将字符串转化为字典或列表
       print("***转化yaml数据为字典或列表***")
       data = yaml.load(file_data)
       print(data)
       print("类型：", type(data))
       return data
   current_path = os.path.abspath(".")
   yaml_path = os.path.join(current_path, "config.yaml")
   get_yaml_data(yaml_path)
   ```

3. ### yaml文件数据为键值对

   - yaml文件中内容为键值对：

     yaml键值对：即python中字典
     usr: my
     psw: 123455
     s: " abc\n"

     python解析yaml文件后获取的数据：

     {'usr': 'my', 'psw': 123455, 's': ' abc\n'}

   - yaml文件中内容为“键值对'嵌套"键值对"

     yaml键值对嵌套：即python中字典嵌套字典
     usr1:
       name: a
       psw: 123
     usr2:
       name: b
       psw: 456

     python解析yaml文件后获取的数据：

     {'usr1': {'name': 'a', 'psw': 123}, 'usr2': {'name': 'b', 'psw': 456}}

   - yaml文件中“键值对”中嵌套“数组”

     yaml键值对中嵌套数组
     usr3:

     ​	-a

     ​	-b

     ​	-c
     usr4:

     ​	-b

     python解析yaml文件后获取的数据：

     {'usr3': ['a', 'b', 'c'], 'usr4': ['b']}

4. ### yaml文件数据为数组

   1. yaml文件中内容为数组

      yaml数组

      -a

      -b

      -5

      python解析yaml文件后获取的数据：

      ['a', 'b', 5]

   2. yaml文件“数组”中嵌套“键值对”

      yaml"数组"中嵌套"键值对"

      -usr1: aaa

      -psw1: 111
       usr2: bbb
       psw2: 222

      python解析yaml文件后获取的数据：

      [{'usr1': 'aaa'}, {'psw1': 111, 'usr2': 'bbb', 'psw2': 222}]

5. ### yaml文件中基本数据类型

