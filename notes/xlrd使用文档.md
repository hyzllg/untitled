## 1、安装xlrd模块

​	pip install xlrd

## 2、导入xlrd模块

```python
import xlrd
```

## 3、打开Excel文件读取数据

```python
data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
```

## 4、常用的函数

​	excel中最重要的方法就是book和sheet的操作

1. ### 获取book中一个工作表

   ```python
   table = data.sheets()[0]          #通过索引顺序获取
   
   table = data.sheet_by_index(sheet_indx)#通过索引顺序获取
   
   table = data.sheet_by_name(sheet_name)#通过名称获取
   
   以上三个函数都会返回一个xlrd.sheet.Sheet()对象
   
   names = data.sheet_names()    #返回book中所有工作表的名字
   
   data.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕
   ```

2. ### 行的操作

   ```python
   nrows = table.nrows  #获取该sheet中的有效行数
   
   table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
   
   table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
   
   table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
   
   table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
   
   table.row_len(rowx) #返回该列的有效单元格长度
   ```

3. ### 列(colnum)的操作

   ```python
   ncols = table.ncols   #获取列表的有效列数
   
   table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
   
   table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
   
   table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
   
   table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表
   ```

4. ### 单元格的操作

   ```python
   table.cell(rowx,colx)   #返回单元格对象
   
   table.cell_type(rowx,colx)    #返回单元格中的数据类型
   
   table.cell_value(rowx,colx)   #返回单元格中的数据
   
   table.cell_xf_index(rowx, colx)   # 暂时还没有搞懂
   ```

5. python解决open()函数、xlrd.open_workbook()函数文件名包含中文，sheet名包含中文报错

   ```python
   #打开文件
   file = open(filename,'rb') 
   
   #打开excel文件
   workbook = xlrd.open_workbook(filename)
   
   #获取sheet
   sheet = workbook.sheet_by_name(sheetname)
   
   #解决
   filename = filename.decode('utf-8'
   ```

   

