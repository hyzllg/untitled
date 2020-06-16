'''
1. str常用方法
   + 判断字符串中的字符是否全为数字  s.isdigit()
   + 判断字符串是否全为英文字母 s.isalpha()
   + 判断字符串所有字符是否全为小写英文字母  s.islower()
   + 判断字符串所有字符是否全为大写英文字母  s.isupper()
   + 判断字符串是否只由空格组成 s.isspace()
   + 判断字符串是否全为数字字符 s.isnumeric()
   + 将原字符串居中，左右默认填充空格 s.center()
   + 获取一个字符串中子串的个数 s.count()
   + 获取字符串中子串sub的索引,失败返回-1 s.find()
   + 生成每个英文单词的首字母大写字符串 s.title()
   + 生成将英文转换为大写的字符串 s.upper()
   + 生成将英文转换为小写的字符串 s.lower()
   + 查找 找不到抛异常 index()
   + 将原字符串的old用new代替，生成一个新的字符串 replace()
   + 去除两边空格及指定字符串 s.strip()
   + 裁剪分割 s.split()
   + 连接字符，按某字符串为分隔符 join()
   + 返回S是否是以***开头，如果以***头返回True,否则返回False s.startswith()
   + 返回S是否是以***结尾，如果***结尾返回True,否则返回False s.endswith()
   + 转码，解码 enocde(),decode()
2. list
   + 末尾追加 list.append()
   + 指定位置插入 list.insert()
   + 逐个追加，列表合并 list.extend()
   + 排序 list.sort(),sorted()
   + 删除第一个匹配项, 成功无返回，找不到报异常 list.remove()
   + 出栈 返回出栈元素 list.pop()
   + 清除列表，无返回值 list.clear()
   + 返回对应元素的索引下标, begin为开始索引，end为结束索引, list.index()
      当 value 不存在时触发ValueError错误
   + 返回列表中元素的个数 list.count()
   + 复制此列表（只复制一层，不会复制深层对象) list.copy()
   + 指定位置删除 del list[index]
   + 反转 list.reverse()
   + 将列表返回 下标 和 内容 for a,b in enumerate(list):
3. dict
   + 存在则更改，不存在则新增 dict[key] = value
   + 字典不支持 { }+{ } dict.update() 可增可改可拼接
   + dict.fromkeys{[1,2,3][]}
   + 不存在，同查，抛异常 del dict[]
   + 取出 + 删除；不存在：None 或 [默认值] dict.pop()
   + 末尾删除 LIFO dict.popitem()
   + 返回字典D的副本,只复制一层(浅拷贝) dict.copy()
   + 返回键key所对应的值,如果没有此键，则返回 dict.get()
   + 清空 dict.clear()
   + 取出所有的key-value  列表(元组) for index,value in dict.items()
   + 取出所有value 列表 dict.values()
4. set
   + 在集合中添加一个新的元素e；如果元素已经存在，则不添加  set.add()
   + 从集合中删除一个元素，如果元素不存在于集合中，则会产生一个KeyError错误
   + 从集合S中移除一个元素e,在元素e不存在时什么都不做
   + 清空集合内的所有元素
   + 将集合进行一次浅拷贝
   + 从集合S中删除一个随机元素;如果此集合为空，则引发KeyError异常
   + 等同于 S l= s2, 用 S与s2得到的全集更新变量S
   + S - s2 补集运算，返回存在于在S中，但不在s2中的所有元素的集合
   + 等同于 S -= s2
   + 等同于 S & s2
   + 等同于S &= s2
   + 如果S与s2交集为空返回True,非空则返回False
   + 如果S与s2交集为非空返回True,空则返回False
   + 如果S为s2的超集返回True,否则返回False
   + 返回对称补集, 等同于 S ^ s2
   + 等同于 S ^= s2, 用 S 与 s2 的对称补集更新 S
   + 生成 S 与 s2的全集, 等同于 S \






'''
import requests
import re
def name_idno():
    url = 'http://www.xiaogongju.org/index.php/index/id.html/id/513436/year/1990/month/06/day/14/sex/%E7%94%B7'

    headers = {
        "Content-Type":"text/html;charset=utf-8",
        "Host":"www.xiaogongju.org",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    request = requests.get(url,headers=headers)
    ret = request.text
    ret = re.findall('\s<td>\w*</td>',ret)
    new_ret = []
    for i in ret:
        i = i.replace(' ','')
        i = i.replace('<td>','')
        i = i.replace('</td>','')
        new_ret.append(i)
    print(new_ret)
    return new_ret

a = name_idno()
print(a[0])
print(a[1])



























