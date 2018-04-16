# 遍历序列，对序列中每个元素进行操作，最终获得新的序列

li = [11,22,33]
new_list = map(lambda a: a + 10,li)
# print(new_list)
# for i in new_list:
#     print(i)

#新的队列是一个map的对象

li_1 = [2,4,5]
li_2 = [3,6,7]
n_list = map(lambda a,b:a+b,li_1,li_2)
for i in n_list:
    print(i)

