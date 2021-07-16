a = input("--------")
all_list = []
code_xy = '217,285'
if '|' in code_xy:
    a = code_xy.split('|')
    for i in a:
        x = i.split(",")[0]
        y = i.split(",")[1]
        all_list.append([x,y])
else:
    x = code_xy.split(",")[0]
    y = code_xy.split(",")[1]
    all_list.append([x, y])



print(all_list)

