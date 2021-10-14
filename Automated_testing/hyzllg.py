import xlwt

#创建一个工作簿
webook = xlwt.Workbook(encoding='utf-8')
#创建一个sheet对象
sheet = webook.add_sheet("我是菜鸟")
#首先初始化样式
style = xlwt.XFStyle()

#然后为样式设置字体
font = xlwt.Font()
font.name = 'Times New Roman'
# 黑体
font.bold = True

# 创建背景模式对像
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5

# 设定样式
style.font = font
style.pattern = pattern
#写入内容
sheet.write(0,0,"测试编号",style)
#设置单元格宽度和高度
sheet.col(0).width = 256*72
sheet.row(0).height_mismatch = True
sheet.row(0).height = 20*40
#保存文件
webook.save("我是菜鸟.xls")