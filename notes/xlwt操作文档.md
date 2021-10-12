## 1、安装xlwt

​	pip install xlwt

## 2、设置字体

```python
import xlwt

# 创建一个工作簿
xl = xlwt.Workbook(encoding='utf-8')
# 创建一个sheet对象,第二个参数是指单元格是否允许重设置，默认为False
sheet = xl.add_sheet('菜鸟的成长历程', cell_overwrite_ok=False)
# 初始化样式
style = xlwt.XFStyle()
# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
# 黑体
font.bold = True
# 下划线
font.underline = False
# 斜体字
font.italic = True
# 设定样式
style.font = font
# 第一个参数代表行，第二个参数是列，第三个参数是内容，第四个参数是格式
sheet.write(0, 0, '不带样式的携入')
sheet.write(1, 0, '带样式的写入', style)

# 保存文件
xl.save('C:\\Users\\15136\\Desktop\\字体.xls')
```

## 3、设置单元格宽度

```python
import xlwt
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('单元格宽度', cell_overwrite_ok=True)
sheet.write(0, 0, '第一个行第一列内容')
sheet.col(0).width = 5000
xl.save('C:\\Users\\15136\\Desktop\\单元格宽度.xls')
```

## 4、将一个日期输入一个单元格

```python
import xlwt
import datetime
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('日期', cell_overwrite_ok=True)
# 初始化样式
style = xlwt.XFStyle()
#  Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
style.num_format_str = 'M/D/YY'
sheet.write(0, 0, datetime.date.today(), style)
sheet.col(0).width = 5000
xl.save('C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls')
```

## 5、添加一个公式

```python
import xlwt
xl = xlwt.Workbook(encoding='UTF-8')
sheet = xl.add_sheet('公式', cell_overwrite_ok=True)
# 第一行第一列
sheet.write(0, 0, 5)
# 第一行第二列
sheet.write(0, 1, 3)
sheet.write(0,2,xlwt.Formula('A1 * B1'))
sheet.write(1,0,xlwt.Formula("A1 + B1"))
xl.save("C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls")
```

## 6、在单元格中添加超链接

```python
import xlwt

xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('超链接')
sheet.write(0, 0, xlwt.Formula('HYPERLINK("https://www.baidu.com";"百度")'))
xl.save("C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls")
```

## 7、合并列和行

```python
import xlwt
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('合并列和行')
# (行，行，列，列，内容)
sheet.write_merge(0, 1, 0, 3, '合并从第一行到第二行，第一列到第四列')
font = xlwt.Font()  # 创建字体示例
font.bold = True  # bold设置为黑体字
style = xlwt.XFStyle()  # 初始化样式
style.font = font
sheet.write_merge(2, 3, 0, 3, '合并从第三行到第四行，第一列到第四列', style)
xl.save('C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls')
```

## 8、单元格的对齐方式

```python
import xlwt
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('单元格的对齐方式')
# 创建对齐格式对象
alignment = xlwt.Alignment()
# 左右的对其，水平居中 May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER,
# HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,
# HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_CENTER
# 上下对齐 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()  # 创建一个样式对象
style.alignment = alignment  # 将格式Alignment对象加入到样式对象
sheet.write(0,0,'单元居中',style)
xl.save('C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls')
```

## 9、为单元格加边框

```python
import xlwt
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('单元格添加边框')
# 创建边框对象
borders = xlwt.Borders()
borders.left = xlwt.Borders.DASHED  # 对边框对象进行操作，指定边框上下左右的边框类型为虚线
# DASHED虚线
# NO_LINE没有
# THIN实线
# May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
# MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40      #指定上下左右的边框颜色为0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
style = xlwt.XFStyle()  # Create Style   #创建样式对象
style.borders = borders  # 将设置好的边框对象borders 加到样式对象style中。
sheet.write(0, 0, '单元格内容', style)
sheet.write(1, 0, '单元格内容', style)
sheet.write(0, 1, '单元格内容', style)
sheet.write(1, 1, '单元格内容', style)
sheet.col(0).wigth = 4000
sheet.col(1).wigth = 4000
xl.save('C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls')
```

## 10、设置背景色

```python
import xlwt
xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('单元格背景色')
# 创建背景模式对像
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 #设置模式颜色 May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 =
# Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
style = xlwt.XFStyle() # 创建样式对象Create the Pattern
style.pattern = pattern # 将模式加入到样式对象Add Pattern to Style
sheet.write(0, 0, '单元格内容', style)#向单元格写入内容时使用样式对象style
xl.save('C:\\Users\\15136\\Desktop\\菜鸟的成长历程.xls')
```

