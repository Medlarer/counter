#取出列表中大于12的数，然后生成一个新的列表
li = [11,22,33]
new_list = filter(lambda a:a>12,li)
print(new_list)
for i in new_list:
    print(i)

#filter返回一个filter对象