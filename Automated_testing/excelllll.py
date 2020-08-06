import xlrd
import xlwt
import os
from xlutils.copy import copy
from practice import generate_ID

wb = xlrd.open_workbook(os.path.join(os.path.expanduser("~"), 'Desktop')+"\交行还款场景.xlsx")
#输出表名字其中一直方法
wb.sheet_names()
#选择第一个表有多种方法可以根据id或者name
shell1=wb.sheet_by_index(0)
shell2=wb.sheet_by_index(1)
#输出表格名字
name1 = shell1.name
name2 = shell2.name
print(f"表格名字：{name1}")
print(f"表格名字：{name2}")
#输出当前表格行数
nrows1 = shell1.nrows
nrows2 = shell2.nrows
print(f"表格行数：{nrows1}")
print(f"表格行数：{nrows2}")
#输出当前表格列数
ncols1 = shell1.ncols
ncols2 = shell2.ncols
print(f"表格列数：{ncols1}")
print(f"表格列数：{ncols2}")




#print修改文件copy一份
#不可以直接在原来的表进行修改只能copy修改保存
# 打开想要更改的wb文件
a = os.path.join(os.path.expanduser("~"), 'Desktop')+"\交行还款场景.xlsx"
# 将操作文件对象拷贝，变成可写的workbook对象
old_wb = xlrd.open_workbook(a)
new_wb=copy(old_wb)
# 获得第一个sheet的对象
wb=new_wb.get_sheet(0)
for i in range(1,nrows1):
    # 写入
    wb.write(i, 2, generate_ID(gender=1) + "、" + generate_ID(gender=1))
wb=new_wb.get_sheet(1)
for i in range(1,nrows2):
    # 写入
    wb.write(i, 2, generate_ID(gender=1) + "、" + generate_ID(gender=1))

new_wb.save(os.path.join(os.path.expanduser("~"), 'Desktop')+"\交行还款.xls")#保存